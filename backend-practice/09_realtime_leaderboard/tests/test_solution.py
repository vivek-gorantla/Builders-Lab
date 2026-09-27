import sys
import os
import sqlite3
import pytest

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']

from solution import LeaderboardService

@pytest.fixture
def db_conn():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()

def test_submit_score_and_rank(db_conn):
    lb = LeaderboardService(db_conn)
    lb.submit_score("player1", score_delta=100, is_win=True, country="US")
    lb.submit_score("player2", score_delta=250, is_win=True, country="US")
    lb.submit_score("player3", score_delta=50, is_win=False, country="CA")

    p2_rank = lb.get_player_rank("player2")
    assert p2_rank["rank"] == 1
    assert p2_rank["total_score"] == 250

    p1_rank = lb.get_player_rank("player1")
    assert p1_rank["rank"] == 2

def test_win_streak_tracking(db_conn):
    lb = LeaderboardService(db_conn)
    lb.submit_score("pro_gamer", 10, is_win=True)
    lb.submit_score("pro_gamer", 10, is_win=True)
    lb.submit_score("pro_gamer", 10, is_win=True)
    assert lb.get_player_streak("pro_gamer") == 3

    # Loss resets current win streak to 0
    lb.submit_score("pro_gamer", -5, is_win=False)
    assert lb.get_player_streak("pro_gamer") == 0

def test_country_filtered_leaderboard(db_conn):
    lb = LeaderboardService(db_conn)
    lb.submit_score("p_us", 500, is_win=True, country="US")
    lb.submit_score("p_jp", 900, is_win=True, country="JP")

    jp_lb = lb.get_top_leaderboard(limit=5, country="JP")
    assert len(jp_lb) == 1
    assert jp_lb[0]["player_id"] == "p_jp"
