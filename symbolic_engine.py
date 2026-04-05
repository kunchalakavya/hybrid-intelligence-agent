"""Symbolic Reasoning Engine - deterministic, rule-based, zero hallucinations."""

from knowledge_base import FACTS, RULES, CONSTRAINTS


def _fmt_program(name, p):
    fee_total = p['fee_per_sem'] * p['semesters'] if isinstance(p['semesters'], int) else "variable"
    fee_str = f"₹{fee_total:,}" if isinstance(fee_total, int) else fee_total
    return (f"**{name}** ({p['duration']})\n"
            f"- Eligibility: {p['eligibility']}\n"
            f"- Entrance: {p['entrance']}\n"
            f"- Fee/semester: ₹{p['fee_per_sem']:,}  |  Total tuition: {fee_str}")


def _answer_fees(q):
    lines = ["**Fee Structure**\n"]
    for prog, data in FACTS["programs"].items():
        sems = data["semesters"]
        per_sem = data["fee_per_sem"]
        total = per_sem * sems if isinstance(sems, int) else "variable"
        total_str = f"₹{total:,}" if isinstance(total, int) else total
        lines.append(f"• **{prog}**: ₹{per_sem:,}/sem | Total: {total_str}")
    ex = FACTS["fees_extra"]
    lines.append(f"\n**Additional charges:**")
    lines.append(f"• Hostel: ₹{ex['hostel_per_year']:,}/year")
    lines.append(f"• Exam fee: ₹{ex['exam_fee_per_sem']:,}/semester")
    lines.append(f"• Registration (one-time): ₹{ex['registration']:,}")
    return "\n".join(lines)


def _answer_admission(q):
    a = FACTS["admission"]
    docs = "\n".join(f"  {i+1}. {d}" for i, d in enumerate(a["documents"]))
    return (f"**Admission Information**\n\n"
            f"**Application Window:** {a['application_window']}\n\n"
            f"**Process:** {a['process']}\n\n"
            f"**Required Documents:**\n{docs}")


def _answer_exam(q):
    e = FACTS["exam_schedule"]
    g = FACTS["grading"]
    grade_str = " | ".join(f"{k}: {v}" for k, v in g["grade_map"].items())
    return (f"**Examination & Grading**\n\n"
            f"**Mid-Semester Exams:**\n"
            f"• Odd semester: {e['mid_semester']['odd']}\n"
            f"• Even semester: {e['mid_semester']['even']}\n\n"
            f"**End-Semester Exams:**\n"
            f"• Odd semester: {e['end_semester']['odd']}\n"
            f"• Even semester: {e['end_semester']['even']}\n\n"
            f"**Results:** {e['results']}\n"
            f"**Backlog exams:** {e['backlog_exam']}\n\n"
            f"**Grading System ({g['system']}):**\n{grade_str}\n"
            f"• Pass marks: {g['pass_mark']}%\n"
            f"• Minimum attendance: {g['minimum_attendance']}\n"
            f"• CGPA to % conversion: {g['cgpa_to_percent']}")


def _answer_scholarship(q):
    lines = ["**Scholarships Available**\n"]
    for s in FACTS["scholarships"]:
        lines.append(f"**{s['name']}**\n  Criteria: {s['criteria']}\n  Benefit: {s['benefit']}\n")
    return "\n".join(lines)


def _answer_hostel(q):
    h = FACTS["hostel"]
    types = ", ".join(h["types"])
    fac = ", ".join(h["facilities"])
    return (f"**Hostel Information**\n\n"
            f"**Room types:** {types}\n"
            f"**Facilities:** {fac}\n"
            f"**Mess fee:** ₹{h['mess_fee_per_month']:,}/month\n"
            f"**Allocation:** {h['allocation']}")


def _answer_placement(q):
    p = FACTS["placements"]
    pkg = "\n".join(f"  • {dept}: ₹{lpa} LPA" for dept, lpa in p["avg_package_lpa"].items())
    recruiters = ", ".join(p["top_recruiters"])
    return (f"**Placement Information**\n\n"
            f"**Cell:** {p['cell']}\n"
            f"**Eligibility:** CGPA ≥ {CONSTRAINTS['min_cgpa_placement']}, no active backlogs\n"
            f"**Top Recruiters:** {recruiters}\n"
            f"**Highest Package:** ₹{p['highest_package_lpa']} LPA\n\n"
            f"**Average Packages by Department:**\n{pkg}")


def _answer_library(q):
    lib = FACTS["library"]
    res = ", ".join(lib["e_resources"])
    return (f"**Library Information**\n\n"
            f"**Timings:** {lib['timing']}\n"
            f"**Books per student:** {lib['books_per_student']}\n"
            f"**Loan period:** {lib['loan_period_days']} days\n"
            f"**Fine:** ₹{lib['fine_per_day']}/day overdue\n"
            f"**E-Resources:** {res}")


def _answer_program(q):
    lines = ["**Academic Programs**\n"]
    for name, p in FACTS["programs"].items():
        lines.append(_fmt_program(name, p))
        lines.append("")
    depts = "\n".join(f"  • **{k}**: {v}" for k, v in FACTS["departments"].items())
    lines.append(f"**Departments:**\n{depts}")
    return "\n".join(lines)


def _answer_contact(q):
    c = FACTS["contacts"]
    lines = ["**Contact Directory**\n"]
    for dept, info in c.items():
        lines.append(f"• **{dept.capitalize()}:** {info}")
    return "\n".join(lines)


_HANDLERS = {
    "fees":       _answer_fees,
    "admission":  _answer_admission,
    "exam":       _answer_exam,
    "scholarship":_answer_scholarship,
    "hostel":     _answer_hostel,
    "placement":  _answer_placement,
    "library":    _answer_library,
    "program":    _answer_program,
    "contact":    _answer_contact,
}


def reason(query: str) -> dict:
    """Run symbolic reasoning. Returns dict with answer, topic, rule_fired."""
    q = query.lower()
    for rule in RULES:
        if rule["condition"](q):
            topic = rule["topic"]
            answer = _HANDLERS[topic](q)
            return {
                "path": "symbolic",
                "rule_fired": rule["id"],
                "topic": topic,
                "answer": answer,
                "confidence": "deterministic",
            }
    return {"path": "symbolic", "rule_fired": None, "topic": None, "answer": None, "confidence": None}
