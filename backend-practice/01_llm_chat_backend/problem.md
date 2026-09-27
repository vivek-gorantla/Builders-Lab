# Problem 01: ChatGPT / LLM Chat Assistant API

## 1. Scenario
Modern AI platforms like ChatGPT maintain conversation memory history, apply system prompts, count prompt and completion token consumption per user, and manage sliding context window limits.

## 2. Goal
Build the `LLMChatService` backend manager that simulates or connects to an LLM provider while managing state, history, and usage statistics.

## 3. Required Class
- `LLMChatService`

## 4. Required Methods
- `create_conversation(user_id: str, system_prompt: str = "You are a helpful AI assistant.") -> str`
- `send_message(conversation_id: str, user_content: str) -> dict`
- `get_conversation_history(conversation_id: str) -> list[dict]`
- `get_user_token_usage(user_id: str) -> dict`

## 5. Behavior
- `create_conversation`: Generates a unique `conversation_id`, initializes message history starting with system prompt message `{"role": "system", "content": system_prompt}`.
- `send_message`: Appends user message `{"role": "user", "content": user_content}`, generates AI completion message `{"role": "assistant", "content": assistant_response}`, estimates token usage (e.g. 1 token $\approx$ 4 characters or word count approximation), updates user's aggregate token usage, and returns `{"role": "assistant", "content": ..., "tokens_used": int}`.
- Context Pruning: If conversation history exceeds `max_context_messages`, keep system prompt and the most recent `max_context_messages` messages.
- `get_user_token_usage`: Returns `{"total_prompt_tokens": int, "total_completion_tokens": int, "total_tokens": int}`.

## 6. Validation Rules
- Empty `user_content` raises `ValueError`.
- Accessing non-existent `conversation_id` raises `KeyError`.

## 7. Edge Cases
- Multiple conversations owned by the same user aggregate into the user's total token usage.

## 8. Examples
```python
chat = LLMChatService()
conv_id = chat.create_conversation("user1", "You are a Python expert.")
res = chat.send_message(conv_id, "What is a decorator?")
print(res["content"])
```

## 9. Constraints
- Pure Python standard library. (Optional: Can connect to real LLM API like OpenAI if API key provided via environment variable, but must work out-of-the-box with built-in completion generator).

## 10. Left for Developer Decision
- Mock completion response generator vs real API adapter.
