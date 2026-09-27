import sys
import os
import sqlite3
import pytest

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']

from solution import AuthSessionService

@pytest.fixture
def db_conn():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()

def test_user_registration_and_login(db_conn):
    auth = AuthSessionService(db_conn)
    reg = auth.register_user("dev@example.com", "Password123!", "Developer")
    assert "user_id" in reg

    tokens = auth.login("dev@example.com", "Password123!")
    assert "access_token" in tokens
    assert "refresh_token" in tokens

def test_verify_session_and_logout(db_conn):
    auth = AuthSessionService(db_conn)
    auth.register_user("user@example.com", "secret", "User")
    tokens = auth.login("user@example.com", "secret")

    session = auth.verify_session(tokens["access_token"])
    assert session["email"] == "user@example.com"

    # Logout blacklists access token
    assert auth.logout(tokens["access_token"]) is True
    
    # Subsequent verification must raise ValueError
    with pytest.raises(ValueError):
        auth.verify_session(tokens["access_token"])

def test_refresh_token_issues_new_access_token(db_conn):
    auth = AuthSessionService(db_conn)
    auth.register_user("user2@example.com", "secret", "User2")
    tokens = auth.login("user2@example.com", "secret")

    new_tokens = auth.refresh_access_token(tokens["refresh_token"])
    assert "access_token" in new_tokens
    assert new_tokens["access_token"] != tokens["access_token"]

def test_duplicate_email_registration_fails(db_conn):
    auth = AuthSessionService(db_conn)
    auth.register_user("test@example.com", "p1", "Name")
    with pytest.raises(ValueError):
        auth.register_user("test@example.com", "p2", "Name2")
