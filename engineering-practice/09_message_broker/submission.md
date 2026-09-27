# Submission Guide - Project 09: Message Broker

Before submitting:
- [ ] Pub/Sub topic subscription and fan-out delivery working.
- [ ] `unsubscribe()` correctly removes callbacks.
- [ ] Subscriber exceptions are caught so other subscribers still receive messages.
- [ ] `async_mode=True` dispatches callbacks without blocking main thread.
- [ ] Tests pass.

## Evaluation Criteria
- **Functional Correctness**: 50 points
- **Observer Pattern & Architectural Decoupling**: 20 points
- **Error Isolation & Concurrency**: 10 points
- **Code Quality**: 10 points
- **Performance**: 10 points

**Total**: 100 points
