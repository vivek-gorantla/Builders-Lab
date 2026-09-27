# 02 - Expiring Cache

## What You Are Building
An in-memory key-value cache supporting per-entry expiration (TTL) and LRU (Least-Recently-Used) eviction when max capacity is reached.

## What You Will Learn
- Timestamp arithmetic and deadline tracking
- Designing LRU eviction mechanisms
- Efficient key lookup and cache state management

## Requirements
- Implement `ExpiringCache` in `solution.py`.
- Pass all unit tests in `tests/test_solution.py`.

## Getting Started
Open `solution.py` and replace `raise NotImplementedError` statements with your code.

## Testing
Run pytest:
```bash
python -m pytest
```
