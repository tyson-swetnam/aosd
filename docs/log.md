# Course update log

Dated history of changes to this knowledge bundle (OKF §9), newest first.
Bullets are prefixed **Initialization / Creation / Update / Deprecation /
Removal**.

## 2026-09-17

- **Creation**: one page per problem named in Professor Winfree's schedule,
  55 in all, under [Problems](problems/index.md). Each gives the statement,
  why it is in the course, where it comes from, hints and a resolution
  folded away, figures, and sources with access markers. Pages say plainly
  when the editors could not be sure which problem Winfree assigned
  (`problem.identification`), and label reconstructions as such.
- **Creation**: [the original syllabus](syllabus.md) transcribed in full,
  with a session-by-session schedule linking every problem page;
  `scripts/gen_problem_index.py` builds the problem index and its navigation
  block from page frontmatter (CI checks it is current).
- **Creation**: figures for the problems under `assets/images/problems/`:
  diagrams drawn for this site (CC BY 4.0) and public-domain, CC0 or CC BY
  images from Wikimedia Commons, Project Gutenberg and the Library of
  Congress, each captioned with its source and licence.
- **Update**: identifications draw on Winfree's own archived web pages (his
  2001-02 "Adventures in Discovery" columns identify Rainbow Moon) and on
  the bookmark names inside his archived course handout, which point at a
  companion problem document that does not survive (for example, Paired
  Observations links to `Keplers_Laws`, LoShu to `Tictactoe_LoShu`).
- **Update**: editorial rewrite of the home, section, GamesWorth and readings
  pages: parallel section structure (overview, sessions, key ideas,
  GamesWorth focus, readings, problems table), quotations checked against
  the syllabus, repeated boilerplate removed, lists that were folded into
  paragraphs fixed, and external links checked (access markers, years and
  addresses corrected where they were wrong).
- **Update**: `scripts/check_site.py` fails the build when a list is folded
  into a paragraph.
- **Update**: consistency pass across the home, section, readings,
  GamesWorth, syllabus and problem-index pages. Each problem now appears in
  exactly one section's problem table (Pedestrian Crosswalk Mystery under
  Section 3, Stacked Cantilevers Lab under Section 5; the sections where
  they begin still mention them). Problem names match each page's title
  everywhere, including the syllabus schedule's link text. The section
  navigation labels and the problem index use the full section titles.
  Every session now opens with a "Readings due" line, readings lists share
  one format and link their reading-list entries, and Ehrlich's chapter
  titles for sessions 16 to 18 were added (checked against Crossref).
- **Update**: the syllabus transcription now keeps two lines exactly as
  printed: the "Spring break" line after session 17 and the final-exam line
  with its unfilled date. Quotations of the syllabus on problem pages were
  checked against the PDF, and an Internet Archive copy of Ehrlich's book is
  marked as available to print-disabled readers only.

- **Update**: CI follows [UNM-CARC/docs](https://github.com/UNM-CARC/docs).
  `.github/workflows/docs.yml` has the same `okf-conformance` job (the
  reference OKF validator, shared with idss-mesa.github.io, plus the
  `llms.txt` drift check) and the same `deploy` job (Zensical build, agent
  surface, `actions/deploy-pages`). This site adds a problem-index drift
  check, a trial build on pull requests, `--strict` and `check_site.py`.
  The site now builds with Zensical, which reads `mkdocs.yml`; the root
  `index.md` no longer carries a `license` key, which the reference
  validator does not expect (the licence stays in the page badge and the
  JSON-LD).

## 2026-09-16

- **Initialization**: made the site an Open Knowledge Format (OKF v0.2)
  bundle with the same agent surface as the *AI Automation and Agents*
  course site. Every content page now carries frontmatter (`title`,
  `description`, `type`, `tags`, `status`, `generated`, `sources`); the
  root `index.md` declares `okf_version`.
- **Creation**: `scripts/gen_llms_txt.py` writes `llms.txt` (linked outline
  with Markdown-twin and raw-source addresses) and `llms-full.txt` (the whole
  corpus); `scripts/postbuild_agent_surface.py` mirrors every page's Markdown
  at its URL plus `index.md`, injects `okf:*` meta tags, Open Graph tags and
  schema.org JSON-LD, adds a Markdown button and a machine-readable line to
  every page, gives the 404 page recovery links, and writes `robots.txt`;
  `scripts/okf_validate.py` and `scripts/check_site.py` enforce the contract
  in CI.
- **Creation**: the [For AI agents](about/ai-agents.md) page and this log,
  under *About* in the navigation; `AGENTS.md` and `CLAUDE.md` at the
  repository root for coding agents.
- **Update**: the GitHub Actions workflow now validates the bundle, builds
  with `mkdocs build --strict`, runs the post-build step and its checks, and
  deploys with `actions/deploy-pages` instead of `mkdocs gh-deploy`.
- **Update**: corrected `site_url` and `repo_url` in `mkdocs.yml` to the
  `tyson-swetnam` account, enabled the *Edit this page* and *View source*
  buttons, removed the unused `mkdocstrings` and `mkdocs-jupyter` plugins and
  the missing chatbot widget references, and trimmed `requirements.txt` to
  the build dependencies.
- **Update**: favicon changed to the University of New Mexico icon used by
  the *AI Automation and Agents* site (`assets/unm.ico`).
