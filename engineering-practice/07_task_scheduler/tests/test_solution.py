import sys
import os

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']
import sys
import os
import time
from datetime import datetime, timedelta
import pytest


from solution import TaskScheduler

def sample_fn(container, val):
    container.append(val)

def failing_fn():
    raise RuntimeError("Scheduler task failure")

def test_schedule_and_get_task():
    scheduler = TaskScheduler()
    run_time = time.time() + 10
    scheduler.schedule("t1", sample_fn, run_time, [], 42)

    task_info = scheduler.get_task("t1")
    assert task_info["task_id"] == "t1"
    assert task_info["status"] == "SCHEDULED"

def test_duplicate_task_id_raises_error():
    scheduler = TaskScheduler()
    scheduler.schedule("t1", sample_fn, time.time() + 10)
    with pytest.raises(ValueError):
        scheduler.schedule("t1", sample_fn, time.time() + 20)

def test_execution_at_scheduled_time():
    scheduler = TaskScheduler()
    results = []
    run_at = time.time() + 0.1
    scheduler.schedule("t_exec", sample_fn, run_at, results, "executed")

    scheduler.start()
    time.sleep(0.3)
    scheduler.stop()

    assert results == ["executed"]
    assert scheduler.get_task("t_exec")["status"] == "COMPLETED"

def test_cancel_task():
    scheduler = TaskScheduler()
    results = []
    run_at = time.time() + 0.2
    scheduler.schedule("t_cancel", sample_fn, run_at, results, "never")

    assert scheduler.cancel("t_cancel") is True
    assert scheduler.get_task("t_cancel")["status"] == "CANCELLED"

    scheduler.start()
    time.sleep(0.3)
    scheduler.stop()

    assert results == []

def test_failed_task_recorded():
    scheduler = TaskScheduler()
    run_at = time.time() + 0.05
    scheduler.schedule("t_fail", failing_fn, run_at)

    scheduler.start()
    time.sleep(0.2)
    scheduler.stop()

    assert scheduler.get_task("t_fail")["status"] == "FAILED"

def test_unknown_task_raises_key_error():
    scheduler = TaskScheduler()
    with pytest.raises(KeyError):
        scheduler.get_task("nonexistent")