#!/usr/bin/env python3
"""Generate the problem index page and the `Problems` navigation block.

Reads the frontmatter of every page under docs/problems/ (except index.md)
and writes:

* docs/problems/index.md — a section listing (OKF §8: no frontmatter) that
  groups every problem by course section, in session order, with its
  one-sentence description, its kind, and a marker when the editors are not
  certain the page describes the problem Winfree assigned
  (`problem.identification` of `probable` or `unknown`).
* the nav block in mkdocs.yml between the markers
  `# problems-nav-begin` and `# problems-nav-end`, so the navigation lists
  every problem under its section without hand-editing.

Run it whenever a problem page is added, renamed or retitled; CI checks
that the committed index matches (`git diff --exit-code docs/problems/index.md
mkdocs.yml`).

Usage: python3 scripts/gen_problem_index.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PROBLEMS = DOCS / "problems"
CONFIG = ROOT / "mkdocs.yml"

SECTION_TITLES = {
    1: "Section 1: Detecting Nonsense, Error Checking, False Assumptions, Cherishing Mistakes",
    2: "Section 2: Creative Blocks",
    3: "Section 3: Observations and Questions",
    4: "Section 4: Patterns, Empirical Generalizations",
    5: "Section 5: Inferences, Hypotheses, Explanations",
}
SECTION_PAGES = {n: f"section{n}.md" for n in SECTION_TITLES}
IDENT_NOTE = {
    "probable": " *(identification probable)*",
    "unknown": " *(identification uncertain)*",
}


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
    if not m:
        return {}
    data = yaml.safe_load(m.group(1))
    return data if isinstance(data, dict) else {}


def load_problems() -> list[dict]:
    out = []
    for path in sorted(PROBLEMS.glob("*.md")):
        if path.name == "index.md":
            continue
        fm = frontmatter(path)
        prob = fm.get("problem") or {}
        try:
            section = int(prob.get("section"))
            session = int(prob.get("session"))
        except (TypeError, ValueError):
            print(f"error: {path.relative_to(ROOT)}: frontmatter needs problem.section and "
                  f"problem.session", file=sys.stderr)
            sys.exit(1)
        out.append({
            "file": path.name,
            "title": str(fm.get("title") or path.stem),
            "description": str(fm.get("description") or "").strip(),
            "section": section,
            "session": session,
            "identification": str(prob.get("identification") or "confident"),
            "kind": str(prob.get("kind") or "puzzle"),
        })
    out.sort(key=lambda p: (p["section"], p["session"], p["title"]))
    return out


def write_index(problems: list[dict]) -> None:
    lines = [
        "# Problems",
        "",
        "Every problem, lab and discussion named in Professor Winfree's "
        "[syllabus](../syllabus.md), one page each, grouped by section and listed in "
        "the order the course met them. Each page gives the statement, why the "
        "problem is in the course, where it comes from, hints, and sources. The "
        "course grades effort rather than answers, so resolutions are folded away "
        "until you choose to open them.",
        "",
        "A few of Winfree's problems are known only by the name in his schedule. "
        "Where the editors could not identify one with confidence, the page says so "
        "and offers the likeliest interpretations; the listing below marks those.",
        "",
    ]
    for n, title in SECTION_TITLES.items():
        items = [p for p in problems if p["section"] == n]
        if not items:
            continue
        lines += [f"## [{title}]({'../' + SECTION_PAGES[n]})", ""]
        for p in items:
            note = IDENT_NOTE.get(p["identification"], "")
            lines.append(f"* Session {p['session']:02d} — [{p['title']}]({p['file']}) "
                         f"({p['kind']}){note} - {p['description']}")
        lines.append("")
    (PROBLEMS / "index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_nav(problems: list[dict]) -> None:
    text = CONFIG.read_text(encoding="utf-8")
    begin, end = "  # problems-nav-begin", "  # problems-nav-end"
    if begin not in text or end not in text:
        print("error: mkdocs.yml lacks the problems-nav-begin/end markers", file=sys.stderr)
        sys.exit(1)
    block = [begin, "  - Problems:", "    - problems/index.md"]
    for n, title in SECTION_TITLES.items():
        items = [p for p in problems if p["section"] == n]
        if not items:
            continue
        short = title.split(":")[0]
        block.append(f"    - {short}:")
        for p in items:
            label = p["title"].replace("'", "''")
            block.append(f"      - '{label}': problems/{p['file']}")
    block.append(end)
    head = text[: text.index(begin)]
    tail = text[text.index(end) + len(end):]
    CONFIG.write_text(head + "\n".join(block) + tail, encoding="utf-8")


def main() -> None:
    problems = load_problems()
    if not problems:
        print("no problem pages under docs/problems/", file=sys.stderr)
        sys.exit(1)
    write_index(problems)
    write_nav(problems)
    uncertain = sum(1 for p in problems if p["identification"] != "confident")
    print(f"problem index: {len(problems)} pages, {uncertain} with uncertain identification; "
          f"nav block rewritten in mkdocs.yml")


if __name__ == "__main__":
    main()
