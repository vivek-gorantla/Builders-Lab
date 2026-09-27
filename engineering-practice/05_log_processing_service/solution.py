from pathlib import Path
from typing import Union, Dict, Any, List, Tuple, Optional

class LogAnalyzer:
    """Stream-based log processing service for extracting metric insights from structured log files."""

    def __init__(self) -> None:
        raise NotImplementedError("Implement __init__")

    def parse_line(self, line: str) -> Optional[Dict[str, str]]:
        raise NotImplementedError("Implement parse_line")

    def process_file(self, path: Union[str, Path]) -> int:
        raise NotImplementedError("Implement process_file")

    def get_error_count(self) -> int:
        raise NotImplementedError("Implement get_error_count")

    def get_request_count(self) -> int:
        raise NotImplementedError("Implement get_request_count")

    def get_top_endpoints(self, limit: int = 5) -> List[Tuple[str, int]]:
        raise NotImplementedError("Implement get_top_endpoints")

    def get_top_users(self, limit: int = 5) -> List[Tuple[str, int]]:
        raise NotImplementedError("Implement get_top_users")

    def get_status_summary(self) -> Dict[str, int]:
        raise NotImplementedError("Implement get_status_summary")
