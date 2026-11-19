"""Demo mode: a simple, rule-based report so the starter works with no AI key.

It is deliberately basic. It sorts each line into one of five sections by
looking for a few words. A real model (Day 2) does this far better.
"""
import re

SECTIONS = ["Highlights", "Progress", "Risks", "Blockers", "Next week"]

KEYWORDS = {
    "Blockers": ["blocked", "waiting on", "waiting for", "stuck", "cannot", "can't", "pending approval", "no access"],
    "Risks": ["risk", "delay", "delayed", "might", "may slip", "concern", "worried", "behind", "tight"],
    "Next week": ["next week", "will ", "plan to", "planning", "to do", "todo", "start ", "going to"],
    "Highlights": ["shipped", "launched", "released", "won", "signed", "praised", "milestone", "completed ahead"],
}


def _clean(line: str) -> str:
    return re.sub(r"^[\s\-\*•\d\.\)]+", "", line).strip()


def demo_report(updates: str) -> str:
    buckets = {name: [] for name in SECTIONS}
    for raw in updates.splitlines():
        line = _clean(raw)
        if not line:
            continue
        lowered = line.lower()
        placed = False
        for name in ("Blockers", "Risks", "Next week", "Highlights"):
            if any(word in lowered for word in KEYWORDS[name]):
                buckets[name].append(line)
                placed = True
                break
        if not placed:
            buckets["Progress"].append(line)

    out = ["## Weekly status report", "_Demo mode: sorted with simple rules. A real model writes this much better._", ""]
    for name in SECTIONS:
        out.append(f"### {name}")
        items = buckets[name]
        out.extend(f"- {item}" for item in items) if items else out.append("- Nothing to report.")
        out.append("")
    return "\n".join(out)
