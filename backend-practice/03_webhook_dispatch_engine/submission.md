# Submission Guide - Project 03: Webhook Delivery Engine

Verify:
- [ ] HMAC SHA256 signature computed for every payload.
- [ ] Event fan-out dispatches to subscribed endpoints only.
- [ ] Failed attempts retry up to `max_retries` before moving to DLQ.
- [ ] Tests pass.

## Rubric
- Functional Correctness: 50 | Webhook Security & Retry Policy: 20 | Error Handling: 10 | Code Quality: 10 | Performance: 10
