import sys
import os
import sqlite3
import pytest

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']

from solution import OrderInventoryService

@pytest.fixture
def db_conn():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()

def test_create_order_reserves_stock(db_conn):
    svc = OrderInventoryService(db_conn)
    svc.add_product_stock("p100", "Smartphone", 799.0, 10)

    order = svc.create_order("u1", {"p100": 2})
    assert order["status"] == "PENDING"
    assert order["total_amount"] == 1598.0

def test_overselling_stock_raises_error(db_conn):
    svc = OrderInventoryService(db_conn)
    svc.add_product_stock("p200", "Laptop", 1200.0, 1)

    # Ordering more than available stock must fail
    with pytest.raises(ValueError):
        svc.create_order("u1", {"p200": 5})

def test_pay_order_completes_purchase(db_conn):
    svc = OrderInventoryService(db_conn)
    svc.add_product_stock("p1", "Item 1", 10.0, 5)

    order = svc.create_order("u1", {"p1": 2})
    paid_order = svc.pay_order(order["order_id"])
    assert paid_order["status"] == "PAID"

def test_cancel_order_releases_stock(db_conn):
    svc = OrderInventoryService(db_conn)
    svc.add_product_stock("p1", "Item 1", 10.0, 5)

    order = svc.create_order("u1", {"p1": 3})
    svc.cancel_order(order["order_id"])
    
    # Stock should be released back to inventory
    # Ordering 5 items now succeeds
    order2 = svc.create_order("u2", {"p1": 5})
    assert order2["status"] == "PENDING"
