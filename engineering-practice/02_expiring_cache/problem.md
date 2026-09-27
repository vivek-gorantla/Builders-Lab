# Problem 02: Expiring Cache

## 1. Scenario
High-concurrency backend services rely on in-memory caches to reduce database load. You need to build a lightweight, in-memory cache component (resembling a mini Redis) that supports entry TTL (Time-To-Live) and optional maximum capacity with Least-Recently-Used (LRU) eviction.

## 2. Goal
Implement the `ExpiringCache` class without using external caching libraries.

## 3. Required Classes
- `ExpiringCache`

## 4. Required Methods
- `__init__(capacity: Optional[int] = None)`
- `set(key: str, value: Any, ttl: Optional[float] = None) -> None`
- `get(key: str) -> Any`
- `delete(key: str) -> bool`
- `exists(key: str) -> bool`
- `size() -> int`

## 5. Behavior
- `set`: Stores a key-value pair. An optional `ttl` (in seconds) specifies how long the key remains valid. If an item exceeds its TTL, it expires. If `capacity` is set and reached, evict the least recently used unexpired item.
- `get`: Retrieves the value associated with `key`. If the key is missing or expired, return `None`. Reading an active item refreshes its LRU access status.
- `delete`: Deletes a key from the cache. Returns `True` if key existed and was deleted, `False` otherwise.
- `exists`: Returns `True` if `key` exists and is not expired; otherwise `False`.
- `size`: Returns the current count of unexpired keys in the cache.

## 6. Validation Rules
- `capacity`, if provided, must be a positive integer (`capacity > 0`). Otherwise, raise `ValueError`.
- `ttl`, if provided, must be a positive float/int.
- Expired keys must never be returned by `get()`, counted in `size()`, or report `True` for `exists()`.

## 7. Edge Cases
- Overwriting an existing key updates its value, TTL, and LRU recency.
- Accessing an expired key should clean it up or treat it as absent.
- Reaching capacity when all existing keys are active vs. when some are expired.

## 8. Examples
```python
cache = ExpiringCache(capacity=2)
cache.set("session_1", {"user_id": 42}, ttl=60.0)
print(cache.get("session_1")) # {"user_id": 42}
```

## 9. Constraints
- Standard Python standard library only (e.g., `time`, `collections`). No Redis or external packages.

## 10. Left for Developer Decision
- Data structure chosen for LRU tracking (e.g., `collections.OrderedDict`, custom doubly-linked list, or timestamp tracking).
- Eager vs lazy cleanup strategy for expired entries.
