"""University Knowledge Base - facts, rules, constraints for symbolic reasoning."""

FACTS = {
    "programs": {
        "B.Tech": {"duration": "4 years", "semesters": 8, "eligibility": "10+2 PCM ≥60%", "entrance": "JEE Main / State CET", "fee_per_sem": 75000},
        "M.Tech": {"duration": "2 years", "semesters": 4, "eligibility": "B.Tech ≥55%", "entrance": "GATE", "fee_per_sem": 60000},
        "MBA":    {"duration": "2 years", "semesters": 4, "eligibility": "Any degree ≥50%", "entrance": "CAT/MAT/XAT", "fee_per_sem": 90000},
        "MCA":    {"duration": "2 years", "semesters": 4, "eligibility": "B.Sc/BCA with Maths", "entrance": "NIMCET", "fee_per_sem": 55000},
        "Ph.D":   {"duration": "3–5 years", "semesters": "flexible", "eligibility": "Master's ≥55%", "entrance": "University Entrance Test", "fee_per_sem": 30000},
    },
    "departments": {
        "CSE": "Computer Science & Engineering",
        "ECE": "Electronics & Communication",
        "ME":  "Mechanical Engineering",
        "CE":  "Civil Engineering",
        "AI":  "Artificial Intelligence & ML",
        "DS":  "Data Science",
    },
    "fees_extra": {
        "hostel_per_year": 50000,
        "exam_fee_per_sem": 2000,
        "registration": 5000,
    },
    "scholarships": [
        {"name": "Merit Scholarship",   "criteria": "Top 10% CGPA",               "benefit": "50% tuition waiver"},
        {"name": "SC/ST Scholarship",   "criteria": "SC/ST, income < 2.5 LPA",    "benefit": "Full tuition + ₹1000/month"},
        {"name": "Sports Scholarship",  "criteria": "National/State sports rep",   "benefit": "25% tuition waiver"},
        {"name": "MBA Entrance Award",  "criteria": "CAT/MAT score ≥90 percentile","benefit": "30% MBA tuition waiver"},
    ],
    "exam_schedule": {
        "mid_semester":  {"odd": "September Week 3", "even": "February Week 3"},
        "end_semester":  {"odd": "November–December", "even": "April–May"},
        "results":       "Within 30 days of last exam",
        "backlog_exam":  "June and December",
    },
    "grading": {
        "system": "10-point CGPA",
        "pass_mark": 40,
        "grade_map": {"O": "91–100", "A+": "81–90", "A": "71–80", "B+": "61–70", "B": "51–60", "C": "40–50", "F": "<40"},
        "cgpa_to_percent": "CGPA × 9.5",
        "minimum_attendance": "75%",
    },
    "admission": {
        "application_window": "January–March (for July intake)",
        "documents": ["10th marksheet", "12th marksheet", "Entrance scorecard", "Transfer certificate", "ID proof", "Passport photos"],
        "process": "Apply online → Document verification → Counselling → Fee payment → Enrollment",
    },
    "hostel": {
        "types": ["Single occupancy", "Double occupancy", "Triple occupancy"],
        "facilities": ["Wi-Fi", "Laundry", "Mess", "24×7 security", "Common room"],
        "mess_fee_per_month": 3500,
        "allocation": "First-come first-served after admission confirmation",
    },
    "library": {
        "timing": "8 AM – 10 PM (Mon–Sat), 10 AM – 6 PM (Sun)",
        "books_per_student": 3,
        "loan_period_days": 14,
        "fine_per_day": 5,
        "e_resources": ["IEEE Xplore", "Springer", "NPTEL", "DELNET"],
    },
    "placements": {
        "cell": "Training & Placement Cell (TPC)",
        "eligibility": "CGPA ≥ 6.0, no active backlogs",
        "top_recruiters": ["TCS", "Infosys", "Wipro", "Cognizant", "Amazon", "Google", "Microsoft"],
        "avg_package_lpa": {"CSE": 7.5, "AI": 9.0, "DS": 8.5, "ECE": 6.0, "ME": 5.5, "CE": 5.0},
        "highest_package_lpa": 42,
    },
    "contacts": {
        "admissions":  "admissions@university.edu | +91-9000000001",
        "examinations":"exam.cell@university.edu | +91-9000000002",
        "placements":  "tpc@university.edu | +91-9000000003",
        "hostel":      "hostel.warden@university.edu | +91-9000000004",
        "general":     "info@university.edu | +91-9000000000",
    },
}

# ── RULES (if-then logic for symbolic inference) ──────────────────────────────

RULES = [
    {
        "id": "R1",
        "condition": lambda q: any(w in q for w in ["fee", "fees", "cost", "tuition", "payment", "charge"]),
        "topic": "fees",
    },
    {
        "id": "R2",
        "condition": lambda q: any(w in q for w in ["admission", "apply", "application", "enroll", "join", "eligib"]),
        "topic": "admission",
    },
    {
        "id": "R3",
        "condition": lambda q: any(w in q for w in ["exam", "examination", "schedule", "date", "backlog", "result", "grade", "cgpa", "attendance", "pass", "fail"]),
        "topic": "exam",
    },
    {
        "id": "R4",
        "condition": lambda q: any(w in q for w in ["scholarship", "waiver", "financial", "aid", "stipend"]),
        "topic": "scholarship",
    },
    {
        "id": "R5",
        "condition": lambda q: any(w in q for w in ["hostel", "accommodation", "room", "mess", "dorm"]),
        "topic": "hostel",
    },
    {
        "id": "R6",
        "condition": lambda q: any(w in q for w in ["placement", "job", "recruit", "package", "salary", "campus", "hire"]),
        "topic": "placement",
    },
    {
        "id": "R7",
        "condition": lambda q: any(w in q for w in ["library", "book", "journal", "ieee", "springer", "nptel", "fine"]),
        "topic": "library",
    },
    {
        "id": "R8",
        "condition": lambda q: any(w in q for w in ["program", "course", "department", "branch", "btech", "mtech", "mba", "mca", "phd", "b.tech", "m.tech"]),
        "topic": "program",
    },
    {
        "id": "R9",
        "condition": lambda q: any(w in q for w in ["contact", "phone", "email", "office", "reach", "address"]),
        "topic": "contact",
    },
]

# ── CONSTRAINTS (hard checks) ─────────────────────────────────────────────────

CONSTRAINTS = {
    "min_attendance": 75,
    "min_pass_marks": 40,
    "min_cgpa_placement": 6.0,
    "max_books_library": 3,
    "loan_period_days": 14,
}
