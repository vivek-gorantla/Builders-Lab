import sys
import os

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']
import sys
import os
import pytest
from pathlib import Path


from solution import FileIndexer

def test_index_directory_and_stats(tmp_path):
    # Create temp files
    (tmp_path / "file1.txt").write_text("Hello World")
    (tmp_path / "file2.py").write_text("print('test')")
    sub_dir = tmp_path / "subdir"
    sub_dir.mkdir()
    (sub_dir / "file3.txt").write_text("Nested text file")

    indexer = FileIndexer()
    indexed_count = indexer.index_directory(tmp_path)
    assert indexed_count == 3

    stats = indexer.get_statistics()
    assert stats["total_files"] == 3
    assert stats["extension_counts"].get(".txt") == 2
    assert stats["extension_counts"].get(".py") == 1

def test_search_by_name(tmp_path):
    (tmp_path / "report_2026.pdf").write_bytes(b"pdf data")
    (tmp_path / "invoice.pdf").write_bytes(b"invoice data")

    indexer = FileIndexer()
    indexer.index_directory(tmp_path)

    results = indexer.search_by_name("report")
    assert len(results) == 1
    assert results[0]["name"] == "report_2026.pdf"

def test_search_by_extension(tmp_path):
    (tmp_path / "doc1.txt").write_text("data")
    (tmp_path / "script.py").write_text("data")

    indexer = FileIndexer()
    indexer.index_directory(tmp_path)

    # Search with dot and without dot
    res_dot = indexer.search_by_extension(".txt")
    res_no_dot = indexer.search_by_extension("txt")
    assert len(res_dot) == 1
    assert len(res_no_dot) == 1

def test_find_largest_files(tmp_path):
    (tmp_path / "small.txt").write_bytes(b"a" * 10)
    (tmp_path / "large.txt").write_bytes(b"a" * 1000)
    (tmp_path / "medium.txt").write_bytes(b"a" * 100)

    indexer = FileIndexer()
    indexer.index_directory(tmp_path)

    largest = indexer.find_largest_files(limit=2)
    assert len(largest) == 2
    assert largest[0]["name"] == "large.txt"
    assert largest[1]["name"] == "medium.txt"

def test_nonexistent_directory():
    indexer = FileIndexer()
    with pytest.raises(FileNotFoundError):
        indexer.index_directory("non_existent_folder_xyz_123")