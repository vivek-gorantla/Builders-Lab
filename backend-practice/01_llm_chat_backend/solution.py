from typing import List, Dict, Any, Optional

class LLMChatService:
    """LLM Chat backend service with conversation memory, system prompts, and token tracking."""

    def __init__(self, max_context_messages: int = 10) -> None:
        raise NotImplementedError("Implement __init__")

    def create_conversation(self, user_id: str, system_prompt: str = "You are a helpful AI assistant.") -> str:
        raise NotImplementedError("Implement create_conversation")

    def send_message(self, conversation_id: str, user_content: str) -> Dict[str, Any]:
        raise NotImplementedError("Implement send_message")

    def get_conversation_history(self, conversation_id: str) -> List[Dict[str, str]]:
        raise NotImplementedError("Implement get_conversation_history")

    def get_user_token_usage(self, user_id: str) -> Dict[str, int]:
        raise NotImplementedError("Implement get_user_token_usage")
