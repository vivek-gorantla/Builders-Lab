# Submission Guide - Project 03: Job Queue

Before submitting:
- [ ] Duplicate job IDs raise `ValueError`.
- [ ] Status transitions correctly through PENDING -> RUNNING -> COMPLETED/FAILED/CANCELLED.
- [ ] Worker exceptions are caught and mark status as FAILED without dying.
- [ ] Worker threads shut down cleanly upon `stop_worker()`.
- [ ] Tests pass.

## Evaluation Criteria
- **Functional Correctness**: 50 points
- **Concurrency & Thread Safety**: 20 points
- **Error Handling**: 10 points
- **Code Quality**: 10 points
- **Performance**: 10 points

**Total**: 100 points
