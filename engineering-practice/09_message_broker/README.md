# 09 - Message Broker

## What You Are Building
An in-memory Pub/Sub message broker supporting multi-topic message fan-out, subscriber error isolation, and optional async dispatch.

## What You Will Learn
- Observer Pattern implementation
- Decoupled event-driven architecture
- Exception isolation (preventing consumer failures from crashing producers)
- Asynchronous callback invocation using threads

## Requirements
- Complete `MessageBroker` in `solution.py`.
- Pass all pytest tests in `tests/test_solution.py`.

## Getting Started
Open `solution.py` and fill in the missing methods.

## Testing
Run:
```bash
python -m pytest
```
