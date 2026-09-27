# Problem 04: File Indexer

## 1. Scenario
Desktop search tools and IDEs index local files to enable fast keyword search, file-type filtering, and storage analytics. You need to build a local file indexing system that traverses a given directory tree and indexes metadata.

## 2. Goal
Implement the `FileIndexer` class using Python's `pathlib` module.

## 3. Required Classes
- `FileIndexer`

## 4. Required Methods
- `index_directory(path: Union[str, Path]) -> int`
- `search_by_name(query: str) -> list[dict]`
- `search_by_extension(extension: str) -> list[dict]`
- `find_largest_files(limit: int = 10) -> list[dict]`
- `get_statistics() -> dict`

## 5. Behavior
- Metadata schema per file: `name` (str), `path` (str), `extension` (str, e.g., `.py`), `size` (bytes, int), `modified_at` (float timestamp).
- `index_directory`: Recursively traverses directory `path`. Returns count of files indexed.
- `search_by_name`: Performs case-insensitive substring search on file names. Returns matching file metadata dicts.
- `search_by_extension`: Returns all files matching `extension` (handles leading dot gracefully, e.g., `.txt` or `txt`).
- `find_largest_files`: Returns top `limit` largest files sorted descending by file size.
- `get_statistics`: Returns summary dict with `total_files` (int), `total_size_bytes` (int), `extension_counts` (dict mapping extension string to count).

## 6. Validation Rules
- If specified `path` does not exist or is not a directory, raise `FileNotFoundError` or `ValueError`.
- Permission issues or unreadable files during traversal should be caught and skipped gracefully without crashing.

## 7. Edge Cases
- Files with no extension.
- Hidden files (starting with `.`).
- Empty directories.
- Searching when index is empty.

## 8. Examples
```python
indexer = FileIndexer()
indexer.index_directory("./my_project")
results = indexer.search_by_extension("py")
```

## 9. Constraints
- Use standard library modules (`pathlib`, `os`). Do not use third-party search engines (like ElasticSearch or Lucene).

## 10. Left for Developer Decision
- Internal data structure for stored index.
- Efficient lookup indices vs scan-on-query.
