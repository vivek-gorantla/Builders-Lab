# 10 - DB-Backed Background Job Scheduler Engine

## What You Are Building
A production-grade DB-backed background task scheduler engine managing task handlers, job polling concurrency, exception retries, and job status lifecycles.

## What You Will Learn
- Celery / Sidekiq DB queue architecture
- Database transaction locking for job workers
- Exception handling & automatic retry policies

## Testing
```bash
python -m pytest
```
