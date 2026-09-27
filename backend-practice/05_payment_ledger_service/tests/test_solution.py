import sys
import os
import sqlite3
import pytest

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']

from solution import PaymentLedgerService

@pytest.fixture
def db_conn():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()

def test_deposit_and_balance(db_conn):
    ledger = PaymentLedgerService(db_conn)
    ledger.create_account("user_wallet", "USD")
    
    ledger.deposit("user_wallet", 500.0, reference="dep_001")
    assert ledger.get_balance("user_wallet") == 500.0

def test_atomic_transfer_between_accounts(db_conn):
    ledger = PaymentLedgerService(db_conn)
    ledger.create_account("alice", "USD")
    ledger.create_account("bob", "USD")

    ledger.deposit("alice", 200.0, reference="init_alice")
    ledger.transfer("alice", "bob", 75.0, reference="tx_001")

    assert ledger.get_balance("alice") == 125.0
    assert ledger.get_balance("bob") == 75.0
    assert ledger.verify_ledger_integrity() is True

def test_insufficient_funds_rejection(db_conn):
    ledger = PaymentLedgerService(db_conn)
    ledger.create_account("user1", "USD")
    ledger.create_account("user2", "USD")
    ledger.deposit("user1", 50.0, "init")

    with pytest.raises(ValueError):
        ledger.transfer("user1", "user2", 100.0, "failed_tx")

def test_duplicate_transfer_reference_rejection(db_conn):
    ledger = PaymentLedgerService(db_conn)
    ledger.create_account("a", "USD")
    ledger.create_account("b", "USD")
    ledger.deposit("a", 100.0, "init")

    ledger.transfer("a", "b", 30.0, reference="unique_ref_1")
    with pytest.raises(ValueError):
        ledger.transfer("a", "b", 30.0, reference="unique_ref_1")
