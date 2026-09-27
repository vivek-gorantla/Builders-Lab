# Problem 05: Log Processing Service

## 1. Scenario
Production backend systems generate large volumes of log files. Operations teams require efficient analyzers to parse log records, track error spikes, identify top active users, and discover hot API endpoints without loading entire multi-gigabyte log files into RAM.

## 2. Goal
Build a memory-efficient, stream-based log analyzer class `LogAnalyzer`.

## 3. Required Classes
- `LogAnalyzer`

## 4. Required Methods
- `parse_line(line: str) -> Optional[dict]`
- `process_file(path: Union[str, Path]) -> int`
- `get_error_count() -> int`
- `get_request_count() -> int`
- `get_top_endpoints(limit: int = 5) -> list[tuple[str, int]]`
- `get_top_users(limit: int = 5) -> list[tuple[str, int]]`
- `get_status_summary() -> dict[str, int]`

## 5. Behavior
- Expected log format: `<YYYY-MM-DD HH:MM:SS> <LEVEL> user=<USER_ID> endpoint=<ENDPOINT>`
- `parse_line`: Parses a single line string into a dictionary with keys `timestamp`, `level`, `user`, `endpoint`. Returns `None` if line is malformed.
- `process_file`: Streams and processes the file line-by-line. Skips malformed lines. Returns the count of valid log entries processed.
- `get_error_count`: Returns total lines with level `ERROR`.
- `get_request_count`: Returns total valid log lines processed.
- `get_top_endpoints`: Returns a list of `(endpoint_path, count)` tuples sorted by count descending.
- `get_top_users`: Returns a list of `(user_id, count)` tuples sorted by count descending.
- `get_status_summary`: Returns a dictionary mapping log levels (e.g., `"INFO"`, `"ERROR"`, `"WARNING"`) to their total occurrences.

## 6. Validation Rules
- Malformed lines must return `None` from `parse_line` and be ignored during file streaming without raising exceptions.
- `process_file` on a non-existent file path must raise `FileNotFoundError`.

## 7. Edge Cases
- Blank lines or lines with missing key-value pairs.
- Multiple calls to `process_file` accumulating statistics.
- Log levels with 0 occurrences.

## 8. Examples
Input log line:
`2026-09-27 10:15:01 INFO user=12 endpoint=/users`
Output parsed dict:
`{"timestamp": "2026-09-27 10:15:01", "level": "INFO", "user": "12", "endpoint": "/users"}`

## 9. Constraints
- Files must be processed using line streaming (`for line in f:`) to avoid loading large files completely into memory.

## 10. Left for Developer Decision
- String parsing methodology (regular expressions vs `split()`).
- Data structure used for aggregation (e.g., `collections.Counter` or standard `dict`).
