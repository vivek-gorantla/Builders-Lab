from typing import Callable, Any, List, Optional

class MessageBroker:
    """In-memory publish/subscribe message broker with subscriber isolation and async mode."""

    def __init__(self) -> None:
        raise NotImplementedError("Implement __init__")

    def subscribe(self, topic: str, callback: Callable[[Any], None]) -> None:
        raise NotImplementedError("Implement subscribe")

    def unsubscribe(self, topic: str, callback: Callable[[Any], None]) -> bool:
        raise NotImplementedError("Implement unsubscribe")

    def publish(self, topic: str, message: Any, async_mode: bool = False) -> None:
        raise NotImplementedError("Implement publish")

    def get_subscriber_count(self, topic: str) -> int:
        raise NotImplementedError("Implement get_subscriber_count")
