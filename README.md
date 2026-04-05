# Orchestrated Hybrid Intelligence Agent
### University Academic Query Assistant

A **Neuro-Symbolic AI** system combining deterministic symbolic reasoning with LLM-based neural generation.

---

## Architecture

```
User Query
    │
    ▼
┌─────────────────────────┐
│      Orchestrator        │  ← intent classification
│  (semantic analysis)     │
└────────┬────────┬────────┘
         │        │
    Factual?   Ambiguous/
    Logical?   Emotional?
         │        │
         ▼        ▼
┌──────────┐  ┌──────────┐
│ Symbolic │  │  Neural  │
│ Engine   │  │  Engine  │
│ (Rules)  │  │ (Claude) │
└────┬─────┘  └────┬─────┘
     └──────┬───────┘
            ▼
    Response Synthesis
            │
            ▼
       Final Answer
```

## Features
- **Zero hallucinations** on factual queries (fees, dates, rules) via symbolic path
- **Empathetic responses** for emotional/ambiguous queries via neural path
- **Automatic fallback**: symbolic → neural if no rule matches
- **Session memory** for multi-turn neural conversations
- **Visual badges** showing which reasoning path was used

## Project Structure
```
hybrid_agent/
├── app.py              # Flask web server
├── orchestrator.py     # Intent classifier + router
├── symbolic_engine.py  # Rule-based reasoning
├── neural_engine.py    # Anthropic Claude API
├── knowledge_base.py   # University facts, rules, constraints
├── requirements.txt
└── templates/
    └── index.html      # Chat web UI
```

## Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your Anthropic API key (for neural path)
export ANTHROPIC_API_KEY=sk-ant-...

# 3. Run
python app.py

# 4. Open browser at http://localhost:5000
```

> **Without API key**: Symbolic path works fully. Neural path shows a graceful fallback message.

## Knowledge Base Coverage
| Topic | Path |
|---|---|
| Fees & charges | Symbolic |
| Admission process | Symbolic |
| Exam schedule & grading | Symbolic |
| Scholarships | Symbolic |
| Hostel & accommodation | Symbolic |
| Placements & packages | Symbolic |
| Library | Symbolic |
| Programs & departments | Symbolic |
| Contact information | Symbolic |
| Career advice, stress, study tips | Neural |
| General conversation | Neural |

## Tech Stack
- **Python 3.9+** · Flask · Anthropic SDK
- **Symbolic AI**: rule-based inference, pattern matching
- **Neural AI**: Claude Sonnet via Anthropic API
- **Frontend**: Vanilla HTML/CSS/JS (no frameworks)
