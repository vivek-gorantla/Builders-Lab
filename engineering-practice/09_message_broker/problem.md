# Problem 09: Message Broker

## 1. Scenario
Event-driven microservice architectures rely on publish/subscribe message brokers (like RabbitMQ or Apache Kafka) to decouple message producers from consumers. You need to build an in-memory publish/subscribe message broker supporting topic subscriptions, callback isolation, and optional asynchronous dispatch.

## 2. Goal
Implement the `MessageBroker` class using the Observer Pattern.

## 3. Required Classes
- `MessageBroker`

## 4. Required Methods
- `subscribe(topic: str, callback: Callable[[Any], None]) -> None`
- `unsubscribe(topic: str, callback: Callable[[Any], None]) -> bool`
- `publish(topic: str, message: Any, async_mode: bool = False) -> None`
- `get_subscriber_count(topic: str) -> int`

## 5. Behavior
- `subscribe`: Registers a subscriber callback function for a specific string `topic`.
- `unsubscribe`: Removes a callback from a `topic`. Returns `True` if removed, `False` if callback was not subscribed.
- `publish`: Delivers `message` to all registered callbacks on `topic`.
  - If `async_mode=False`, invoke callbacks synchronously in caller thread.
  - If `async_mode=True`, dispatch callback executions asynchronously (e.g. using worker threads).
- `get_subscriber_count`: Returns total active subscribers for `topic`.

## 6. Validation Rules
- Error Isolation: If one subscriber callback raises an unhandled exception, the broker MUST catch it, suppress/log it, and continue executing all remaining subscribers for that topic.
- Publishing to a topic with 0 subscribers must be safe and complete without error.

## 7. Edge Cases
- Duplicate subscriptions of the same function to the same topic.
- Unsubscribing from a topic that does not exist.
- Non-string topic names or None callbacks (raise `ValueError`).

## 8. Examples
```python
broker = MessageBroker()
broker.subscribe("payments", lambda msg: print("Payment received:", msg))
broker.publish("payments", {"amount": 50, "currency": "USD"})
```

## 9. Constraints
- Pure Python standard library (`threading`, `concurrent.futures`, etc.).

## 10. Left for Developer Decision
- Data structure mapping topics to callback subscribers.
- Thread management for `async_mode=True` (e.g. `threading.Thread` vs `ThreadPoolExecutor`).
