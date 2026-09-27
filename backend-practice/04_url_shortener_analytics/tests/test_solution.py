import sys
import os
import sqlite3
import pytest

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']

from solution import URLShortenerService

@pytest.fixture
def db_conn():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()

def test_shorten_and_resolve_url(db_conn):
    svc = URLShortenerService(db_conn)
    res = svc.shorten_url("https://github.com/openai/gpt-3")
    assert "slug" in res
    slug = res["slug"]

    resolved = svc.resolve_url(slug, user_ip="192.168.1.1")
    assert resolved == "https://github.com/openai/gpt-3"

def test_custom_slug_and_duplicate_rejection(db_conn):
    svc = URLShortenerService(db_conn)
    res = svc.shorten_url("https://python.org", custom_slug="python-home")
    assert res["slug"] == "python-home"

    # Duplicate custom slug must be rejected
    with pytest.raises(ValueError):
        svc.shorten_url("https://other.org", custom_slug="python-home")

def test_click_analytics_tracking(db_conn):
    svc = URLShortenerService(db_conn)
    res = svc.shorten_url("https://news.ycombinator.com")
    slug = res["slug"]

    svc.resolve_url(slug, user_ip="10.0.0.1")
    svc.resolve_url(slug, user_ip="10.0.0.2")

    stats = svc.get_analytics(slug)
    assert stats["total_clicks"] == 2
    assert "clicks" in stats and len(stats["clicks"]) == 2

def test_invalid_url_validation(db_conn):
    svc = URLShortenerService(db_conn)
    with pytest.raises(ValueError):
        svc.shorten_url("not_a_valid_url")
