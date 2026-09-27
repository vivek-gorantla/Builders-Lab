import sys
import os

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']
import sys
import os
import pytest


from solution import UserService, TaskService

def test_register_user_and_get_user():
    user_svc = UserService()
    user_data = user_svc.register_user("Alice", "alice@example.com")
    assert "user_id" in user_data
    assert user_data["name"] == "Alice"

    fetched = user_svc.get_user(user_data["user_id"])
    assert fetched["email"] == "alice@example.com"

def test_register_invalid_user():
    user_svc = UserService()
    with pytest.raises(ValueError):
        user_svc.register_user("", "alice@example.com")
    with pytest.raises(ValueError):
        user_svc.register_user("Alice", "invalid_email_format")

def test_create_task_and_permissions():
    user_svc = UserService()
    task_svc = TaskService(user_svc)

    u1 = user_svc.register_user("User 1", "u1@example.com")
    u2 = user_svc.register_user("User 2", "u2@example.com")

    task = task_svc.create_task(u1["user_id"], "Complete Project", "Build local mini backend")
    assert task["status"] == "PENDING"
    assert task["owner_id"] == u1["user_id"]

    # u2 trying to modify u1 task raises PermissionError
    with pytest.raises(PermissionError):
        task_svc.update_task(task["task_id"], requester_id=u2["user_id"], title="Hacked Title")

    # u1 updating task succeeds
    updated = task_svc.update_task(task["task_id"], requester_id=u1["user_id"], status="IN_PROGRESS")
    assert updated["status"] == "IN_PROGRESS"

def test_mark_completed():
    user_svc = UserService()
    task_svc = TaskService(user_svc)

    u1 = user_svc.register_user("User 1", "u1@example.com")
    task = task_svc.create_task(u1["user_id"], "Finish Assignment")
    completed = task_svc.mark_completed(task["task_id"], requester_id=u1["user_id"])
    assert completed["status"] == "COMPLETED"

def test_delete_task():
    user_svc = UserService()
    task_svc = TaskService(user_svc)

    u1 = user_svc.register_user("User 1", "u1@example.com")
    task = task_svc.create_task(u1["user_id"], "Task to delete")

    assert task_svc.delete_task(task["task_id"], requester_id=u1["user_id"]) is True
    with pytest.raises(KeyError):
        task_svc.mark_completed(task["task_id"], requester_id=u1["user_id"])

def test_list_tasks_filtering_and_pagination():
    user_svc = UserService()
    task_svc = TaskService(user_svc)

    u1 = user_svc.register_user("User 1", "u1@example.com")
    for i in range(15):
        task_svc.create_task(u1["user_id"], f"Task {i}")

    res = task_svc.list_tasks(owner_id=u1["user_id"], page=1, page_size=10)
    assert len(res["items"]) == 10
    assert res["total"] == 15
    assert res["total_pages"] == 2
    assert res["page"] == 1

    res_p2 = task_svc.list_tasks(owner_id=u1["user_id"], page=2, page_size=10)
    assert len(res_p2["items"]) == 5