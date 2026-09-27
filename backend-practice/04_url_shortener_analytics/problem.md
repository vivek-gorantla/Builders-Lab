# Problem 04: URL Shortener & Analytics Service

## 1. Scenario
URL Shorteners (like Bitly or TinyURL) map long target URLs to short Base62 slugs, enforce expiration deadlines, track detailed click analytics (IP address, user agent, timestamp), and persist state in SQL / PostgreSQL databases.

## 2. Goal
Build `URLShortenerService` supporting database persistence (SQLite or PostgreSQL / SQL DB connection).

## 3. Required Class
- `URLShortenerService`

## 4. Required Methods
- `__init__(db_connection_or_url: Optional[Any] = None)`
- `shorten_url(original_url: str, custom_slug: Optional[str] = None, ttl_seconds: Optional[float] = None) -> dict`
- `resolve_url(slug: str, user_ip: Optional[str] = None, user_agent: Optional[str] = None) -> str`
- `get_analytics(slug: str) -> dict`

## 5. Behavior
- Database Compatibility: Creates `urls` and `clicks` tables in SQLite / PostgreSQL connection.
- `shorten_url`: Generates unique Base62 slug (or uses `custom_slug`). Stores `original_url`, `slug`, `created_at`, `expires_at`.
- `resolve_url`: Looks up `slug`. If expired or missing, raises `KeyError` / `ValueError`. Otherwise, records click event record (`slug`, `user_ip`, `user_agent`, `timestamp`) and returns `original_url`.
- `get_analytics`: Returns `{"slug": ..., "original_url": ..., "total_clicks": int, "clicks": [click_log_dicts]}`.

## 6. Validation Rules
- Invalid URL format (must start with `http://` or `https://`) raises `ValueError`.
- Duplicate `custom_slug` raises `ValueError`.

## 7. Edge Cases
- Resolving an expired slug (behaves as 404 / raises exception).

## 8. Examples
```python
svc = URLShortenerService()
res = svc.shorten_url("https://google.com", custom_slug="g")
url = svc.resolve_url("g") # "https://google.com"
```

## 9. Constraints
- Python standard library (`sqlite3`, `hashlib`, `time`). Easily configurable to PostgreSQL connection strings.

## 10. Left for Developer Decision
- Base62 encoding algorithm implementation.
