# Problem 07: OAuth2 / JWT Auth & Session Service

## 1. Scenario
Production user authentication backends store salted password hashes in relational databases (PostgreSQL/MySQL), issue JWT access and refresh tokens, and manage token revocation / blacklisting.

## 2. Goal
Implement `AuthSessionService` with database persistence (SQLite or PostgreSQL / SQL DB).

## 3. Required Class
- `AuthSessionService`

## 4. Required Methods
- `register_user(email: str, password: str, name: str) -> dict`
- `login(email: str, password: str) -> dict`
- `refresh_access_token(refresh_token: str) -> dict`
- `logout(access_token: str) -> bool`
- `verify_session(access_token: str) -> dict`

## 5. Behavior
- Password Security: Hashes passwords with salt using `hashlib.pbkdf2_hmac` before storing in DB `users` table.
- `login`: Validates credentials and returns `{"access_token": str, "refresh_token": str}`.
- Token Blacklisting: `logout` persists revoked token signature in DB `token_blacklist` table.
- `verify_session`: Decodes JWT access token, checks signature against `secret_key`, verifies token is not in `token_blacklist`, and returns user payload `{"user_id": ..., "email": ..., "name": ...}`.

## 6. Validation Rules
- Invalid email format or empty password raises `ValueError`.
- Revoked or expired access tokens raise `ValueError`.

## 7. Edge Cases
- Login with incorrect password raises `ValueError`.

## 8. Examples
```python
auth = AuthSessionService()
auth.register_user("a@b.com", "pass", "Alice")
tokens = auth.login("a@b.com", "pass")
```

## 9. Constraints
- Python standard library (`hashlib`, `hmac`, `sqlite3`, `json`, `time`).

## 10. Left for Developer Decision
- JWT encoding structure (header.payload.signature).
