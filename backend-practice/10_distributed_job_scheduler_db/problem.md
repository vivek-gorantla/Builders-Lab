# Problem 10: DB-Backed Background Job Scheduler Engine

## 1. Scenario
Distributed task queues (like Celery, Sidekiq, or Temporal) persist job execution state in databases (PostgreSQL/MySQL), allowing worker nodes to poll due jobs, lock jobs for execution, and handle retries.

## 2. Goal
Implement `DBJobScheduler` managing background tasks in a DB table.

## 3. Required Class
- `DBJobScheduler`

## 4. Required Methods
- `register_task_handler(task_type: str, handler: Callable[[dict], Any]) -> None`
- `enqueue_job(task_type: str, payload: dict, run_at: Optional[float] = None, max_retries: int = 3) -> str`
- `poll_and_execute_next_job(worker_id: str) -> Optional[dict]`
- `get_job_status(job_id: str) -> dict`
- `retry_failed_jobs() -> int`

## 5. Behavior
- `enqueue_job`: Inserts job into DB `jobs` table with `status="PENDING"`, `run_at` (defaults to current timestamp), and `max_retries`. Returns `job_id`.
- `poll_and_execute_next_job`: Within a DB transaction lock, selects the oldest `PENDING` or `FAILED` (with retries remaining) job where `run_at <= current_time`. Updates status to `"RUNNING"` assigned to `worker_id`. Executes registered handler callback.
  - If handler succeeds: Update status to `"COMPLETED"`.
  - If handler raises exception: Increment `retries_attempted`. If `retries_attempted >= max_retries`, mark `"PERMANENTLY_FAILED"`. Otherwise mark `"FAILED"`.

## 6. Validation Rules
- Enqueuing task with unregistered `task_type` raises `ValueError`.

## 7. Edge Cases
- Polling when no pending jobs are available returns `None`.

## 8. Examples
```python
sched = DBJobScheduler()
sched.register_task_handler("task1", print)
jid = sched.enqueue_job("task1", {"msg": "hi"})
sched.poll_and_execute_next_job("w1")
```

## 9. Constraints
- SQLite / PostgreSQL DB connection compatibility.

## 10. Left for Developer Decision
- DB table schema (`jobs` table with `job_id`, `task_type`, `payload_json`, `status`, `run_at`, `max_retries`, `retries_attempted`, `worker_id`).
