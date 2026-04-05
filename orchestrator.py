"""Orchestrator - semantic analysis, intent classification, query routing."""

import re

# Keywords that signal emotional/ambiguous/conversational queries → neural path
NEURAL_TRIGGERS = [
    r"\b(feel|feeling|stressed|anxious|worried|scared|depressed|sad|happy|frustrated|overwhelmed)\b",
    r"\b(should i|what do you think|advice|suggest|help me decide|opinion)\b",
    r"\b(career|future|goal|dream|passion|motivation|purpose)\b",
    r"\b(friend|family|relationship|loneliness|homesick)\b",
    r"\b(how to study|tips|strategy|improve|better at|struggle)\b",
    r"\b(why is|explain|understand|difference between|compare|pros and cons)\b",
    r"\b(hi|hello|hey|thanks|thank you|please|good morning|good evening)\b",
]

# If query is very short and vague → likely conversational
def _is_conversational(q: str) -> bool:
    return len(q.split()) <= 4 and not any(
        kw in q for kw in ["fee", "exam", "hostel", "admission", "scholarship",
                            "placement", "library", "program", "contact", "grade"]
    )


def classify(query: str) -> str:
    """
    Returns 'symbolic' or 'neural'.
    Think-Before-Acting: analyse before routing.
    """
    q = query.lower().strip()

    # Step 1: Check neural triggers
    for pattern in NEURAL_TRIGGERS:
        if re.search(pattern, q):
            return "neural"

    # Step 2: Short/conversational check
    if _is_conversational(q):
        return "neural"

    # Step 3: Default to symbolic for factual/structured queries
    return "symbolic"


def route(query: str, symbolic_fn, neural_fn) -> dict:
    """
    Main orchestration pipeline.
    1. Classify intent
    2. Route to appropriate reasoning path
    3. Return enriched response dict
    """
    path = classify(query)

    if path == "symbolic":
        result = symbolic_fn(query)
        # Fallback: if symbolic finds no matching rule, escalate to neural
        if result.get("answer") is None:
            result = neural_fn(query)
            result["fallback"] = True
        else:
            result["fallback"] = False
    else:
        result = neural_fn(query)
        result["fallback"] = False

    result["query"] = query
    return result
