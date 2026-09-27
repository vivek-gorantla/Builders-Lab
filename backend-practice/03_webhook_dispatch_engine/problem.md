# Problem 03: Real-Time Webhook Delivery Engine

## 1. Scenario
API platforms like Stripe and GitHub deliver real-time webhooks to customer endpoints. The delivery engine signs payloads with HMAC signatures (`X-Webhook-Signature`), retries failed HTTP attempts with backoff, and routes permanently failing events to a Dead Letter Queue (DLQ).

## 2. Goal
Build `WebhookEngine` managing webhook client subscriptions, event fan-out, HMAC signatures, and retry delivery logic.

## 3. Required Class
- `WebhookEngine`

## 4. Required Methods
- `register_endpoint(client_id: str, target_url: str, secret: str, subscribed_events: list[str]) -> str`
- `dispatch_event(event_type: str, payload: dict) -> str`
- `get_delivery_logs(event_id: str) -> list[dict]`
- `process_pending_deliveries() -> int`
- `get_dead_letter_queue() -> list[dict]`

## 5. Behavior
- `register_endpoint`: Registers target URL, secret key, and subscribed event types. Returns `endpoint_id`.
- `dispatch_event`: Generates unique `event_id`, computes HMAC SHA256 signature of JSON payload using endpoint's `secret`, and enqueues delivery attempts for all endpoints subscribed to `event_type`.
- `process_pending_deliveries`: Simulates/executes webhook dispatch attempts. Increments `attempt_count`. If attempt succeeds, mark `"DELIVERED"`. If attempt fails, increment retries. If `attempt_count >= max_retries`, move event delivery to Dead Letter Queue (`"DEAD_LETTER"`).

## 6. Validation Rules
- Invalid URL format or empty payload raises `ValueError`.

## 7. Edge Cases
- Event dispatched with 0 subscribers completes cleanly without error.

## 8. Examples
```python
engine = WebhookEngine()
engine.register_endpoint("c1", "https://example.com/hook", "secret", ["payment.success"])
event_id = engine.dispatch_event("payment.success", {"id": "px_100"})
```

## 9. Constraints
- Pure Python standard library (`hmac`, `hashlib`, `json`, `time`).

## 10. Left for Developer Decision
- Mock HTTP dispatcher simulation vs real urllib HTTP request sender.
