# Problem 10: Mini Backend

## 1. Scenario
Backend services organize business logic into decoupled domain service layers (e.g., UserService, TaskService). You need to build an in-memory backend service layer for a multi-user task management application, incorporating entity validation, authorization ownership checks, status workflows, and paginated queries.

## 2. Goal
Implement `UserService` and `TaskService` in a clean service-oriented architecture.

## 3. Required Classes
- `User` (Data Model)
- `Task` (Data Model)
- `UserService`
- `TaskService`

## 4. Required Methods
### `UserService`
- `register_user(name: str, email: str) -> dict`
- `get_user(user_id: str) -> dict`

### `TaskService`
- `__init__(user_service: UserService)`
- `create_task(owner_id: str, title: str, description: str = "") -> dict`
- `update_task(task_id: str, requester_id: str, title: Optional[str] = None, description: Optional[str] = None, status: Optional[str] = None) -> dict`
- `delete_task(task_id: str, requester_id: str) -> bool`
- `mark_completed(task_id: str, requester_id: str) -> dict`
- `list_tasks(requester_id: Optional[str] = None, owner_id: Optional[str] = None, status: Optional[str] = None, page: int = 1, page_size: int = 10) -> dict`

## 5. Behavior
- `register_user`: Validates name and email format. Auto-generates unique `user_id`. Returns user dictionary representation.
- `create_task`: Validates `owner_id` exists in `user_service` and `title` is non-empty. Auto-generates unique `task_id`, sets status to `"PENDING"`, and records timestamps (`created_at`, `updated_at`).
- `update_task`: Enforces authorization check (`requester_id == task.owner_id`). Raises `PermissionError` if unauthorized. Updates provided fields and updates `updated_at`.
- `delete_task`: Enforces authorization check. Removes task. Returns `True`.
- `mark_completed`: Shortcut for updating task status to `"COMPLETED"` with owner authorization check.
- `list_tasks`: Returns dictionary with paginated task items:
  `{"items": list[dict], "total": int, "page": int, "page_size": int, "total_pages": int}`
  Supports optional filtering by `owner_id` and `status`.

## 6. Validation Rules
- Non-empty name and valid email (must contain `'@'`) required for `register_user`.
- Task title cannot be empty or whitespace.
- Task status must be one of `"PENDING"`, `"IN_PROGRESS"`, `"COMPLETED"`.
- Modifying or deleting tasks owned by another user raises `PermissionError`.
- Unknown user or task ID raises `KeyError` or `ValueError`.

## 7. Edge Cases
- Pagination out of range (returns empty items list).
- Filtering tasks by non-existent owner ID.
- Updating task with no changes specified.

## 8. Examples
```python
user_svc = UserService()
task_svc = TaskService(user_svc)

user = user_svc.register_user("Bob", "bob@example.com")
task = task_svc.create_task(user["user_id"], "Write Documentation")
completed = task_svc.mark_completed(task["task_id"], user["user_id"])
```

## 9. Constraints
- Pure Python standard library only.

## 10. Left for Developer Decision
- ID generation mechanism (UUID string vs auto-increment string).
- Timestamp format (float epoch timestamp vs ISO string).
