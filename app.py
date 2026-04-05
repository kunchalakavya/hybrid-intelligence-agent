"""
Orchestrated Hybrid Intelligence Agent - Flask Web App
University Academic Query Assistant
"""

import os
from flask import Flask, render_template, request, jsonify, session
from orchestrator import route
from symbolic_engine import reason
from neural_engine import generate

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "hybrid-agent-dev-key-2024")


@app.route("/")
def index():
    session.clear()
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("query", "").strip()
    if not query:
        return jsonify({"error": "Empty query"}), 400

    # Maintain conversation history in session for neural context
    history = session.get("history", [])

    result = route(
        query=query,
        symbolic_fn=reason,
        neural_fn=lambda q: generate(q, history),
    )

    # Update history for neural continuity (only store user+assistant pairs)
    if result["path"] == "neural":
        history.append({"role": "user", "content": query})
        history.append({"role": "assistant", "content": result["answer"]})
        session["history"] = history[-20:]  # keep last 10 turns

    return jsonify({
        "answer":      result["answer"],
        "path":        result["path"],
        "topic":       result.get("topic"),
        "rule_fired":  result.get("rule_fired"),
        "fallback":    result.get("fallback", False),
        "confidence":  result.get("confidence"),
    })


@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n🎓 Hybrid Intelligence Agent running on http://localhost:{port}")
    print("   Set ANTHROPIC_API_KEY env var to enable neural reasoning path.\n")
    app.run(debug=True, port=port)
