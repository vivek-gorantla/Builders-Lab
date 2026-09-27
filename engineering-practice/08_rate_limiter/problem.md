# Problem 08: Rate Limiter

## 1. Scenario
API gateways enforce rate limits to protect backend servers against abuse and denial-of-service attacks. You need to build a reusable, thread-safe rate limiter component implementing a sliding-window algorithm per client ID.

## 2. Goal
Implement `RateLimiter` using thread locks and timestamp queues.

## 3. Required Classes
- `RateLimiter`

## 4. Required Methods
- `__init__(limit: int, window_seconds: float)`
- `allow(client_id: str) -> bool`
- `get_remaining(client_id: str) -> int`
- `reset(client_id: Optional[str] = None) -> None`

## 5. Behavior
- Constructor: Initializes with maximum allowed requests (`limit`) within sliding time window (`window_seconds`).
- `allow`: Checks if `client_id` has exceeded `limit` requests within the trailing `window_seconds`. If under limit, records request timestamp and returns `True`. Otherwise returns `False`.
- `get_remaining`: Returns available remaining quota for `client_id` in current window.
- `reset`: Resets request history for a specific `client_id` (or all clients if `client_id` is `None`).

## 6. Validation Rules
- `limit <= 0` or `window_seconds <= 0` must raise `ValueError`.
- Empty or non-string `client_id` in `allow` must raise `ValueError`.
- Must be thread-safe (`threading.Lock`).

## 7. Edge Cases
- Bursts of requests arriving within milliseconds of each other.
- Independent rate tracking across thousands of distinct client IDs.
- Expired timestamps being cleaned up so memory does not leak.

## 8. Examples
```python
limiter = RateLimiter(limit=3, window_seconds=10)
print(limiter.allow("alice")) # True
print(limiter.allow("alice")) # True
print(limiter.allow("alice")) # True
print(limiter.allow("alice")) # False (rate limited)
```

## 9. Constraints
- Implement sliding-window algorithm. Do not use standard fixed-window reset.
- Thread-safe concurrency using `threading.Lock`.

## 10. Left for Developer Decision
- Standard library data structure for per-client timestamps (`collections.deque` vs list).
- Strategy for timestamp eviction.
