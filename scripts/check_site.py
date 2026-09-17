#!/usr/bin/env python3
"""Post-build assertions on the rendered site.

Run AFTER `zensical build` and `scripts/postbuild_agent_surface.py`. Verifies
that the tree about to be deployed carries the agent surface this site
promises:

  1. llms.txt, llms-full.txt, robots.txt and sitemap.xml exist at the root
     (and robots.txt advertises llms.txt, proving the post-build step ran).
  2. Every content Markdown source under docs/ (assets/, overrides/ and
     stylesheets/ excluded) has an `index.md` mirror at its pretty URL whose
     text is the source with its relative links absolutized (okf_links), there
     are no stray mirrors, and the counts match. llms-full.txt keeps no
     relative link either.
  3. Every mirrored page's index.html declares the Markdown alternate link, the
     visible Markdown button, the machine-readable line, Open Graph tags and a
     schema.org JSON-LD record, and — wherever the source frontmatter has a
     `type` — the okf:type meta. 404.html carries the recovery body and 404.md
     exists beside it. Root and section index.md files carry no type and are
     exempt from the type check.
  4. Every built page carries one `<h1>` and at least 500 characters of
     server-rendered text, and no page redirects with a meta refresh: the
     three things an agent crawler without JavaScript needs from the HTML.
  5. No paragraph in the built HTML contains a literal list marker at the
     start of a line ("- item", "* item", "1. item"). Python-Markdown folds a
     list into the preceding paragraph when no blank line separates them, so
     the marker shows up as text instead of a `<ul>`; the source needs a
     blank line before the list.

Adapted from tyson-swetnam/AI-Automation-and-Agents (scripts/check_site.py).

Usage: python3 scripts/check_site.py <site_dir> [docs_dir]
Exit code 1 with the list of failures; 2 if a directory is missing.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

from okf_links import ROOT, rewrite_relative_targets, site_url

# Top-level directories under docs/ that hold no content pages.
SKIP_TOP = {"assets", "overrides", "stylesheets"}
REQUIRED_ROOT_FILES = ["llms.txt", "llms-full.txt", "robots.txt", "sitemap.xml"]

failures: list[str] = []
warnings: list[str] = []


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
    if not m:
        return {}
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def dest_for(rel: Path, site: Path) -> Path:
    if rel.name == "index.md":
        return site / rel
    return site / rel.parent / rel.stem / "index.md"


def content_sources(docs: Path) -> list[Path]:
    return sorted(p for p in docs.rglob("*.md")
                  if p.relative_to(docs).parts[0] not in SKIP_TOP)


def check_root_files(site: Path):
    for name in REQUIRED_ROOT_FILES:
        f = site / name
        if not f.is_file():
            failures.append(f"missing {name} at the site root")
        elif f.stat().st_size == 0:
            failures.append(f"{name} is empty")
    robots = site / "robots.txt"
    if robots.is_file() and "llms.txt" not in robots.read_text(encoding="utf-8", errors="replace"):
        failures.append("robots.txt does not mention llms.txt (postbuild_agent_surface.py not run?)")


def check_mirrors(site: Path, docs: Path) -> int:
    base = site_url()
    sources = content_sources(docs)
    expected = {dest_for(p.relative_to(docs), site): p for p in sources}
    mirrors = {p for p in site.rglob("index.md")
               if p.relative_to(site).parts[0] not in SKIP_TOP}

    if len(mirrors) != len(sources):
        failures.append(f"{len(mirrors)} index.md mirror(s) in site/ but {len(sources)} "
                        f"content source(s) under docs/")
    for stray in sorted(mirrors - set(expected)):
        failures.append(f"stray mirror with no source: {stray.relative_to(site)}")

    checked = 0
    for dest, src in sorted(expected.items()):
        rel = src.relative_to(docs).as_posix()
        if not dest.is_file():
            failures.append(f"{rel}: no mirror at {dest.relative_to(site)}")
            continue
        want = rewrite_relative_targets(src.read_text(encoding="utf-8"), rel, base)
        if dest.read_text(encoding="utf-8") != want:
            failures.append(f"{rel}: mirror {dest.relative_to(site)} is not the source with its "
                            "relative links absolutized (scripts/okf_links.py)")
        page = dest.parent / "index.html"
        if not page.is_file():
            failures.append(f"{rel}: mirror present but no rendered {page.relative_to(site)}")
            continue
        text = page.read_text(encoding="utf-8", errors="replace")
        if 'rel="alternate" type="text/markdown"' not in text:
            failures.append(f"{rel}: {page.relative_to(site)} lacks the Markdown alternate link")
        if "View this page as Markdown" not in text:
            failures.append(f"{rel}: {page.relative_to(site)} lacks the visible Markdown button")
        if "course-machine-readable" not in text:
            failures.append(f"{rel}: {page.relative_to(site)} lacks the machine-readable line")
        if 'property="og:title"' not in text or 'property="og:image"' not in text:
            failures.append(f"{rel}: {page.relative_to(site)} lacks Open Graph tags")
        if "application/ld+json" not in text:
            failures.append(f"{rel}: {page.relative_to(site)} lacks a JSON-LD record")
        if frontmatter(src).get("type") and 'name="okf:type"' not in text:
            failures.append(f"{rel}: {page.relative_to(site)} lacks <meta name=\"okf:type\">")
        checked += 1
    return checked


def check_404(site: Path) -> None:
    """A dead URL should hand an agent somewhere to go, in HTML and in Markdown."""
    page = site / "404.html"
    if not page.is_file():
        failures.append("no 404.html in the build")
    else:
        text = page.read_text(encoding="utf-8")
        if "course-404-recovery" not in text:
            failures.append("404.html has no recovery body (postbuild_agent_surface.py adds it)")
        # A scanner reads the 404 body as text, so the recovery points must also be
        # there as literal Markdown, not only as HTML anchors.
        if "](" not in text or "llms.txt" not in text or "sitemap.xml" not in text:
            failures.append("404.html lacks a Markdown recovery block pointing at llms.txt "
                            "and sitemap.xml")
    md = site / "404.md"
    if not md.is_file():
        failures.append("no 404.md beside 404.html")
    elif "llms.txt" not in md.read_text(encoding="utf-8"):
        failures.append("404.md does not point at llms.txt")


def check_crawlable_html(site: Path) -> int:
    """What a crawler without JavaScript needs: one H1, real text, no meta refresh."""
    checked = 0
    for page in sorted(site.rglob("index.html")):
        if page.relative_to(site).parts[0] in SKIP_TOP:
            continue
        rel = page.relative_to(site).as_posix()
        text = page.read_text(encoding="utf-8", errors="replace")
        body = re.sub(r"(?s)<(script|style).*?</\1>", "", text)
        visible = " ".join(re.sub(r"<[^>]+>", " ", body).split())
        if len(visible) < 500:
            failures.append(f"{rel}: only {len(visible)} characters of server-rendered text "
                            "(agent crawlers run no JavaScript; 500 is the floor)")
        h1s = len(re.findall(r"<h1[ >]", text))
        if h1s != 1:
            failures.append(f"{rel}: {h1s} <h1> elements (exactly one is required)")
        head = text[:text.index("</head>")] if "</head>" in text else text
        if re.search(r'http-equiv=["\']?refresh', head, re.I):
            failures.append(f"{rel}: redirects with a meta refresh; serve the content or a real "
                            "301/302 at the canonical URL")
        checked += 1
    return checked


# A literal list marker at the start of a line inside a <p>. Matched on the raw
# HTML, so a paragraph that opens with a bold number ("<strong>1. The five
# solids.</strong>") does not count; ordered markers are one or two digits, so
# a wrapped line that happens to begin with a year ("1923. It resurfaced") does
# not count either.
SWALLOWED = re.compile(r"(?:^|\n)[ \t]*(?:[-*+]|\d{1,2}[.)])[ \t]+\S")


def check_swallowed_lists(site: Path) -> int:
    """A list that follows a paragraph without a blank line renders as text."""
    checked = 0
    for page in sorted(site.rglob("index.html")):
        if page.relative_to(site).parts[0] in SKIP_TOP:
            continue
        text = page.read_text(encoding="utf-8", errors="replace")
        for para in re.findall(r"<p>(.*?)</p>", text, re.S):
            if SWALLOWED.search(para):
                snippet = " ".join(re.sub(r"<[^>]+>", "", para).split())[:80]
                failures.append(f"{page.relative_to(site).as_posix()}: a list is folded into a "
                                f"paragraph (missing blank line in the source): \"{snippet}\"")
        checked += 1
    return checked


def check_llms_full(site: Path) -> None:
    """An agent ingesting llms-full.txt has no base to resolve a relative link against."""
    full = site / "llms-full.txt"
    if not full.is_file():
        return
    bad = re.findall(r"]\((\.\./[^)]*)\)", full.read_text(encoding="utf-8"))
    if bad:
        failures.append(f"llms-full.txt keeps {len(bad)} relative link(s), e.g. {bad[0]} — "
                        "gen_llms_txt.py should absolutize them")


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip().splitlines()[-2], file=sys.stderr)
        sys.exit(2)
    site = Path(sys.argv[1])
    docs = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "docs"
    for d, what in ((site, "site directory (run `zensical build` first)"),
                    (docs, "docs directory")):
        if not d.is_dir():
            print(f"error: {d} is not a directory — {what}", file=sys.stderr)
            sys.exit(2)

    check_root_files(site)
    check_404(site)
    check_llms_full(site)
    crawlable = check_crawlable_html(site)
    check_swallowed_lists(site)
    pages = check_mirrors(site, docs)

    for w in warnings:
        print(f"WARN  {w}")
    for f in failures:
        print(f"FAIL  {f}")
    print(f"\ncheck_site: {pages} mirrored page(s) verified, {crawlable} page(s) checked for "
          f"crawlable HTML: {len(failures)} failure(s), {len(warnings)} warning(s).")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
