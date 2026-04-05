"""Neural Reasoning Engine - Free Gemini API."""

import os
import google.generativeai as genai

SYSTEM_PROMPT = """You are a helpful, empathetic university assistant for students and applicants.
You assist with academic queries, student wellbeing, career guidance, and general university life.
Be warm, concise, and supportive. Keep responses under 200 words."""

def generate(query: str, conversation_history: list = None) -> dict:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {
            "path": "neural",
            "answer": "Please set your GEMINI_API_KEY to enable AI responses.",
            "confidence": "low",
        }
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=SYSTEM_PROMPT)
    response = model.generate_content(query)
    return {
        "path": "neural",
        "answer": response.text,
        "confidence": "generative",
    }