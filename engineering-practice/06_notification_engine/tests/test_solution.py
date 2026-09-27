import sys
import os

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']
import sys
import os
import pytest


from solution import (
    NotificationEngine,
    EmailProvider,
    SmsProvider,
    PushProvider
)

def test_register_and_send_success():
    engine = NotificationEngine()
    engine.register_channel("email", EmailProvider())

    notif_id = engine.send("email", "user@example.com", "Welcome!")
    assert isinstance(notif_id, str) and len(notif_id) > 0

    history = engine.get_history(notif_id)
    assert history["status"] == "SENT"
    assert history["recipient"] == "user@example.com"

def test_unregistered_channel_raises_error():
    engine = NotificationEngine()
    with pytest.raises((KeyError, ValueError)):
        engine.send("sms", "+1234567890", "Test")

def test_empty_recipient_or_message_validation():
    engine = NotificationEngine()
    engine.register_channel("sms", SmsProvider())
    with pytest.raises(ValueError):
        engine.send("sms", "", "Valid message")
    with pytest.raises(ValueError):
        engine.send("sms", "+1234567890", "")

def test_retry_failed_notification():
    engine = NotificationEngine(max_retries=2)
    failing_provider = EmailProvider(should_fail=True)
    engine.register_channel("email", failing_provider)

    notif_id = engine.send("email", "user@example.com", "Fail Test")
    history = engine.get_history(notif_id)
    assert history["status"] == "FAILED"
    assert history["retries_attempted"] == 2

def test_send_bulk():
    engine = NotificationEngine()
    engine.register_channel("push", PushProvider())

    recipients = ["device1", "device2", "device3"]
    ids = engine.send_bulk("push", recipients, "Broadcast alert")
    assert len(ids) == 3
    history_all = engine.get_history()
    assert len(history_all) == 3

def test_unknown_history_id_raises_key_error():
    engine = NotificationEngine()
    with pytest.raises(KeyError):
        engine.get_history("invalid_id_999")