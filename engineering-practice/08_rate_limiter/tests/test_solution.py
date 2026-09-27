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
import threading
import pytest


from solution import RateLimiter

def test_invalid_configuration():
    with pytest.raises(ValueError):
        RateLimiter(limit=0, window_seconds=10)
    with pytest.raises(ValueError):
        RateLimiter(limit=5, window_seconds=0)

def test_allow_within_limit():
    limiter = RateLimiter(limit=3, window_seconds=1.0)
    assert limiter.allow("client_1") is True
    assert limiter.allow("client_1") is True
    assert limiter.allow("client_1") is True
    assert limiter.allow("client_1") is False

def test_sliding_window_expiration():
    limiter = RateLimiter(limit=2, window_seconds=0.2)
    assert limiter.allow("alice") is True
    assert limiter.allow("alice") is True
    assert limiter.allow("alice") is False

    time.sleep(0.25)
    # Window expired, should allow again
    assert limiter.allow("alice") is True

def test_multiple_clients_independent():
    limiter = RateLimiter(limit=1, window_seconds=1.0)
    assert limiter.allow("client_a") is True
    assert limiter.allow("client_b") is True
    assert limiter.allow("client_a") is False
    assert limiter.allow("client_b") is False

def test_get_remaining_and_reset():
    limiter = RateLimiter(limit=3, window_seconds=10.0)
    limiter.allow("user1")
    assert limiter.get_remaining("user1") == 2
    limiter.reset("user1")
    assert limiter.get_remaining("user1") == 3

def test_empty_client_id_raises_error():
    limiter = RateLimiter(limit=5, window_seconds=10)
    with pytest.raises(ValueError):
        limiter.allow("")

def test_thread_safety():
    limiter = RateLimiter(limit=50, window_seconds=5.0)
    threads = []
    allowed_count = [0]
    lock = threading.Lock()

    def make_request():
        if limiter.allow("shared_client"):
            with lock:
                allowed_count[0] += 1

    for _ in range(100):
        t = threading.Thread(target=make_request)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    assert allowed_count[0] == 50