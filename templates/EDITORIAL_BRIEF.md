# Editorial brief for the course pages

The site republishes Professor Arthur T. Winfree's course "The Art of
Scientific Discovery" (University of Arizona, EEB 479/479H/579, 2001). The
primary source is his syllabus, transcribed in full at `docs/syllabus.md`
(PDF at `docs/assets/aosd_syllabus.pdf`). Every factual claim about the
course must trace to it; every quotation attributed to Winfree must appear
verbatim in it. Do not invent Winfree quotations, session content, grading
rules, or problem statements.

## Voice and clarity

- Write for a first-year undergraduate who has never heard of the course.
  Short paragraphs, concrete sentences, one idea per sentence.
- Winfree's own words carry the philosophy; use them (quoted, attributed)
  rather than paraphrasing them into generic self-help language.
- Cut boilerplate. Earlier drafts repeated "Skills Being Developed",
  "Assessment Focus", "Practical Skills Developed" on every page in nearly
  identical words. Assessment is described once, on the GamesWorth page and
  the syllabus page. A section page describes what that section does.
- Prefer the specific to the generic: name the problem, the reading, the
  session. "Practice exercises: Weird Organism, Rearranged Triangle" beats
  "various practice exercises".
- Do not editorialize about Winfree's intentions beyond what the syllabus
  says. "The syllabus pairs this with..." is fine; "Winfree believed..."
  needs a quotation.

## Structure of a section page

1. Frontmatter (keep the existing keys; update `description` if the page
   changed substantially).
2. `# Title` matching the frontmatter title, the CC BY badge line, and the
   italic one-line tagline.
3. **Overview**: what the section trains, in Winfree's framing, two or
   three paragraphs.
4. **The sessions**: one `###` heading per session in this section
   (`### Session 07: Perceptual blocks` style: number then a short label
   drawn from the syllabus), each with the readings due and the problems,
   every problem linked to its page under `problems/`. Keep the syllabus's
   own phrasing for the activity where it is distinctive ("facts before
   explanations of facts", "like a jig-saw puzzle of cross-checks").
5. **Key ideas**: the conceptual content worth keeping from the earlier
   draft (for Section 2, the four kinds of block from Adams; for Section 5,
   multiple working hypotheses and strong inference), tightened.
6. **GamesWorth focus for this section**: a short list of what to practise
   in the daily notebook, specific to the section's problems.
7. **Readings for this section**: the readings the syllabus assigns in
   these sessions, each linked to its entry on the readings page
   (`readings.md#anchor`) or to the source, with the access marker.
8. **Problems in this section**: a table (Session, Problem, Kind, What it
   trains) linking every problem page.
9. Closing italic line (keep the existing one if it is good).

The five section pages must be parallel in structure so a reader can
predict where things are.

## Markdown rules (Python-Markdown / Material for MkDocs)

- A list must be preceded by a blank line. `**Examples:**` on one line and
  `- item` on the next renders as a single paragraph with a literal "- ".
- Admonitions: `!!! note "Title"` then a blank line then content indented
  four spaces. Collapsibles: `??? tip "Hints"` (closed) or `???+` (open).
- Exactly one `# H1` per page. Headings in order, no skipped levels.
- Internal links are relative paths to `.md` files
  (`problems/seven-bridges.md`, `../section3.md`); external links get
  `{target=_blank}` and an access marker for readings: 🔓 open, 🔓
  *(borrow)* Internet Archive lending, 🔒 paywalled.
- Images: `![alt](../assets/images/problems/name.svg){ width="560" }` with
  a caption line in italics below; alt text required.
- Tables need a header row and a `| :-- |` separator row; no blank lines
  inside a table.
- No raw HTML except the CC BY badge line and `<br>` inside table cells.
- No emoji except the access markers.
- Straight quotes and apostrophes are fine; use `—` sparingly.

## Problem pages

Follow `templates/problem.md` exactly in shape. Everything factual comes
from the verified research record; where the record says
`identification: unknown`, the page says so plainly and offers the
candidate interpretations rather than pretending. The course grades effort,
not answers: hints and resolutions live in collapsibles unless the
historical resolution is the lesson (`reveal_policy: open`), in which case
use an open `## What happened` section. Never publish a resolution when
`reveal_policy` is `none`.
