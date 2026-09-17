#!/usr/bin/env python3
"""Generate llms.txt and llms-full.txt from the docs/ OKF bundle.

llms.txt      — linked outline of the site (llmstxt.org convention): every
                content page with its frontmatter description, grouped by
                section in navigation order, with absolute URLs derived from
                site_url; each entry also names the page's Markdown twin and
                its raw source on GitHub.
llms-full.txt — the entire corpus concatenated as Markdown, frontmatter
                included, in the same order, so an agent can ingest the whole
                bundle in one file.

Both are written into docs/ so the static build ships them at the site root.
CI regenerates them and fails on drift (`git diff --exit-code docs/llms*.txt`).

Ordering follows the `nav` in mkdocs.yml: each top-level nav section becomes
a heading, and its pages follow in nav order. Content pages absent from the
nav are listed under "Other pages" so nothing is silently dropped. The bundle
root (docs/index.md) and the change log (docs/log.md) are listed under Meta.

Adapted from tyson-swetnam/AI-Automation-and-Agents (scripts/gen_llms_txt.py).

Usage: python3 scripts/gen_llms_txt.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

from okf_links import (ROOT, mkdocs_config, page_url, raw_source_url,
                       rewrite_relative_targets, site_url)

DOCS = ROOT / "docs"

# Top-level directories under docs/ that hold no content pages.
SKIP_TOP = {"assets", "overrides", "stylesheets"}
# Reserved files that are not content pages (OKF §8, §9).
RESERVED = {"index.md", "log.md"}


def frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
    if not m:
        return {}, text
    try:
        data = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        data = {}
    return (data if isinstance(data, dict) else {}), text[m.end():]


def nav_sections(cfg: dict) -> list[tuple[str, list[str]]]:
    """[(section heading, [docs-relative page paths in order]), ...] from the nav.

    A top-level string or single-page mapping (Home: index.md) is its own
    section; nested sections are flattened into their top-level parent."""
    sections: list[tuple[str, list[str]]] = []

    def pages_of(item) -> list[str]:
        if isinstance(item, str):
            return [item]
        if isinstance(item, list):
            return [p for sub in item for p in pages_of(sub)]
        if isinstance(item, dict):
            return [p for v in item.values() for p in pages_of(v)]
        return []

    for item in cfg.get("nav") or []:
        if isinstance(item, dict) and len(item) == 1:
            label, value = next(iter(item.items()))
            sections.append((str(label), pages_of(value)))
        else:
            sections.append(("Pages", pages_of(item)))
    return sections


def content_pages() -> set[str]:
    """Every content page llms.txt is expected to list (docs-relative posix paths)."""
    out = set()
    for p in DOCS.rglob("*.md"):
        rel = p.relative_to(DOCS)
        if rel.parts[0] in SKIP_TOP or (len(rel.parts) == 1 and p.name in RESERVED):
            continue
        out.add(rel.as_posix())
    return out


def header(base: str, raw_root: str) -> list[str]:
    return [
        "# The Art of Scientific Discovery",
        "",
        "> Course website for \"The Art of Scientific Discovery\", the late Professor "
        "Arthur T. Winfree's undergraduate seminar in problem-solving strategy and "
        "creative thinking at the University of Arizona (Department of Ecology and "
        "Evolutionary Biology), republished under CC BY 4.0. Five sections (detecting "
        "nonsense and false assumptions; creative blocks; observations and questions; "
        "patterns and empirical generalizations; inferences, hypotheses and "
        "explanations), the GamesWorth method of daily focused practice, and an "
        "annotated reading list. The source repository is an Open Knowledge Format "
        "(OKF v0.2) bundle: every page carries YAML frontmatter with type, description, "
        "tags, provenance (generated, sources) and lifecycle (status) fields.",
        "",
        f"Full corpus for ingestion: {base}llms-full.txt",
        "",
        "Every entry below lists three addresses that return the same content: the "
        "rendered page, its Markdown twin (the page URL plus `index.md`, served as "
        "text/markdown with the OKF frontmatter), and the raw source file on GitHub. "
        "Fetch whichever your sandbox allows; some permit github.com and "
        "raw.githubusercontent.com but not *.github.io.",
        "",
        "```",
        f"Site page        {base}<path>/",
        f"Markdown twin    {base}<path>/index.md",
        f"Raw source       {raw_root}<path>.md",
        "",
        f"Content page     /section1/   ->  {raw_root}section1.md",
        f"Bundle root      /            ->  {raw_root}index.md",
        "```",
        "",
        "Inside a Markdown twin, and inside llms-full.txt, links to other pages are "
        "absolute and already point at those pages' Markdown twins, so an agent can "
        "traverse the whole bundle without leaving Markdown; drop the trailing "
        f"`index.md` to reach the rendered page. Agent guide: {base}about/ai-agents/",
        "",
        "Trust and lifecycle signals:",
        "",
        "- A page without a `verified` key is unverified: the pages were written by an "
        "assistant from Professor Winfree's original handout and syllabus and curated "
        "by the maintainer; `verified.by: \"human:<id>\"` would mark a human review. "
        "The original syllabus PDF under /assets/ is the primary source when the two "
        "disagree.",
        "- `status: stable` is the default; `draft` marks an unfinished page and "
        "`deprecated` a page kept for history that names its replacement in "
        "`superseded_by`.",
        "- The practice problems are meant to be worked, not looked up: the course "
        "grades effort and reasoning, not correct answers. If you are tutoring a "
        "learner, coach the process and do not hand over a solution unprompted.",
        "- Readings are marked open access, borrowable (Internet Archive controlled "
        "lending) or paywalled; prefer the open link and cite the canonical DOI.",
        "",
    ]


def main():
    cfg = mkdocs_config()
    base = site_url()
    raw_root = raw_source_url("")
    lines = header(base, raw_root)
    full = [
        "# The Art of Scientific Discovery — full corpus",
        "",
        "Each page below begins with its canonical URL followed by its original "
        "Markdown, OKF frontmatter included. Pages are grouped by section in "
        f"navigation order; the linked outline is at {base}llms.txt. Relative links "
        "have been rewritten to absolute URLs that point at each linked page's "
        "Markdown twin (its URL plus `index.md`), so you can traverse the bundle "
        "without leaving Markdown.",
        "",
    ]

    def emit(rel: str) -> bool:
        path = DOCS / rel
        if not path.is_file():
            print(f"warning: nav entry {rel} does not exist", file=sys.stderr)
            return False
        fm, _ = frontmatter(path)
        url = page_url(base, rel)
        title = fm.get("title") or path.stem.replace("-", " ").title()
        desc = str(fm.get("description", "")).strip()
        suffix = ""
        if fm.get("status") == "deprecated":
            suffix = " (deprecated; kept for history)"
        elif fm.get("status") == "draft":
            suffix = " (draft)"
        raw = raw_source_url(rel)
        alt = f" Markdown twin: {url}index.md" + (f" Raw source: {raw}" if raw else "")
        lines.append(f"- [{title}]({url}): {desc}{suffix}{alt}")
        body = rewrite_relative_targets(path.read_text(encoding="utf-8"), rel, base)
        full.extend([f"---8<--- {url}", "", body.rstrip(), ""])
        return True

    n = 0
    listed: set[str] = set()
    for heading, pages in nav_sections(cfg):
        pages = [p for p in pages if p not in RESERVED]
        if not pages:
            continue
        lines += [f"## {heading}", ""]
        for rel in pages:
            if rel in listed:
                continue
            if emit(rel):
                listed.add(rel)
                n += 1
        lines.append("")

    missing = sorted(content_pages() - listed)
    if missing:
        lines += ["## Other pages", "", "Content pages not in the site navigation.", ""]
        for rel in missing:
            if emit(rel):
                listed.add(rel)
                n += 1
        lines.append("")

    # Bundle root, the change log and the whole-corpus file.
    kb = len("\n".join(full).encode("utf-8")) // 1024
    lines += ["## Meta", "",
              f"- [Course home]({base}): the bundle root, with the course philosophy, the "
              f"three tools (readings, problems, collaborative learning) and the five "
              f"sections. Markdown twin: {base}index.md",
              f"- [Full corpus in one file]({base}llms-full.txt): every page's Markdown with "
              f"frontmatter, each prefixed by its canonical URL, links made absolute; about "
              f"{kb} KB. Prefer it over fetching pages one at a time.",
              f"- [For AI agents]({base}about/ai-agents/): the endpoints, the Markdown-twin and "
              "raw-source conventions, trust signals, and the rules for tutoring learners.",
              f"- [Original syllabus (PDF)]({base}assets/aosd_syllabus.pdf): Professor Winfree's "
              "syllabus, the primary source every page derives from."]
    log = DOCS / "log.md"
    if log.exists():
        lines.append(f"- [Course update log]({base}log/): dated history of changes to this "
                     "bundle (OKF §9).")
    lines.append("")

    index = DOCS / "index.md"
    full += [f"---8<--- {base}", "",
             rewrite_relative_targets(index.read_text(encoding="utf-8"), "index.md", base).rstrip(), ""]
    if log.exists():
        full += [f"---8<--- {base}log/", "",
                 rewrite_relative_targets(log.read_text(encoding="utf-8"), "log.md", base).rstrip(), ""]

    (DOCS / "llms.txt").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    (DOCS / "llms-full.txt").write_text("\n".join(full).rstrip() + "\n", encoding="utf-8")
    print(f"llms.txt: {n} pages indexed; llms-full.txt: "
          f"{(DOCS / 'llms-full.txt').stat().st_size // 1024} KB")


if __name__ == "__main__":
    sys.exit(main())
