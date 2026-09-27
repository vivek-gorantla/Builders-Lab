# Submission Guide - Project 08: Rate Limiter

Before submitting:
- [ ] Constructor validates `limit > 0` and `window_seconds > 0`.
- [ ] Sliding-window algorithm prunes expired timestamps properly.
- [ ] `allow()` returns True/False accurately according to client history.
- [ ] `threading.Lock` guarantees thread safety under concurrent requests.
- [ ] Tests pass.

## Evaluation Criteria
- **Functional Correctness**: 50 points
- **Sliding Window Algorithm & Thread Safety**: 20 points
- **Validation & Error Handling**: 10 points
- **Code Quality**: 10 points
- **Performance**: 10 points

**Total**: 100 points
