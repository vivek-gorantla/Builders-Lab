import sys
import os
import pytest

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)
if 'solution' in sys.modules:
    del sys.modules['solution']

from solution import LLMChatService

def test_create_and_send_message():
    svc = LLMChatService()
    conv_id = svc.create_conversation("user_123", "You are a coding assistant.")
    
    response = svc.send_message(conv_id, "How do I write a Python function?")
    assert "role" in response and response["role"] == "assistant"
    assert "content" in response and len(response["content"]) > 0
    assert "tokens_used" in response and response["tokens_used"] > 0

def test_conversation_history_memory():
    svc = LLMChatService()
    conv_id = svc.create_conversation("user_123")

    svc.send_message(conv_id, "Hello!")
    svc.send_message(conv_id, "What is Python?")

    history = svc.get_conversation_history(conv_id)
    # Should include system prompt, first user + assistant messages, second user + assistant messages
    assert len(history) >= 5
    assert history[0]["role"] == "system"

def test_token_tracking_per_user():
    svc = LLMChatService()
    conv_id = svc.create_conversation("alice")
    svc.send_message(conv_id, "Explain vector databases in detail.")

    usage = svc.get_user_token_usage("alice")
    assert usage["total_prompt_tokens"] > 0
    assert usage["total_completion_tokens"] > 0
    assert usage["total_tokens"] == usage["total_prompt_tokens"] + usage["total_completion_tokens"]

def test_unknown_conversation_raises_key_error():
    svc = LLMChatService()
    with pytest.raises(KeyError):
        svc.send_message("invalid_conv_id", "Hello")
