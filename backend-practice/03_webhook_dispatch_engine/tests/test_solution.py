import sys
import os
import pytest

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']

from solution import WebhookEngine

def test_register_and_dispatch():
    engine = WebhookEngine()
    endpoint_id = engine.register_endpoint("client1", "https://api.client.com/webhooks", "sec_123", ["order.created"])

    event_id = engine.dispatch_event("order.created", {"order_id": 99, "amount": 150.0})
    assert isinstance(event_id, str) and len(event_id) > 0

    logs = engine.get_delivery_logs(event_id)
    assert len(logs) == 1
    assert logs[0]["target_url"] == "https://api.client.com/webhooks"
    assert "signature" in logs[0]

def test_dead_letter_queue_after_max_retries():
    # Simulate delivery failure
    engine = WebhookEngine(max_retries=2)
    engine.register_endpoint("failing_client", "https://failing.url/webhook", "sec_fail", ["user.signup"])

    event_id = engine.dispatch_event("user.signup", {"user_id": 42})
    
    # Process retries until exhausted
    engine.process_pending_deliveries()
    engine.process_pending_deliveries()

    dlq = engine.get_dead_letter_queue()
    # If failing deliveries exhaust max_retries, move to DLQ
