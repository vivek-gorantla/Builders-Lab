# Problem 07: Task Scheduler

## 1. Scenario
Cron services and job schedulers run tasks at exact specified future timestamps. You need to build an in-memory task scheduler component using priority queue ordering and background thread execution.

## 2. Goal
Implement `TaskScheduler` using Python's `heapq`, `threading`, and `time` modules.

## 3. Required Classes
- `TaskScheduler`

## 4. Required Methods
- `schedule(task_id: str, function: Callable, run_at: Union[float, datetime], *args, **kwargs) -> None`
- `cancel(task_id: str) -> bool`
- `get_task(task_id: str) -> dict`
- `start() -> None`
- `stop() -> None`

## 5. Behavior
- Task statuses: `SCHEDULED`, `COMPLETED`, `FAILED`, `CANCELLED`.
- `schedule`: Schedules a task to execute at `run_at` (epoch timestamp float or `datetime` instance). Converts `datetime` to epoch float internally if needed. Status set to `SCHEDULED`.
- `cancel`: Cancels a pending task. Status changes to `CANCELLED`. Returns `True` if cancelled, `False` if already executed/failed.
- `get_task`: Returns task metadata dict (`task_id`, `run_at`, `status`).
- `start`: Starts a background thread that continuously checks the earliest scheduled task in the priority queue and executes it when current time $\ge$ scheduled `run_at`.
- `stop`: Gracefully stops the background scheduler thread.

## 6. Validation Rules
- Duplicate `task_id` raises `ValueError`.
- Querying non-existent `task_id` raises `KeyError`.
- If a scheduled task raises an exception during execution, record status as `FAILED` without breaking the scheduler thread.

## 7. Edge Cases
- Scheduling a task with `run_at` in the past (should execute immediately upon start).
- Cancelling a task that is currently executing or finished.
- Multiple tasks scheduled for the exact same timestamp.

## 8. Examples
```python
scheduler = TaskScheduler()
scheduler.schedule("reminder", print, time.time() + 5.0, "Time up!")
scheduler.start()
# task runs in 5 seconds
scheduler.stop()
```

## 9. Constraints
- Use standard library `heapq`, `threading`, `time`.

## 10. Left for Developer Decision
- Priority heap item structure (tuple of `(run_at, task_id)`).
- Thread sleep interval calculation (sleeping until next task vs short poll).
