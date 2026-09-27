# 06 - E-Commerce Order & Inventory Locking Service

## What You Are Building
An e-commerce order checkout engine managing atomic inventory stock reservations, overselling prevention, and order status state transitions.

## What You Will Learn
- Race condition & overselling prevention
- Database transaction locking strategies
- Order lifecycle state machine (`PENDING`, `PAID`, `CANCELLED`)

## Testing
```bash
python -m pytest
```
