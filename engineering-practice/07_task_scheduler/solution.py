import time
from datetime import datetime
from typing import Callable, Any, Optional, Union, Dict

class TaskScheduler:
    """In-memory task scheduler executing tasks at specified future times using priority queues."""

    def __init__(self) -> None:
        raise NotImplementedError("Implement __init__")

    def schedule(self, task_id: str, function: Callable, run_at: Union[float, datetime], *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError("Implement schedule")

    def cancel(self, task_id: str) -> bool:
        raise NotImplementedError("Implement cancel")

    def get_task(self, task_id: str) -> Dict[str, Any]:
        raise NotImplementedError("Implement get_task")

    def start(self) -> None:
        raise NotImplementedError("Implement start")

    def stop(self) -> None:
        raise NotImplementedError("Implement stop")
