from typing import Dict, List, Any, Optional

class InventoryManager:
    """Inventory management system for tracking store products, stock levels, and reports."""

    def __init__(self) -> None:
        self._products: Dict[str, Dict[str, Any]] = {}

    def add_product(self, product_id: str, name: str, price: float, quantity: int) -> None:
        if not isinstance(product_id, str) or not product_id:
            raise ValueError("Product ID must be a non-empty string.")
        if product_id in self._products:
            raise ValueError(f"Product ID '{product_id}' already exists.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must be a non-empty string.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self._products[product_id] = {
            "product_id": product_id,
            "name": name.strip(),
            "price": float(price),
            "quantity": int(quantity),
        }

    def remove_product(self, product_id: str) -> None:
        if product_id not in self._products:
            raise KeyError(f"Product ID '{product_id}' not found.")
        del self._products[product_id]

    def add_stock(self, product_id: str, quantity: int) -> None:
        if product_id not in self._products:
            raise KeyError(f"Product ID '{product_id}' not found.")
        if quantity <= 0:
            raise ValueError("Stock addition quantity must be positive.")
        self._products[product_id]["quantity"] += int(quantity)

    def remove_stock(self, product_id: str, quantity: int) -> None:
        if product_id not in self._products:
            raise KeyError(f"Product ID '{product_id}' not found.")
        if quantity <= 0:
            raise ValueError("Stock removal quantity must be positive.")
        if quantity > self._products[product_id]["quantity"]:
            raise ValueError(
                f"Insufficient stock for product '{product_id}'. Available: {self._products[product_id]['quantity']}, Requested: {quantity}."
            )
        self._products[product_id]["quantity"] -= int(quantity)

    def get_product(self, product_id: str) -> Dict[str, Any]:
        if product_id not in self._products:
            raise KeyError(f"Product ID '{product_id}' not found.")
        return dict(self._products[product_id])

    def get_low_stock_products(self, threshold: int) -> List[Dict[str, Any]]:
        return [
            dict(prod)
            for prod in self._products.values()
            if prod["quantity"] <= threshold
        ]

    def get_inventory_value(self) -> float:
        return sum(prod["price"] * prod["quantity"] for prod in self._products.values())

    def generate_report(self) -> Dict[str, Any]:
        total_products = len(self._products)
        total_quantity = sum(prod["quantity"] for prod in self._products.values())
        total_value = self.get_inventory_value()
        return {
            "total_products": total_products,
            "total_quantity": total_quantity,
            "total_value": total_value,
        }

