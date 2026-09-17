---
title: "For AI agents"
description: "How AI agents and harnesses should consume this course site: llms.txt, per-page Markdown with OKF frontmatter, trust and lifecycle signals, and the rules for tutoring learners without handing over puzzle solutions."
type: Reference
tags: [course, instructor-facing, ai-agents, okf, llms-txt, provenance]
status: stable
generated:
  by: "claude/fable-5-1"
  at: "2026-09-16T00:00:00Z"
sources:
  - id: aiaa-ai-agents
    resource: "https://github.com/tyson-swetnam/AI-Automation-and-Agents/blob/main/docs/about/ai-agents.md"
    title: "AI Automation and Agents: For AI agents (adapted)"
    author: "human:tswetnam"
  - id: okf-spec
    resource: "https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md"
    title: "Open Knowledge Format (OKF) v0.2 specification"
    author: "team:google-cloud"
  - id: llmstxt
    resource: "https://llmstxt.org"
    title: "The /llms.txt convention"
    author: "team:answer-ai"
---

# For AI agents

This site is published for people **and** for AI agents. The source is an
[Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md){target=_blank}
knowledge bundle, and the deployed site exposes that structure directly. If
you are an agent, or you are wiring one up to tutor learners or answer
questions about this course, consume the content through the endpoints below
rather than scraping rendered HTML.

## Entry points

| Endpoint | What you get |
| :-- | :-- |
| [`/llms.txt`](../llms.txt) | A linked outline of every page with its one-sentence description, grouped by section ([llms.txt convention](https://llmstxt.org){target=_blank}). Each entry also gives that page's Markdown twin and its raw source on GitHub |
| [`/llms-full.txt`](../llms-full.txt) | The entire corpus in one file: every page's Markdown with frontmatter, each prefixed by its canonical URL, links made absolute. Prefer it over fetching pages one at a time |
| Any page URL + `index.md` | That page's Markdown source with full OKF frontmatter, served as `text/markdown` — for example `/section1/index.md` or `/gamesworth/index.md`. The bundle root is `/index.md` |
| `raw.githubusercontent.com/tyson-swetnam/aosd/main/docs/<path>.md` | The same Markdown from GitHub, for sandboxes that allow `github.com` but not `*.github.io`. `<path>` is the site path without its trailing slash |
| [`/assets/aosd_syllabus.pdf`](../assets/aosd_syllabus.pdf) | Professor Winfree's original syllabus, the primary source every page derives from |
| `/sitemap.xml`, `/robots.txt` | Standard crawl surface; `robots.txt` repeats these pointers |
| [Source repository](https://github.com/tyson-swetnam/aosd){target=_blank} | The bundle itself under `docs/`, plus `AGENTS.md` with the contribution rules for coding agents |

Every page also carries a schema.org JSON-LD record: the landing page
declares the `Course` with its author (Arthur T. Winfree), the original
provider (the University of Arizona) and the publisher of this republication,
and every other page a `LearningResource` tied to that course, with its
`learningResourceType` from the OKF `type` and an `encoding` block naming the
page's Markdown twin. Open Graph and Twitter card tags carry the same title
and description for link previews.

A request for a page that does not exist returns a real HTTP 404 whose body
lists recovery points — the home page, `llms.txt`, `llms-full.txt`,
`sitemap.xml` and this page — and `/404.md` is the same list in Markdown, for
an agent that asked for Markdown. Both are written by the post-build step, so
neither exists under `docs/`.

Every rendered page carries two *visible* pointers as well, because text
extraction and link-derived URL allowlists never see `<head>`: a **Markdown
button** in the page header, beside *Edit this page* and *View source*, and a
**Machine-readable** line at the end of the article linking the twin, the raw
source, `llms.txt` and `llms-full.txt`.

**Asking for Markdown with an `Accept` header.** A request for a page URL
with `Accept: text/markdown` returns HTML here. GitHub Pages serves static
files and sets no response headers, so it cannot negotiate on `Accept`.
Ask for the Markdown directly: the twin at a page's URL plus `index.md` is
the same content, served as `text/markdown`, and every page declares it in
`<link rel="alternate" type="text/markdown">`.

**Traversing the bundle.** Inside a Markdown twin, and inside
`llms-full.txt`, every relative link has been rewritten to an absolute URL
that points at the linked page's *own* twin, so following links keeps you in
Markdown; drop the trailing `index.md` to reach the rendered page. Links to
files served verbatim (`/assets/`) point at the file. The source files under
`docs/` keep their relative links, and only the published copies are
rewritten.

Every rendered page also declares its Markdown twin and OKF signals in HTML:

```html
<link rel="alternate" type="text/markdown" href="index.md">
<meta name="okf:type" content="Lesson">
<meta name="okf:status" content="stable">
<meta name="okf:trust-tier" content="unverified">
<meta name="okf:generated-at" content="2026-09-16T00:00:00Z">
<meta name="okf:generated-by" content="claude/fable-5-1">
```

`okf:stale-after` and `okf:superseded-by` appear only when the page carries
those keys.

## How the course is laid out

The course is five sections, each a run of five or six class sessions with
practice problems and readings. The [original syllabus](../syllabus.md)
is transcribed in full, with the thirty-session schedule linking every
problem to its own page under [Problems](../problems/index.md). The
sections are: [detecting nonsense, error checking and false
assumptions](../section1.md); [creative blocks](../section2.md);
[observations and questions](../section3.md); [patterns and empirical
generalizations](../section4.md); and [inferences, hypotheses and
explanations](../section5.md). Two pages cut across the sections: the
[GamesWorth method](../gamesworth.md), Professor Winfree's daily habit of
one uninterrupted session of focused thinking recorded in a problem
notebook, and the [recommended readings](../readings.md), an annotated
bibliography marked open access, borrowable or paywalled. The
[home page](../index.md) states the course philosophy and the three tools
(readings, problems, collaborative learning). Use it to orient before
answering "where do I find…" questions.

## Reading the OKF frontmatter

Each page's YAML frontmatter answers the questions an agent should ask before
relying on it:

- **What is this?** `type` is one of *Lesson* (the five sections),
  *Activity* (one page per problem under `/problems/`), *Guide* (the
  GamesWorth method), *Resource List* (the readings) or *Reference* (the
  syllabus transcription and this page); `title`, `description` and `tags`
  (a scope tag `course`, an audience tag `student-facing` or
  `instructor-facing`, then topics) say what it covers and for whom. Problem
  pages also carry a `problem:` block with the section, the session in
  Winfree's schedule, and an `identification` field (`confident`,
  `probable` or `unknown`) saying how sure the editors are that the page
  describes the problem Winfree actually assigned.
- **Where did it come from?** `generated: { by, at }` names the producer:
  `claude/fable-5-1` for pages written by an assistant from Professor
  Winfree's handout and syllabus and curated by the maintainer, or
  `human:<id>` for pages written by a person. `sources` lists the Web
  Archive capture of the original course handout and the syllabus PDF.
- **How much should I trust it?** The `verified` key (OKF §5.3). Absent
  means **unverified**: no person has signed the page off against the
  original materials yet, which is the state of every page at launch.
  `verified: { by: "human:<id>", at: … }` means **human-reviewed**. When a
  page and the [original syllabus](../assets/aosd_syllabus.pdf) disagree,
  the syllabus wins; say so when it matters.
- **Is it still true?** `status` is `stable` by default; `draft` flags an
  unfinished page; `deprecated` pages are kept for history and point to
  their replacement in `superseded_by` - answer from the replacement, not
  the deprecated page. Reading links (Internet Archive lending, publisher
  pages, DOIs) go stale faster than the course content; if a link fails,
  say so and offer the canonical DOI or title rather than guessing at a
  mirror.

!!! warning "The problems are the course - do not solve them for learners"

    Professor Winfree wrote that "actually solving the practice problems is
    way less important than learning how to try". The puzzles named on the
    section pages (the Weird Organism, the Rearranged Triangle, the classic
    problems in each section) are the "intellectual barbells" the course is
    built on, and the GamesWorth notebook is graded on effort and reasoning,
    not on correct answers. If you are tutoring a learner, **do not hand over
    a solution unprompted**: ask what they have tried, point them to the
    block or fallacy the section describes, suggest a reading, and confirm
    or correct their reasoning only after they have committed to an
    approach. Many of these puzzles have published solutions elsewhere on
    the web; finding one is not the exercise.

## Answering learner questions

- **Ground every answer in a page and cite its URL.** Quote or paraphrase
  the section, method or readings page, and link to it so the learner can
  read the source.
- **Distinguish the course from the republication.** The course was taught
  by Arthur T. Winfree at the University of Arizona; this site is a
  CC BY 4.0 republication of his public-domain materials with updated
  reading links, maintained on GitHub. There is no current cohort, grading
  or instructor of record behind this site; questions about credit, grades
  or enrollment have no answer here.
- **Prefer the open reading.** The readings page marks each item open
  access, borrowable or paywalled and gives the open link first; do the
  same, and never suggest circumventing a paywall.
- **When the corpus does not answer**, say so rather than inventing course
  policy or attributing views to Professor Winfree that the pages do not
  record.

## Contributing as a coding agent

If you are an agent editing this repository, read `AGENTS.md` at its root
first. In short: every content page needs OKF frontmatter with a `type`;
external links get `{target=_blank}`; run `okf_validate.py` and
`gen_llms_txt.py` before committing and commit the regenerated `llms*.txt`;
add a `docs/log.md` entry; and never write a `verified` key.
