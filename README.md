# hybrid-intelligence-agent
🎓 Orchestrated Hybrid Intelligence Agent
Neuro-Symbolic AI for University Query Assistance

B.Tech Final Year Project — Vignan Institute of Technology and Science, Hyderabad
Department of Computer Science & Engineering (AI & ML)
Author: Kunchala Kavya


📌 Overview
A Hybrid Intelligence Agent that combines deterministic symbolic reasoning with LLM-based neural generation to answer university-related queries — with zero hallucinations on factual questions.
Instead of routing every query through an expensive LLM, the system uses a Think-Before-Acting paradigm:
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
│ (Rules)  │  │ (Gemini) │
└────┬─────┘  └────┬─────┘
     └──────┬───────┘
            ▼
    Response Synthesis
            │
            ▼
       Final Answer

✨ Features
FeatureDescription⚙️ Zero HallucinationsFactual queries (fees, dates, rules) answered via deterministic symbolic rules🧠 Neural EmpathyEmotional/conversational queries handled by Gemini LLM🔀 Auto FallbackSymbolic → Neural if no rule matches💬 Session MemoryMulti-turn conversation history for neural path🏷️ Reasoning BadgesUI shows which path answered each query🚀 FastSub-second symbolic responses; no API call needed

🗂️ Project Structure
hybrid_agent/
├── app.py              # Flask web server & API endpoints
├── orchestrator.py     # Intent classifier + query router
├── symbolic_engine.py  # Rule-based deterministic reasoning
├── neural_engine.py    # Gemini API integration
├── knowledge_base.py   # University facts, IF-THEN rules, constraints
├── requirements.txt
└── templates/
    └── index.html      # Chat web UI

🏗️ Architecture
Orchestrator (orchestrator.py)
Classifies every query using a 3-step pipeline:

Neural Trigger Check — Regex patterns detect emotional, advisory, or conversational language
Length Heuristic — Short vague queries (≤4 words) route to neural
Default — All remaining queries go to symbolic engine

Symbolic Engine (symbolic_engine.py)

Matches query against 9 IF-THEN rules (R1–R9)
Topics: fees, admission, exams, scholarships, hostel, placements, library, programs, contacts
Returns deterministic, traceable answers from the knowledge base
Confidence: deterministic — same input always gives same output

Neural Engine (neural_engine.py)

Powered by Google Gemini API (free tier)
Handles: career advice, stress, study tips, general conversation
Maintains session history for multi-turn context
Constrained by a system prompt to avoid making up specific numbers

Knowledge Base (knowledge_base.py)
Structured university data including:

Program fees, eligibility, entrance exams
Exam schedule, grading system (10-point CGPA)
Scholarships, hostel info, placement stats
Contact directory


⚙️ Setup & Run
1. Clone the repo
bashgit clone https://github.com/your-username/hybrid-agent.git
cd hybrid-agent
2. Install dependencies
bashpip install -r requirements.txt
pip install google-genai   # for Gemini neural path
3. Get a free Gemini API key

Go to aistudio.google.com/apikey
Sign in with Google → Create API Key
Copy the key

4. Set the API key & run
Linux / Mac:
bashexport GEMINI_API_KEY=your-key-here
python app.py
Windows:
cmdset GEMINI_API_KEY=your-key-here
python app.py
From Spyder / Jupyter:
pythonimport os, subprocess
os.environ["GEMINI_API_KEY"] = "your-key-here"
subprocess.Popen(["python", "app.py"])
5. Open in browser
http://localhost:5000

Without API key: Symbolic path works fully. Neural path shows a graceful fallback message.


🧪 Test Queries
QueryPathRuleWhat is the fee for B.Tech?⚙️ SymbolicR1Tell me about scholarships⚙️ SymbolicR4What are hostel facilities?⚙️ SymbolicR5Placement packages by department?⚙️ SymbolicR6I'm feeling stressed about exams🧠 Neural—Give me study tips🧠 Neural—Should I choose CSE or AI?🧠 Neural—

📦 Requirements
flask>=3.0
google-genai
Python 3.9+ recommended.

🔮 How to Extend

Add new facts → edit FACTS dict in knowledge_base.py
Add new rules → append to RULES list with a condition lambda and topic
Add new topic handler → add a function to symbolic_engine.py and register in _HANDLERS
Swap LLM → replace neural_engine.py with any other API (OpenAI, Anthropic, Groq, Ollama)


🛠️ Tech Stack

Backend: Python 3, Flask
Symbolic AI: Custom rule-based inference engine
Neural AI: Google Gemini API (gemini-2.0-flash)
Frontend: Vanilla HTML / CSS / JavaScript
Architecture: Neuro-Symbolic AI, Knowledge Representation & Reasoning (KRR)
