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


from solution import InventoryManager

def test_add_and_get_product():
    inv = InventoryManager()
    inv.add_product("P100", "Laptop", 999.99, 10)
    prod = inv.get_product("P100")
    assert prod["product_id"] == "P100"
    assert prod["name"] == "Laptop"
    assert prod["price"] == 999.99
    assert prod["quantity"] == 10

def test_add_duplicate_product_raises_error():
    inv = InventoryManager()
    inv.add_product("P100", "Laptop", 999.99, 10)
    with pytest.raises((ValueError, KeyError)):
        inv.add_product("P100", "Laptop Duplicate", 899.99, 5)

def test_invalid_price_or_quantity():
    inv = InventoryManager()
    with pytest.raises(ValueError):
        inv.add_product("P101", "Negative Price", -10.0, 5)
    with pytest.raises(ValueError):
        inv.add_product("P102", "Negative Qty", 10.0, -5)

def test_remove_product():
    inv = InventoryManager()
    inv.add_product("P100", "Laptop", 999.99, 10)
    inv.remove_product("P100")
    with pytest.raises(KeyError):
        inv.get_product("P100")

def test_remove_nonexistent_product_raises_error():
    inv = InventoryManager()
    with pytest.raises(KeyError):
        inv.remove_product("NONEXISTENT")

def test_add_and_remove_stock():
    inv = InventoryManager()
    inv.add_product("P100", "Mouse", 25.0, 5)
    inv.add_stock("P100", 10)
    assert inv.get_product("P100")["quantity"] == 15
    inv.remove_stock("P100", 7)
    assert inv.get_product("P100")["quantity"] == 8

def test_remove_stock_insufficient_or_invalid():
    inv = InventoryManager()
    inv.add_product("P100", "Keyboard", 45.0, 3)
    with pytest.raises(ValueError):
        inv.remove_stock("P100", 5)
    with pytest.raises(ValueError):
        inv.remove_stock("P100", 0)
    with pytest.raises(ValueError):
        inv.add_stock("P100", -2)

def test_get_low_stock_products():
    inv = InventoryManager()
    inv.add_product("P1", "Item 1", 10.0, 2)
    inv.add_product("P2", "Item 2", 20.0, 15)
    inv.add_product("P3", "Item 3", 30.0, 5)
    low_stock = inv.get_low_stock_products(threshold=5)
    ids = [p["product_id"] for p in low_stock]
    assert "P1" in ids
    assert "P3" in ids
    assert "P2" not in ids

def test_get_inventory_value():
    inv = InventoryManager()
    inv.add_product("P1", "Item 1", 10.0, 2)
    inv.add_product("P2", "Item 2", 20.0, 3)
    assert inv.get_inventory_value() == 80.0

def test_generate_report():
    inv = InventoryManager()
    inv.add_product("P1", "Item 1", 10.0, 2)
    inv.add_product("P2", "Item 2", 20.0, 10)
    report = inv.generate_report()
    assert report["total_products"] == 2
    assert report["total_quantity"] == 12
    assert report["total_value"] == 220.0