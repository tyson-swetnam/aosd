#!/usr/bin/env python3
"""Shared helpers for the scripts that publish Markdown for agents.

* `mkdocs_config()` reads mkdocs.yml with a loader that tolerates the
  `!!python/name:` tags Material's extensions use, so `site_url`, `repo_url`,
  `edit_uri` and `nav` are available to every script.
* `rewrite_relative_targets()` rewrites the relative links in a Markdown page
  to absolute URLs. `postbuild_agent_surface.py` mirrors every page at its
  pretty URL (`docs/a.md` -> `site/a/index.md`), one directory deeper than the
  source, so a relative link copied verbatim would resolve one level too low;
  `gen_llms_txt.py` concatenates every page into `llms-full.txt`, where a
  relative link has no base to resolve against at all.

A link to another **page** resolves to that page's Markdown twin (the page
URL plus `index.md`), so an agent reading Markdown keeps getting Markdown as
it traverses; drop the trailing `index.md` to reach the rendered page. Links
to files served verbatim (`assets/`) resolve to the file itself, and anchors,
external URLs, `mailto:`, fragment-only links and paths that are already
absolute are left alone. The sources under `docs/` are never modified.

Adapted from tyson-swetnam/AI-Automation-and-Agents (scripts/okf_links.py).
"""

from __future__ import annotations

import posixpath
import re
from functools import lru_cache
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "mkdocs.yml"

# Markdown inline link or image: the target sits between "](" and ")". Only the
# tail is matched, so a link whose text wraps onto an earlier line still counts.
MD_TARGET = re.compile(r"(\]\()([^)\s]+)(\s+\"[^\"]*\")?(\))")
# Raw HTML attribute, for pages that embed an image, iframe or object.
HTML_TARGET = re.compile(r"""\b(src|href)=(["'])([^"'>]+)\2""")
SKIP_PREFIXES = ("http://", "https://", "//", "mailto:", "tel:", "#", "/", "data:")


class _TolerantLoader(yaml.SafeLoader):
    """SafeLoader that turns any unknown tag (e.g. !!python/name:...) into None."""


def _unknown(loader, suffix, node):
    return None


_TolerantLoader.add_multi_constructor("tag:yaml.org,2002:python/", _unknown)
_TolerantLoader.add_multi_constructor("!", _unknown)


@lru_cache(maxsize=1)
def mkdocs_config() -> dict:
    data = yaml.load(CONFIG.read_text(encoding="utf-8"), Loader=_TolerantLoader)
    return data if isinstance(data, dict) else {}


def site_url() -> str:
    """The site_url from mkdocs.yml, with a trailing slash."""
    return str(mkdocs_config().get("site_url") or "/").rstrip("/") + "/"


def raw_source_url(rel: str = "") -> str:
    """raw.githubusercontent.com URL of a docs-relative path ("" if repo_url is unset).

    The branch comes from edit_uri ("edit/<branch>/docs/"), so the page URL, the
    Markdown twin and the raw source stay in step if the repository moves.
    """
    cfg = mkdocs_config()
    repo = str(cfg.get("repo_url") or "")
    if "github.com/" not in repo:
        return ""
    slug = repo.rstrip("/").split("github.com/")[-1]
    parts = str(cfg.get("edit_uri") or "").strip("/").split("/")
    branch = parts[1] if len(parts) > 1 else "main"
    return f"https://raw.githubusercontent.com/{slug}/{branch}/docs/{rel}"


def page_url(base: str, rel: str) -> str:
    """The rendered (use_directory_urls) URL of a docs-relative Markdown path."""
    if rel == "index.md":
        return base
    if rel.endswith("/index.md"):
        return base + rel[: -len("index.md")]
    return base + rel[: -len(".md")] + "/"


def twin_url(base: str, rel: str) -> str:
    """The Markdown twin of a docs-relative Markdown path."""
    return page_url(base, rel) + "index.md"


def absolutize(target: str, source_rel: str, base: str) -> str:
    """Resolve one relative target found in `source_rel` to an absolute URL."""
    if not target or target.startswith(SKIP_PREFIXES):
        return target
    path, sep, anchor = target.partition("#")
    if not path:
        return target
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source_rel), path))
    if resolved.startswith(".."):  # escapes docs/; leave it alone
        return target
    url = twin_url(base, resolved) if resolved.endswith(".md") else base + resolved
    return url + sep + anchor


def rewrite_relative_targets(text: str, source_rel: str | Path, base: str) -> str:
    """Return `text` with every relative Markdown and HTML target made absolute.

    `source_rel` is the page's path relative to docs/ (e.g. `section1.md`), `base`
    the site URL with a trailing slash. Fenced code blocks are left untouched, so
    example paths inside them still read as written.
    """
    source_rel = str(source_rel)

    def md(m: re.Match) -> str:
        return m.group(1) + absolutize(m.group(2), source_rel, base) + (m.group(3) or "") + m.group(4)

    def attr(m: re.Match) -> str:
        return f'{m.group(1)}={m.group(2)}{absolutize(m.group(3), source_rel, base)}{m.group(2)}'

    out, fence = [], None
    for line in text.split("\n"):
        stripped = line.lstrip()
        if fence is None and (stripped.startswith("```") or stripped.startswith("~~~")):
            fence = stripped[:3]
        elif fence is not None and stripped.startswith(fence):
            fence = None
        elif fence is None:
            line = MD_TARGET.sub(md, line)
            line = HTML_TARGET.sub(attr, line)
        out.append(line)
    return "\n".join(out)
