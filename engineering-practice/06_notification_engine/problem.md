# Problem 06: Notification Engine

## 1. Scenario
Modern applications notify users across multiple communication channels (Email, SMS, Push notifications). You need to build a modular notification engine that accepts different provider implementations, validates parameters, retries transient delivery failures, and maintains audit logs.

## 2. Goal
Design and implement the strategy-pattern based `NotificationEngine` class.

## 3. Required Classes
- `BaseNotificationProvider` (Abstract base class)
- `EmailProvider`, `SmsProvider`, `PushProvider` (Fake providers)
- `NotificationEngine`

## 4. Required Methods
- `register_channel(channel_name: str, provider: BaseNotificationProvider) -> None`
- `send(channel_name: str, recipient: str, message: str) -> str`
- `send_bulk(channel_name: str, recipients: list[str], message: str) -> list[str]`
- `get_history(notification_id: Optional[str] = None) -> Union[list[dict], dict]`

## 5. Behavior
- Provider Interface: Each provider implements `send(recipient, message) -> bool`.
- `register_channel`: Registers a provider under a channel name (e.g., `"email"`).
- `send`: Validates input, dispatches notification via channel provider. If provider fails, retry up to `max_retries` times. Generates a unique `notification_id` and records history entry. Returns `notification_id`.
- `send_bulk`: Sends the same message to multiple recipients, returning a list of generated notification IDs.
- `get_history`: If `notification_id` is given, returns single history dict. If `None`, returns list of all notification history records.

## 6. Validation Rules
- Sending to an unregistered channel name raises `KeyError` or `ValueError`.
- Empty `recipient` or empty `message` string raises `ValueError`.
- Querying `get_history` with a non-existent `notification_id` raises `KeyError`.

## 7. Edge Cases
- All retries failing (status becomes `"FAILED"` in history).
- Bulk sending with an empty list of recipients.
- Provider throwing an unhandled exception during send (engine should catch it and handle retries).

## 8. Examples
```python
engine = NotificationEngine(max_retries=3)
engine.register_channel("email", EmailProvider())
nid = engine.send("email", "alice@example.com", "Your order has shipped!")
print(engine.get_history(nid)["status"]) # "SENT"
```

## 9. Constraints
- DO NOT send real emails/SMS. Use the simulated providers provided in `solution.py`.

## 10. Left for Developer Decision
- ID generation mechanism (UUID string vs sequential string).
- History record dictionary structure (must include `notification_id`, `channel`, `recipient`, `message`, `status`, `retries_attempted`, `timestamp`).
