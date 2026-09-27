# Problem 05: Fintech Double-Entry Payment Ledger

## 1. Scenario
Financial applications (Stripe, PayPal, Banks) track money movements using double-entry accounting. Money cannot be created or destroyed: every debit entry must be balanced by a credit entry ($\sum 	ext{debits} = \sum 	ext{credits}$).

## 2. Goal
Build `PaymentLedgerService` implementing double-entry transaction accounting with SQL/Postgres database persistence.

## 3. Required Class
- `PaymentLedgerService`

## 4. Required Methods
- `create_account(account_id: str, currency: str = "USD") -> dict`
- `deposit(account_id: str, amount: float, reference: str) -> dict`
- `transfer(source_account_id: str, target_account_id: str, amount: float, reference: str) -> dict`
- `get_balance(account_id: str) -> float`
- `get_account_statement(account_id: str) -> list[dict]`
- `verify_ledger_integrity() -> bool`

## 5. Behavior
- `deposit`: Credits target account from a system clearing account.
- `transfer`: Atomically creates a debit entry for `source_account_id` and a credit entry for `target_account_id` with amount $X$.
- `get_balance`: Calculates current balance by summing credits minus debits for `account_id`.
- `verify_ledger_integrity`: Asserts that global sum of all debit entries equals global sum of all credit entries across the entire ledger. Returns `True` if balanced.

## 6. Validation Rules
- Transfer amount $\le 0$ raises `ValueError`.
- Insufficient balance on `source_account_id` raises `ValueError`.
- Duplicate transaction `reference` string raises `ValueError` (idempotent reference lock).

## 7. Edge Cases
- Transferring between non-existent accounts raises `KeyError`.

## 8. Examples
```python
ledger = PaymentLedgerService()
ledger.create_account("acc1")
ledger.deposit("acc1", 100.0, "dep_1")
print(ledger.get_balance("acc1")) # 100.0
```

## 9. Constraints
- SQLite / PostgreSQL DB connection compatibility.

## 10. Left for Developer Decision
- Ledger entry schema design (`entries` table with `entry_id`, `account_id`, `entry_type`, `amount`, `reference`, `created_at`).
