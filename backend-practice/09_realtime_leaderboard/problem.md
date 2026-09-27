# Problem 09: Gaming Leaderboard & Stats Engine

## 1. Scenario
Online gaming servers maintain global and country-filtered leaderboards, computing player rankings, total scores, and win streaks.

## 2. Goal
Build `LeaderboardService` backed by database queries (SQLite or PostgreSQL / SQL DB).

## 3. Required Class
- `LeaderboardService`

## 4. Required Methods
- `submit_score(player_id: str, score_delta: int, is_win: bool, country: str = "US") -> dict`
- `get_player_rank(player_id: str) -> dict`
- `get_top_leaderboard(limit: int = 10, country: Optional[str] = None) -> list[dict]`
- `get_player_streak(player_id: str) -> int`

## 5. Behavior
- `submit_score`: Updates or inserts player score record. Adds `score_delta` to `total_score`. If `is_win=True`, increments `current_streak`. If `is_win=False`, resets `current_streak` to 0.
- `get_player_rank`: Computes 1-based rank position of `player_id` based on total score descending (rank = $1 + 	ext{count of players with score} > 	ext{player score}$).
- `get_top_leaderboard`: Returns top `limit` players sorted by `total_score` descending. If `country` is specified, filter by country.

## 6. Validation Rules
- Querying non-existent `player_id` raises `KeyError`.

## 7. Edge Cases
- Tie score handling (same total score assigns same rank or breaks ties alphabetically).

## 8. Examples
```python
lb = LeaderboardService()
lb.submit_score("p1", 100, True)
print(lb.get_player_rank("p1")["rank"]) # 1
```

## 9. Constraints
- SQLite / PostgreSQL DB connection compatibility.

## 10. Left for Developer Decision
- SQL window function `RANK()` vs query aggregation.
