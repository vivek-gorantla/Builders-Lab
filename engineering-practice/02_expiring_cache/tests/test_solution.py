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


from solution import ExpiringCache

def test_set_and_get_basic():
    cache = ExpiringCache()
    cache.set("a", 100)
    assert cache.get("a") == 100
    assert cache.exists("a") is True
    assert cache.size() == 1

def test_get_nonexistent_returns_none():
    cache = ExpiringCache()
    assert cache.get("missing") is None
    assert cache.exists("missing") is False

def test_ttl_expiration():
    cache = ExpiringCache()
    cache.set("temp", "val", ttl=0.1)
    assert cache.get("temp") == "val"
    time.sleep(0.15)
    assert cache.get("temp") is None
    assert cache.exists("temp") is False
    assert cache.size() == 0

def test_delete():
    cache = ExpiringCache()
    cache.set("k1", "v1")
    assert cache.delete("k1") is True
    assert cache.exists("k1") is False
    assert cache.delete("k1") is False

def test_lru_eviction():
    cache = ExpiringCache(capacity=3)
    cache.set("k1", 1)
    cache.set("k2", 2)
    cache.set("k3", 3)

    # Access k1 to make it recently used -> order of usage: k2, k3, k1
    assert cache.get("k1") == 1

    # Insert k4 -> should evict k2 (least recently used)
    cache.set("k4", 4)
    assert cache.exists("k2") is False
    assert cache.get("k1") == 1
    assert cache.get("k3") == 3
    assert cache.get("k4") == 4
    assert cache.size() == 3

def test_invalid_capacity():
    with pytest.raises(ValueError):
        ExpiringCache(capacity=0)
    with pytest.raises(ValueError):
        ExpiringCache(capacity=-5)

def test_ttl_none_never_expires():
    cache = ExpiringCache()
    cache.set("perm", "data", ttl=None)
    time.sleep(0.05)
    assert cache.get("perm") == "data"