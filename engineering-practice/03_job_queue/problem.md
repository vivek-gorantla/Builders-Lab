# Problem 03: Job Queue

## 1. Scenario
Asynchronous job processing is essential for tasks like sending background emails, generating PDFs, or image processing. You need to build an in-memory job queue that manages submitted tasks, dispatches them to worker threads, tracks their state lifecycle, and allows task cancellation.

## 2. Goal
Implement the `JobQueue` class using Python's `threading` and `queue` modules.

## 3. Required Classes
- `JobQueue`

## 4. Required Methods
- `submit(job_id: str, function: Callable, *args, **kwargs) -> None`
- `get_status(job_id: str) -> str`
- `cancel(job_id: str) -> bool`
- `start_worker(num_workers: int = 1) -> None`
- `stop_worker() -> None`

## 5. Behavior
- Job States: `PENDING`, `RUNNING`, `COMPLETED`, `FAILED`, `CANCELLED`.
- `submit`: Enqueues a callable task with a unique string `job_id`. Sets status to `PENDING`.
- `get_status`: Returns the current string status of `job_id`.
- `cancel`: Cancels a `PENDING` job before execution, setting status to `CANCELLED` and returning `True`. If job is already `RUNNING`, `COMPLETED`, `FAILED`, or `CANCELLED`, return `False`.
- `start_worker`: Spawns worker threads that pull jobs from the queue and execute them sequentially in FIFO order. Updates status to `RUNNING` before execution, and `COMPLETED` or `FAILED` after.
- `stop_worker`: Signals worker threads to stop processing cleanly and waits for running threads to terminate (`join`).

## 6. Validation Rules
- `job_id` must be unique. Submitting a duplicate ID raises `ValueError`.
- `get_status` on an unknown `job_id` raises `KeyError`.
- Worker threads must catch any exception raised during job execution without terminating the worker thread itself.

## 7. Edge Cases
- Worker encounters a cancelled job in the queue (should skip execution).
- Stopping worker threads when no jobs were ever submitted.
- Submitting jobs while workers are already running.

## 8. Examples
```python
jq = JobQueue()
jq.submit("job_1", print, "Hello World")
jq.start_worker(2)
# worker processes job_1
jq.stop_worker()
```

## 9. Constraints
- Must use standard Python concurrency modules (`threading`, `queue`, `concurrent.futures`). No Celery or Redis.

## 10. Left for Developer Decision
- How to signal worker threads to shutdown (e.g. sentinel value or event flag).
- Synchronization primitive for status updates.
