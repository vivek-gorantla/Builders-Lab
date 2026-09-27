from typing import Dict, Any, Optional

class AuthSessionService:
    """OAuth2/JWT User authentication and session management service with database persistence."""

    def __init__(self, db_connection: Optional[Any] = None, secret_key: str = "jwt_secret_key") -> None:
        raise NotImplementedError("Implement __init__")

    def register_user(self, email: str, password: str, name: str) -> Dict[str, Any]:
        raise NotImplementedError("Implement register_user")

    def login(self, email: str, password: str) -> Dict[str, str]:
        raise NotImplementedError("Implement login")

    def refresh_access_token(self, refresh_token: str) -> Dict[str, str]:
        raise NotImplementedError("Implement refresh_access_token")

    def logout(self, access_token: str) -> bool:
        raise NotImplementedError("Implement logout")

    def verify_session(self, access_token: str) -> Dict[str, Any]:
        raise NotImplementedError("Implement verify_session")
