"""Neural Reasoning Engine - Anthropic Claude API."""
import os
from anthropic import Anthropic

SYSTEM_PROMPT = """You are a helpful, empathetic university assistant for students and applicants.
You assist with academic queries, student wellbeing, career guidance, and general university life.
Be warm, concise, and supportive. Keep responses under 200 words."""
MODEL = "claude-sonnet-4-6"

def generate(query: str, conversation_history: list = None) -> dict:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return {
            "path": "neural",
            "answer": "Please set your ANTHROPIC_API_KEY to enable AI responses.",
            "confidence": "low",
        }
    client = Anthropic(api_key=api_key)

    messages = list(conversation_history) if conversation_history else []
    messages.append({"role": "user", "content": query})

    response = client.messages.create(
        model=MODEL,
        max_tokens=400,
        system=SYSTEM_PROMPT,
        messages=messages,
    )

    answer = "".join(
        block.text for block in response.content if block.type == "text"
    )

    return {
        "path": "neural",
        "answer": answer,
        "confidence": "generative",
    }
