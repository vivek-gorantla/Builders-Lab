# 03 - Real-Time Webhook Delivery Engine

## What You Are Building
A Stripe-grade webhook event distribution engine featuring HMAC SHA256 payload signing, retry attempts, and Dead Letter Queue (DLQ) routing.

## What You Will Learn
- Webhook signature generation (`hmac.new`)
- Event fan-out delivery pattern
- Retry backoff policies & Dead Letter Queues

## Testing
```bash
python -m pytest
```
