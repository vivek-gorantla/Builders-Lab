# 08 - Rate Limiter

## What You Are Building
A thread-safe, per-client sliding-window rate limiter component designed to prevent API abuse by throttling requests within a sliding time window.

## What You Will Learn
- Sliding-window algorithm implementation
- Thread safety and mutual exclusion (`threading.Lock`)
- Deque-based timestamp window tracking
- Memory leak prevention via stale request pruning

## Requirements
- Implement `RateLimiter` in `solution.py`.
- Pass pytest tests.

## Getting Started
Open `solution.py` and implement the stubbed methods.

## Testing
Run:
```bash
python -m pytest
```
