from typing import Optional

class RateLimiter:
    """Sliding-window thread-safe rate limiter per client ID."""

    def __init__(self, limit: int, window_seconds: float) -> None:
        raise NotImplementedError("Implement __init__")

    def allow(self, client_id: str) -> bool:
        raise NotImplementedError("Implement allow")

    def get_remaining(self, client_id: str) -> int:
        raise NotImplementedError("Implement get_remaining")

    def reset(self, client_id: Optional[str] = None) -> None:
        raise NotImplementedError("Implement reset")
