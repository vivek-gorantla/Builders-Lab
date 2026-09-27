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
import pytest


from solution import JobQueue

def sample_task(x, y):
    return x + y

def failing_task():
    raise RuntimeError("Task failure")

def test_submit_and_get_status_pending():
    jq = JobQueue()
    jq.submit("job1", sample_task, 2, 3)
    assert jq.get_status("job1") == "PENDING"

def test_duplicate_job_id_raises_error():
    jq = JobQueue()
    jq.submit("job1", sample_task, 2, 3)
    with pytest.raises(ValueError):
        jq.submit("job1", sample_task, 4, 5)

def test_worker_execution_completed():
    jq = JobQueue()
    jq.submit("job1", sample_task, 10, 20)
    jq.start_worker(num_workers=1)
    time.sleep(0.2)
    assert jq.get_status("job1") == "COMPLETED"
    jq.stop_worker()

def test_worker_handles_failing_job():
    jq = JobQueue()
    jq.submit("job_fail", failing_task)
    jq.start_worker(num_workers=1)
    time.sleep(0.2)
    assert jq.get_status("job_fail") == "FAILED"
    jq.stop_worker()

def test_cancel_pending_job():
    jq = JobQueue()
    jq.submit("job_cancel", sample_task, 1, 1)
    assert jq.cancel("job_cancel") is True
    assert jq.get_status("job_cancel") == "CANCELLED"
    jq.start_worker(num_workers=1)
    time.sleep(0.1)
    # Ensure cancelled job was skipped
    assert jq.get_status("job_cancel") == "CANCELLED"
    jq.stop_worker()

def test_unknown_job_id_raises_error():
    jq = JobQueue()
    with pytest.raises(KeyError):
        jq.get_status("unknown")