import sys
import os

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']
import sys
import os
import time
import pytest


from solution import MessageBroker

def test_subscribe_and_publish_sync():
    broker = MessageBroker()
    received = []

    def sub_a(msg):
        received.append(f"A:{msg}")

    def sub_b(msg):
        received.append(f"B:{msg}")

    broker.subscribe("orders", sub_a)
    broker.subscribe("orders", sub_b)

    broker.publish("orders", "order_101")
    assert "A:order_101" in received
    assert "B:order_101" in received
    assert broker.get_subscriber_count("orders") == 2

def test_unsubscribe():
    broker = MessageBroker()
    received = []

    def sub_a(msg):
        received.append(msg)

    broker.subscribe("news", sub_a)
    assert broker.unsubscribe("news", sub_a) is True
    assert broker.unsubscribe("news", sub_a) is False

    broker.publish("news", "headline")
    assert len(received) == 0
    assert broker.get_subscriber_count("news") == 0

def test_publish_to_topic_without_subscribers():
    broker = MessageBroker()
    # Should not raise any error
    broker.publish("empty_topic", "hello")
    assert broker.get_subscriber_count("empty_topic") == 0

def test_subscriber_exception_isolation():
    broker = MessageBroker()
    received = []

    def failing_sub(msg):
        raise RuntimeError("Subscriber crashed!")

    def working_sub(msg):
        received.append(msg)

    broker.subscribe("alerts", failing_sub)
    broker.subscribe("alerts", working_sub)

    # Publishing should catch failing_sub exception and still run working_sub
    broker.publish("alerts", "critical_event")
    assert received == ["critical_event"]

def test_publish_async_mode():
    broker = MessageBroker()
    received = []

    def slow_sub(msg):
        time.sleep(0.05)
        received.append(msg)

    broker.subscribe("async_topic", slow_sub)
    broker.publish("async_topic", "async_msg", async_mode=True)

    # Non-blocking check right after publish
    time.sleep(0.1)
    assert received == ["async_msg"]