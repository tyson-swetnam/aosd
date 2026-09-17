# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Start with AGENTS.md

`AGENTS.md` is the contract for this repository: what the `docs/` OKF v0.2 bundle is, the frontmatter every content page carries, which files are generated, and the checks CI enforces. Read it before touching anything under `docs/` or `scripts/`.

## Commands

```bash
uv venv --python 3.12 .venv                                   # system Python is too old
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/mkdocs serve                                        # live preview at http://localhost:8000
.venv/bin/python scripts/okf_validate.py docs                 # OKF conformance (CI)
.venv/bin/python scripts/gen_llms_txt.py                      # regenerate llms.txt indexes (CI checks drift)
.venv/bin/mkdocs build --clean --strict                       # static site -> site/
.venv/bin/python scripts/postbuild_agent_surface.py site      # after build: md mirror + okf meta + robots.txt
.venv/bin/python scripts/check_site.py site                   # post-build assertions (CI)
```

Before committing content: `okf_validate.py`, `gen_llms_txt.py`, a strict build with the post-build step and `check_site.py`, and a dated entry in `docs/log.md`. Never write a `verified:` key.
