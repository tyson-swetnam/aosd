---
title: "Superposed Filters"
description: "Stack polarizing filters, write down what you expect, then look: what happens when a third absorbing filter is slid between two crossed ones, and does the order of the filters matter?"
type: Activity
tags: [course, student-facing, problem, section-3, polarization, optics, malus-law, prediction]
status: stable
problem:
  section: 3
  session: 18
  identification: confident
  kind: puzzle
generated:
  by: "claude/opus-5"
  at: "2026-09-16T00:00:00Z"
sources:
  - id: winfree-handout-2002
    resource: "https://web.archive.org/web/20020420212713/http://eebweb.arizona.edu/Faculty/Winfree/handout_479.htm"
    title: "The Art of Scientific Discovery (ECOL 479/579): course handout, archived 20 April 2002"
    author: "Arthur T. Winfree"
  - id: hyperphysics-crossed-polarizers
    resource: "https://hyperphysics.gsu.edu/hbase/phyopt/polcross.html"
    title: "Crossed Polarizers / Polarizer Puzzle / Law of Malus (HyperPhysics)"
    author: "Rod Nave, Georgia State University"
  - id: malus-arcueil-1809
    resource: "https://archive.org/details/bub_gb_Nl87AAAAcAAJ_2"
    title: "Mémoires de Physique et de Chimie de la Société d'Arcueil, tome second (1809), containing Malus, 'Sur une propriété de la lumière réfléchie'"
    author: "Société d'Arcueil; memoir by Étienne-Louis Malus"
  - id: wikipedia-malus
    resource: "https://en.wikipedia.org/wiki/%C3%89tienne-Louis_Malus"
    title: "Étienne-Louis Malus"
    author: "Wikipedia contributors"
  - id: wikipedia-polarizer
    resource: "https://en.wikipedia.org/wiki/Polarizer"
    title: "Polarizer"
    author: "Wikipedia contributors"
  - id: wikipedia-polaroid-polarizer
    resource: "https://en.wikipedia.org/wiki/Polaroid_%28polarizer%29"
    title: "Polaroid (polarizer)"
    author: "Wikipedia contributors"
  - id: aosd-syllabus
    resource: "https://github.com/tyson-swetnam/aosd/blob/main/docs/assets/aosd_syllabus.pdf"
    title: "The Art of Scientific Discovery: original course syllabus (PDF)"
    author: "Arthur T. Winfree"
---

# Superposed Filters

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

*[Section 3](../section3.md), session 18. Discussed in the same session as [Cevians](cevians.md).*

!!! abstract "The problem"

    *Reconstructed from the syllabus and Winfree's handout. His own wording
    of the exercise is lost; the steps below are the editors' version.*

    You need two pieces of linear polarizing filter (the lenses of two pairs
    of polarized sunglasses, two photographic polarizers, or two squares of
    polarizing sheet) and, for the second half, a third piece. Before each
    step, write down your prediction.

    1. Look through one filter at the sky, a puddle's reflection or a
       laptop screen, and turn it. What changes?
    2. Lay the second filter on the first and slowly turn the top one through
       a full turn. How many times does the pair go dark, and why that
       number?
    3. Estimate the light getting through at 0, 30, 45, 60 and 90 degrees
       between the two axes. Propose a formula. What must it give at 0 and
       at 90 degrees?
    4. Set the pair at its darkest. Predict what happens if you slide a
       **third** filter between them, its axis at 45 degrees to both. Then
       do it.
    5. Put the third filter on top of the pair instead, or underneath. Does
       the order matter?
    6. Going further: stack many filters, each turned a little from the one
       below, so the first and last are at 90 degrees. What happens as the
       number grows?

    Keep the record of what you predicted, what you saw, and how far apart
    the two were.

## Why it is in the course

Section 3 is "Observations and Questions", and session 18 pairs this
exercise with [Cevians](cevians.md): one problem you reason out on paper, one
you have to look at. The syllabus says most exercises are made from
elementary mathematics, then adds: "There are some hands-on lab-type
exercises too."

The filters test a hidden assumption: that a filter only takes light away,
so more filters can only mean less light. Step 4 is built to check that
picture. The habit is the one the syllabus names in session 04: "distinguishing
things we know vs only imagine", and "facts before explanations of facts".
Write the prediction, then look, then measure the gap.

Step 2 adds a quieter lesson. The quantity that matters is an angle, a
variable that goes round a circle, the kind of cyclic variable Winfree spent
his career on.

## Where it comes from

In Winfree's handout, the link on "Superposed filters" points to a bookmark
named `Polaroids`. Several of his bookmarks name what a problem is about
rather than repeating its label (`Tictactoe_LoShu` for LoShu, `Sliced_Disk`
for "slice the disk"), so this one points to polarizing (Polaroid) sheets
rather than colour filters. The bookmark led into a companion document that was
never archived, so Winfree's own statement of the problem is lost.

Étienne-Louis Malus (1775–1812) discovered that reflected light is
polarized and published the finding in 1809 in the memoirs of the Société
d'Arcueil. The rule that a second polarizer passes a fraction cos²θ of
already-polarized light carries his name. Through the nineteenth century the effect
needed crystals such as Iceland spar. Polarizing sheet (first patented in 1929,
developed by Edwin Land from 1932, with his H-sheet following in 1938) put
it in anyone's pocket.
HyperPhysics poses the three-filter version as the "Polarizer Puzzle".

??? tip "Hints"

    - Count the dark positions in one full turn. Can the pair tell which face
      of a filter is up, or only the angle between the axes? How often must
      the pattern repeat?
    - Fix the formula's endpoints first: the same at 0 and 180 degrees,
      zero at 90. Then test candidates against your estimates.
    - A filter does more than remove light. What property does the light
      that got through now have? Is the second filter meeting the same light
      the first one met?
    - If moving the third filter to a different place in the stack changes
      the result, "each filter removes a fixed share" cannot be the whole
      story.

??? success "Resolution"

    ![Three stacks of polarizing filters. Two filters with parallel axes look bright; the same two crossed at right angles look black; inserting a third filter at 45 degrees between the crossed pair makes the stack dim but not black, passing about an eighth of the light. Below, a graph shows the light passed by two filters following cos squared of the angle between them, dark twice per full turn.](../assets/images/problems/superposed-filters.svg){ width="560" }

    *Drawn for this site (CC BY 4.0). Ideal filters; each is drawn face-on, with light passing up through the stack. Real sheet polarizers leak a little when crossed.*

    A sheet polarizer passes the part of the light's electric field along its
    axis and absorbs the rest, so unpolarized light loses about half its
    intensity at the first filter and leaves polarized.

    **Two filters.** The second filter meets polarized light and passes
    cos²θ of it (Malus's law), where θ is the angle between the axes: all
    of it at 0 degrees, none at 90. Because cos²θ repeats every 180 degrees,
    a full turn gives two bright and two dark positions.

    **Three filters.** Insert a filter at 45 degrees between a crossed pair.
    It passes cos²45° = 1/2 of what reaches it *and re-polarizes it at 45
    degrees*, so the last filter sees light 45 degrees from its axis instead
    of 90 and passes another half. That is 25% of the light leaving the first
    filter, about 12.5% of the original beam. On top of the pair or
    underneath it, the same filter leaves the stack black: order matters,
    because each filter both removes light and rewrites what is left.

    **The stack.** N filters above the first, each turned 90/N degrees, pass
    [cos²(90/N)]^N of the polarized light: 25% for N = 2, 78% for N = 10,
    97% for N = 90. Many small turns cost almost nothing.

## Sources

- **Arthur T. Winfree**, *The Art of Scientific Discovery (ECOL 479/579): course handout*, archived 20 April 2002; the session-18 link to the `Polaroids` bookmark — [Wayback Machine](https://web.archive.org/web/20020420212713/http://eebweb.arizona.edu/Faculty/Winfree/handout_479.htm){target=_blank} 🔓
- **Rod Nave**, "Crossed Polarizers" and "Polarizer Puzzle", *HyperPhysics*, Georgia State University — [hyperphysics.gsu.edu](https://hyperphysics.gsu.edu/hbase/phyopt/polcross.html){target=_blank} 🔓
- **Étienne-Louis Malus**, "Sur une propriété de la lumière réfléchie", *Mémoires de Physique et de Chimie de la Société d'Arcueil*, tome 2 (1809) — [Internet Archive](https://archive.org/details/bub_gb_Nl87AAAAcAAJ_2){target=_blank} 🔓
- **Wikipedia contributors**, "Étienne-Louis Malus" — [Wikipedia](https://en.wikipedia.org/wiki/%C3%89tienne-Louis_Malus){target=_blank} 🔓
- **Wikipedia contributors**, "Polarizer" — [Wikipedia](https://en.wikipedia.org/wiki/Polarizer){target=_blank} 🔓
- **Wikipedia contributors**, "Polaroid (polarizer)" — [Wikipedia](https://en.wikipedia.org/wiki/Polaroid_%28polarizer%29){target=_blank} 🔓
- **Arthur T. Winfree**, *The Art of Scientific Discovery*, original course syllabus — [PDF](https://github.com/tyson-swetnam/aosd/blob/main/docs/assets/aosd_syllabus.pdf){target=_blank} 🔓

---

*Back to [Section 3](../section3.md) · [All problems](index.md) · [The schedule](../syllabus.md#section-3-observations-and-questions)*
