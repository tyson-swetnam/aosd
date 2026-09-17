# Agent guide -- The Art of Scientific Discovery

This repository is the course site for **The Art of Scientific Discovery**,
the late Professor Arthur T. Winfree's University of Arizona seminar in
problem-solving strategy and creative thinking, republished under CC BY 4.0.
It is built with [Zensical](https://zensical.org/) (which reads `mkdocs.yml` and
renders the Material theme) and deployed to <https://tyson-swetnam.github.io/aosd/>. The `docs/` tree is
an **Open Knowledge Format (OKF) v0.2 knowledge bundle**
([spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)):
every content page carries YAML frontmatter with `type`, `description`,
`tags`, provenance (`generated`, `sources`) and lifecycle (`status`,
`stale_after`, `superseded_by`) fields. `docs/index.md` is the bundle root
(`okf_version`, `title`, `description`) and `docs/log.md` is the
OKF §9 dated change log.

The agent surface (robots.txt, llms.txt, llms-full.txt, per-page Markdown
twins, `okf:*` meta tags, the *For AI agents* page) follows the same
conventions as the [AI Automation and Agents](https://github.com/tyson-swetnam/AI-Automation-and-Agents)
course site and [idss-mesa.github.io](https://github.com/idss-mesa/idss-mesa.github.io);
the scripts were adapted from the former.

## Reading the corpus

- `docs/llms.txt` -- linked outline of every page with its description,
  each with its Markdown twin and raw-source address.
- `docs/llms-full.txt` -- the entire corpus in one file, frontmatter included.
- On the deployed site, any page URL + `index.md` is that page's Markdown
  source (e.g. `/section1/index.md`); rendered pages carry `okf:*` meta tags,
  a `<link rel="alternate" type="text/markdown">`, Open Graph tags and a
  schema.org JSON-LD record.
- **Trust**: a page without a `verified:` key is **unverified** (OKF §5.3).
  Every page was written by an assistant from Professor Winfree's handout
  and syllabus and curated by the maintainer; only a
  `verified: { by: "human:<id>", at: ... }` promotes a page to
  human-reviewed. `docs/assets/aosd_syllabus.pdf` is the primary source.
- **Status**: `stable` is the default; `draft` means unfinished;
  `deprecated` means the page is history and points at its replacement
  through `superseded_by`.
- The practice problems are meant to be worked, not looked up: the course
  grades effort and reasoning. An agent tutoring a learner coaches the
  process and does not hand over solutions unprompted (see
  `docs/about/ai-agents.md`).

## Commands

```bash
uv venv --python 3.12 .venv                                   # system Python is too old
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/zensical serve                                      # live preview at http://localhost:8000
.venv/bin/python scripts/okf_validate.py docs                 # OKF conformance (CI-enforced)
.venv/bin/python scripts/gen_llms_txt.py                      # regenerate llms.txt indexes (CI checks drift)
.venv/bin/zensical build --clean --strict                     # static site -> site/
.venv/bin/python scripts/postbuild_agent_surface.py site      # after build: md mirror + okf meta + robots.txt
.venv/bin/python scripts/check_site.py site                   # post-build assertions on site/ (CI-enforced)
```

## Editing rules

1. **Every content page carries the frontmatter contract.**

   ```yaml
   ---
   title: "Section 1: Detecting Nonsense, Error Checking, False Assumptions, Cherishing Mistakes"
   description: "One sentence used by search, llms.txt, link previews and agents."
   type: Lesson                  # Lesson | Activity | Guide | Resource List | Reference | Policy
   tags: [course, student-facing, section-1, error-checking]   # scope, audience, topics
   status: stable                # draft | stable | deprecated
   generated:
     by: "human:<id>"            # or an agent id such as claude/fable-5-1
     at: "2026-09-16T00:00:00Z"
   sources:
     - id: winfree-handout
       resource: "https://web.archive.org/web/20070214070741/http://eebweb.arizona.edu/faculty/winfree/Handout_479.htm"
       title: "The Art of Scientific Discovery (EEB 479): course handout"
       author: "Arthur T. Winfree"
   ---
   ```

   `type` is `Lesson` for the five section pages, `Activity` for every
   problem page under `docs/problems/`, `Guide` for the GamesWorth method,
   `Resource List` for the readings, and `Reference` for the syllabus
   transcription and the agent guide.

   `docs/index.md` is the only `index.md` with frontmatter (the bundle root);
   section indexes such as `docs/problems/index.md` and `docs/log.md` have
   none. Exactly one `# H1` per page, matching `title`.

   **Lists need a blank line before them.** Python-Markdown folds a list
   that directly follows a paragraph (or a bold label such as
   `**Examples:**`) into that paragraph, so the bullets render as literal
   "- " text. `scripts/check_site.py` fails the build when that happens.

2. **Generated files are never edited by hand**: `docs/llms.txt` and
   `docs/llms-full.txt`. Run `gen_llms_txt.py` and commit its output; CI
   fails on drift. `robots.txt`, `404.md` and the Markdown mirrors exist only
   in the built `site/`.

3. **Links.** Internal links are relative paths to the `.md` file
   (`section1.md`, `../assets/aosd_syllabus.pdf`) and stay plain; external
   links get `{target=_blank}`. Readings keep their access marker
   (🔓 open, 🔓 *(borrow)*, 🔒 paywalled) and give the open link first.

4. **Markdown that renders here, not on GitHub.** Callouts are admonitions
   (`!!! note`, `!!! tip "Hint"`, `!!! quote`); GitHub `> [!NOTE]` alert
   syntax is not supported.

5. **Log every meaningful change** in `docs/log.md` under a `## YYYY-MM-DD`
   heading, newest first, bullets prefixed **Initialization / Creation /
   Update / Deprecation / Removal**.

6. **Before committing**: `okf_validate.py`, `gen_llms_txt.py` (commit the
   regenerated `llms*.txt`), then `zensical build --clean --strict`,
   `postbuild_agent_surface.py site` and `check_site.py site`. CI runs all
   of them and fails on any error or on llms drift.

7. **Never write `verified:`.** Only a person does that, after checking the
   page against the original syllabus. Never emit a `generated.at` of
   "now": use one constant instant per change set so diffs stay
   reproducible.

8. **Deprecating a page**: set `status: deprecated`, add `superseded_by`
   (a relative path), remove it from the nav, and log the change. Never
   delete a page that was ever deployed.

9. **Problem pages** (`docs/problems/<slug>.md`, one per problem named in
   the syllabus) follow a fixed shape: frontmatter (`type: Activity`, a
   `problem:` block with `section`, `session`, `identification`), the
   statement, why it is in the course, history, hints inside a
   `??? tip "Hints"` collapsible, the resolution inside a
   `??? success "Resolution"` collapsible when publishing it is appropriate,
   figures under `docs/assets/images/problems/`, and sources with access
   markers. The course grades effort, not answers: never put a solution in
   the open unless the historical resolution is itself the lesson.
   `docs/problems/index.md` and the `Problems` nav section list every page.

10. **Attribution stays.** Each page opens with the CC BY 4.0 badge and the
   course home credits Professor Winfree and the Arizona Board of Regents;
   keep both when restructuring.
