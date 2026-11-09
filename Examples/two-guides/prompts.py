"""
prompts.py — the two guide personas and their prompts.
"""

ORGANISATIONS = {
    "thinkcompany": {
        "name": "Helsinki Think Company",
        "role": (
            "people, ideas, community and starting a company: events, "
            "teams, pitching and student entrepreneurship"
        ),
    },
    "aif": {
        "name": "LUMI AI Factory",
        "role": (
            "building AI: computing power, datasets, model training, "
            "expert advice and help with the EU AI Act"
        ),
    },
}

# Minimal system prompt — saves tokens for the answer.
SYSTEM_PROMPT = """You are the guide for {name}. Your organisation focuses on: {role}.

Use ONLY the numbered excerpts below. Give a detailed answer (at least 3 specific suggestions from the excerpts).

RULES:
1. Cite every claim with [n].
2. If the question is NOT about your role ({other_name}: {other_role}), say you can't directly help but offer 2 related suggestions from the excerpts, and tell them to ask {other_name}.
3. If the question IS about your role (starting a company, finding team members, entrepreneurship, pitching), answer fully using the excerpts — DO NOT suggest the other guide.
4. Answer in the same language as the question."""


def system_prompt_for(org_key):
    mine = ORGANISATIONS[org_key]
    other_key = "aif" if org_key == "thinkcompany" else "thinkcompany"
    other = ORGANISATIONS[other_key]
    return SYSTEM_PROMPT.format(
        name=mine["name"],
        role=mine["role"],
        other_name=other["name"],
        other_role=other["role"],
    )


def build_user_message(chunks, question):
    lines = [
        "Excerpts from your own organisation's website (ONLY source of facts):",
        "",
    ]
    for chunk in chunks:
        text = chunk["text"][:200].strip()
        if len(chunk["text"]) > 200:
            text += "..."
        lines.append(f"[{chunk['n']}] Page: {chunk['title']}")
        lines.append(text)
        lines.append("")
    lines.append("Question:")
    lines.append(question)
    return "\n".join(lines)
