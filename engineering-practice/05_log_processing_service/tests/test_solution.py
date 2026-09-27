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


from solution import LogAnalyzer

def test_parse_line_valid():
    analyzer = LogAnalyzer()
    line = "2026-09-27 10:15:01 INFO user=12 endpoint=/users"
    parsed = analyzer.parse_line(line)
    assert parsed is not None
    assert parsed["timestamp"] == "2026-09-27 10:15:01"
    assert parsed["level"] == "INFO"
    assert parsed["user"] == "12"
    assert parsed["endpoint"] == "/users"

def test_parse_line_malformed():
    analyzer = LogAnalyzer()
    assert analyzer.parse_line("bad line content") is None
    assert analyzer.parse_line("") is None

def test_process_file(tmp_path):
    log_content = (
        "2026-09-27 10:15:01 INFO user=12 endpoint=/users\n"
        "2026-09-27 10:15:04 ERROR user=14 endpoint=/payments\n"
        "2026-09-27 10:15:08 INFO user=12 endpoint=/orders\n"
        "2026-09-27 10:15:10 WARNING user=15 endpoint=/users\n"
        "MALFORMED LINE TO IGNORE\n"
    )
    log_file = tmp_path / "server.log"
    log_file.write_text(log_content)

    analyzer = LogAnalyzer()
    processed_count = analyzer.process_file(log_file)
    assert processed_count == 4
    assert analyzer.get_request_count() == 4
    assert analyzer.get_error_count() == 1

def test_top_endpoints_and_users(tmp_path):
    log_content = (
        "2026-09-27 10:00:00 INFO user=u1 endpoint=/home\n"
        "2026-09-27 10:00:01 INFO user=u1 endpoint=/home\n"
        "2026-09-27 10:00:02 INFO user=u2 endpoint=/api/v1\n"
    )
    log_file = tmp_path / "test.log"
    log_file.write_text(log_content)

    analyzer = LogAnalyzer()
    analyzer.process_file(log_file)

    top_ep = analyzer.get_top_endpoints(limit=1)
    assert top_ep == [("/home", 2)]

    top_usr = analyzer.get_top_users(limit=1)
    assert top_usr == [("u1", 2)]

def test_get_status_summary(tmp_path):
    log_content = (
        "2026-09-27 10:00:00 INFO user=u1 endpoint=/home\n"
        "2026-09-27 10:00:01 ERROR user=u1 endpoint=/home\n"
    )
    log_file = tmp_path / "summary.log"
    log_file.write_text(log_content)

    analyzer = LogAnalyzer()
    analyzer.process_file(log_file)
    summary = analyzer.get_status_summary()
    assert summary["INFO"] == 1
    assert summary["ERROR"] == 1

def test_missing_file_raises_error():
    analyzer = LogAnalyzer()
    with pytest.raises(FileNotFoundError):
        analyzer.process_file("non_existent_log_file.log")