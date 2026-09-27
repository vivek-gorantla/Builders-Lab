from typing import Optional, List, Dict, Any

class User:
    """User entity model."""
    def __init__(self, user_id: str, name: str, email: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email

    def to_dict(self) -> Dict[str, Any]:
        return {"user_id": self.user_id, "name": self.name, "email": self.email}

class Task:
    """Task entity model."""
    def __init__(self, task_id: str, owner_id: str, title: str, description: str = "", status: str = "PENDING", created_at: Optional[float] = None, updated_at: Optional[float] = None) -> None:
        self.task_id = task_id
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "owner_id": self.owner_id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

class UserService:
    """User management service layer."""

    def __init__(self) -> None:
        raise NotImplementedError("Implement UserService.__init__")

    def register_user(self, name: str, email: str) -> Dict[str, Any]:
        raise NotImplementedError("Implement register_user")

    def get_user(self, user_id: str) -> Dict[str, Any]:
        raise NotImplementedError("Implement get_user")

class TaskService:
    """Task management service layer with ownership permissions and pagination."""

    def __init__(self, user_service: UserService) -> None:
        raise NotImplementedError("Implement TaskService.__init__")

    def create_task(self, owner_id: str, title: str, description: str = "") -> Dict[str, Any]:
        raise NotImplementedError("Implement create_task")

    def update_task(self, task_id: str, requester_id: str, title: Optional[str] = None, description: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
        raise NotImplementedError("Implement update_task")

    def delete_task(self, task_id: str, requester_id: str) -> bool:
        raise NotImplementedError("Implement delete_task")

    def mark_completed(self, task_id: str, requester_id: str) -> Dict[str, Any]:
        raise NotImplementedError("Implement mark_completed")

    def list_tasks(self, requester_id: Optional[str] = None, owner_id: Optional[str] = None, status: Optional[str] = None, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        raise NotImplementedError("Implement list_tasks")
