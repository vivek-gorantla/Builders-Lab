import sys
import os
import sqlite3
import pytest

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']

from solution import DBJobScheduler

@pytest.fixture
def db_conn():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()

def test_enqueue_and_execute_job(db_conn):
    scheduler = DBJobScheduler(db_conn)
    results = []

    def email_handler(payload):
        results.append(payload["to"])
        return "SENT"

    scheduler.register_task_handler("send_email", email_handler)
    job_id = scheduler.enqueue_job("send_email", {"to": "user@example.com"})

    status_before = scheduler.get_job_status(job_id)
    assert status_before["status"] == "PENDING"

    executed = scheduler.poll_and_execute_next_job("worker_1")
    assert executed is not None
    assert executed["job_id"] == job_id
    assert results == ["user@example.com"]

    status_after = scheduler.get_job_status(job_id)
    assert status_after["status"] == "COMPLETED"

def test_job_execution_failure_and_retries(db_conn):
    scheduler = DBJobScheduler(db_conn)

    def failing_handler(payload):
        raise RuntimeError("Service unavailable")

    scheduler.register_task_handler("flaky_job", failing_handler)
    job_id = scheduler.enqueue_job("flaky_job", {"attempt": 1}, max_retries=2)

    # Worker executes and fails
    scheduler.poll_and_execute_next_job("w1")
    status = scheduler.get_job_status(job_id)
    assert status["status"] == "FAILED"
    assert status["retries_attempted"] == 1
