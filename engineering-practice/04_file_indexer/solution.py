from pathlib import Path
from typing import Union, List, Dict, Any

class FileIndexer:
    """Local file indexing system for directory scanning, metadata indexing, and search."""

    def __init__(self) -> None:
        raise NotImplementedError("Implement __init__")

    def index_directory(self, path: Union[str, Path]) -> int:
        raise NotImplementedError("Implement index_directory")

    def search_by_name(self, query: str) -> List[Dict[str, Any]]:
        raise NotImplementedError("Implement search_by_name")

    def search_by_extension(self, extension: str) -> List[Dict[str, Any]]:
        raise NotImplementedError("Implement search_by_extension")

    def find_largest_files(self, limit: int = 10) -> List[Dict[str, Any]]:
        raise NotImplementedError("Implement find_largest_files")

    def get_statistics(self) -> Dict[str, Any]:
        raise NotImplementedError("Implement get_statistics")
