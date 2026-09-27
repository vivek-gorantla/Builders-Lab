# 06 - Notification Engine

## What You Are Building
A pluggable notification engine using the Strategy Pattern to dispatch messages to different channel providers (Email, SMS, Push), supporting configurable retry logic and audit history logging.

## What You Will Learn
- Object-Oriented Design & Strategy Pattern
- Abstract Base Classes (`abc.ABC`)
- Dependency Injection
- Failure retry policies and history tracking

## Requirements
- Complete `NotificationEngine` in `solution.py`.
- Pass all unit tests in `tests/test_solution.py`.

## Getting Started
Open `solution.py` and implement the stubbed methods.

## Testing
Run:
```bash
python -m pytest
```
