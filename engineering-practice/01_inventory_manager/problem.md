# Problem 01: Inventory Manager

## 1. Scenario
You are developing an in-memory inventory management component for a retail store. The system tracks products, manages stock levels during additions and purchases, monitors low-stock alerts, and generates business inventory reports.

## 2. Goal
Design and implement the `InventoryManager` class to encapsulate product records, enforce business integrity rules, handle stock updates safely, and compute aggregate metrics.

## 3. Required Classes
- `InventoryManager`

## 4. Required Methods
- `add_product(product_id: str, name: str, price: float, quantity: int) -> None`
- `remove_product(product_id: str) -> None`
- `add_stock(product_id: str, quantity: int) -> None`
- `remove_stock(product_id: str, quantity: int) -> None`
- `get_product(product_id: str) -> dict`
- `get_low_stock_products(threshold: int) -> list[dict]`
- `get_inventory_value() -> float`
- `generate_report() -> dict`

## 5. Behavior
- `add_product`: Registers a new product. Each product has a unique string ID, a descriptive name, a non-negative price, and a non-negative initial quantity.
- `remove_product`: Deletes a product from the inventory completely.
- `add_stock`: Increases the stored quantity of an existing product by a positive integer.
- `remove_stock`: Decreases the stored quantity of an existing product by a positive integer, provided sufficient stock is available.
- `get_product`: Retrieves a structured dictionary representing the product details (`product_id`, `name`, `price`, `quantity`).
- `get_low_stock_products`: Returns a list of product dictionaries whose quantity is less than or equal to `threshold`.
- `get_inventory_value`: Calculates the total valuation of all stock currently in inventory ($\sum 	ext{price} 	imes 	ext{quantity}$).
- `generate_report`: Generates summary statistics including total distinct products, total aggregate quantity of items, total inventory monetary value, and count of low-stock items.

## 6. Validation Rules
- `product_id` must be unique. Attempting to add a product with an existing `product_id` must raise a `ValueError` or `KeyError`.
- `price` cannot be negative. If `price < 0`, raise a `ValueError`.
- `quantity` cannot be negative. If initial or added/removed quantity is invalid, raise a `ValueError`.
- `add_stock` and `remove_stock` require `quantity > 0`. If `quantity <= 0`, raise a `ValueError`.
- If `remove_stock` requests more items than available, raise a `ValueError`.
- Accessing or modifying a non-existent `product_id` must raise a `KeyError`.

## 7. Edge Cases
- Adding stock to a product that was removed.
- Removing stock down to exactly 0 (allowed).
- Threshold set to 0 in `get_low_stock_products` (matches items with 0 stock).
- Calculating inventory value when the inventory is empty (should return 0.0).

## 8. Examples
```python
manager = InventoryManager()
manager.add_product("P101", "Wireless Mouse", 29.99, 15)
manager.add_stock("P101", 5) # quantity is now 20
manager.remove_stock("P101", 2) # quantity is now 18
print(manager.get_inventory_value()) # 539.82
```

## 9. Constraints
- Must run in standard Python 3.10+ without external libraries.
- All state must be managed in memory.

## 10. Left for Developer Decision
- Internal data structure used to index products (e.g., dictionary mapping ID to object or dict).
- Data model for representing a single product internally (class vs dictionary).
