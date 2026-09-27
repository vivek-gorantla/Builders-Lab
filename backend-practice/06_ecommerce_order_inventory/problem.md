# Problem 06: E-Commerce Order & Inventory Locking Service

## 1. Scenario
E-commerce checkout platforms (Shopify, Amazon) lock inventory when an order is created to prevent overselling, and release stock back to inventory if the order is cancelled or times out.

## 2. Goal
Implement `OrderInventoryService` supporting atomic inventory reservations and order state machine (`PENDING` $ightarrow$ `PAID` / `CANCELLED`).

## 3. Required Class
- `OrderInventoryService`

## 4. Required Methods
- `add_product_stock(product_id: str, title: str, price: float, initial_stock: int) -> dict`
- `create_order(user_id: str, items: dict[str, int]) -> dict`
- `pay_order(order_id: str) -> dict`
- `cancel_order(order_id: str) -> dict`
- `get_order(order_id: str) -> dict`

## 5. Behavior
- `create_order`: Accepts `items` dict mapping `product_id` to requested quantity. Within a database transaction, verifies all products have sufficient stock, decrements stock levels, calculates `total_amount`, sets status to `"PENDING"`, and returns order payload.
- `pay_order`: Transitions status from `"PENDING"` to `"PAID"`.
- `cancel_order`: If status is `"PENDING"`, releases reserved item quantities back to product stock levels and sets status to `"CANCELLED"`.

## 6. Validation Rules
- Insufficient stock for any item in `create_order` rolls back the transaction and raises `ValueError`.
- Paying or cancelling an already cancelled/paid order raises `ValueError`.

## 7. Edge Cases
- Ordering 0 items or requesting non-existent products raises `ValueError`.

## 8. Examples
```python
svc = OrderInventoryService()
svc.add_product_stock("P1", "Watch", 100.0, 5)
ord = svc.create_order("u1", {"P1": 2}) # stock becomes 3
svc.cancel_order(ord["order_id"]) # stock restored to 5
```

## 9. Constraints
- SQLite / PostgreSQL DB connection compatibility.

## 10. Left for Developer Decision
- Database table schemas (`products`, `orders`, `order_items`).
