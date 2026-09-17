---
title: "Bacterial Hybrids"
description: "Two strains that cannot grow alone give colonies when mixed: list every explanation, read the linkage hidden in a table of colony counts, and design the experiment that kills the rival. An editors' reconstruction; Winfree's own problem sheet is lost."
type: Activity
tags: [course, student-facing, problem, section-5, genetics, bacteria, multiple-working-hypotheses, linkage]
status: stable
problem:
  section: 5
  session: 30
  identification: probable
  kind: puzzle
generated:
  by: "claude/opus-5"
  at: "2026-09-16T00:00:00Z"
sources:
  - id: winfree-handout-2002
    resource: "https://web.archive.org/web/20020420212713/http://eebweb.arizona.edu/Faculty/Winfree/handout_479.htm"
    title: "The Art of Scientific Discovery (ECOL 479/579): course handout, archived 20 April 2002"
    author: "Arthur T. Winfree"
  - id: lederberg-tatum-1946
    resource: "https://doi.org/10.1038/158558a0"
    title: "Gene Recombination in Escherichia coli"
    author: "Joshua Lederberg and Edward L. Tatum"
  - id: tatum-lederberg-1947
    resource: "https://pmc.ncbi.nlm.nih.gov/articles/PMC518375/"
    title: "Gene Recombination in the Bacterium Escherichia coli"
    author: "Edward L. Tatum and Joshua Lederberg"
  - id: lederberg-1947
    resource: "https://pmc.ncbi.nlm.nih.gov/articles/PMC1209393/"
    title: "Gene Recombination and Linked Segregations in Escherichia Coli"
    author: "Joshua Lederberg"
  - id: davis-1950
    resource: "https://pmc.ncbi.nlm.nih.gov/articles/PMC385908/"
    title: "Nonfiltrability of the Agents of Genetic Recombination in Escherichia coli"
    author: "Bernard D. Davis"
  - id: hayes-1953
    resource: "https://doi.org/10.1099/00221287-8-1-72"
    title: "Observations on a Transmissible Agent Determining Sexual Differentiation in Bacterium coli"
    author: "William Hayes"
  - id: wollman-jacob-hayes-1956
    resource: "https://doi.org/10.1101/sqb.1956.021.01.012"
    title: "Conjugation and Genetic Recombination in Escherichia coli K-12"
    author: "Élie L. Wollman, François Jacob and William Hayes"
  - id: lederberg-1996
    resource: "https://pmc.ncbi.nlm.nih.gov/articles/PMC1207540/"
    title: "Genetic Recombination in Escherichia coli: Disputation at Cold Spring Harbor, 1946–1996"
    author: "Joshua Lederberg"
  - id: almquist-1924
    resource: "https://doi.org/10.1093/infdis/35.4.341"
    title: "Investigations on Bacterial Hybrids"
    author: "E. Almquist"
  - id: aosd-syllabus
    resource: "https://github.com/tyson-swetnam/aosd/blob/main/docs/assets/aosd_syllabus.pdf"
    title: "The Art of Scientific Discovery: original course syllabus (PDF)"
    author: "Arthur T. Winfree"
---

# Bacterial Hybrids

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

*[Section 5](../section5.md), session 30, the last session in the schedule. The reading for the day is Judson, Chapter 9: Theory.*

!!! abstract "The problem"

    This statement is the editors' reconstruction. Winfree's own problem
    sheet does not survive (see the note at the foot of the page). The
    numbers were made up for this page; they are not anyone's lab data.

    Two strains of a microbe, **A** and **B**, cannot grow on a bare
    nutrient plate. Strain A cannot make two substances it needs; strain B
    cannot make two different ones. Each strain also carries two traits you
    can read from a colony: **Lac**, whether it ferments lactose (Lac+) or
    not (Lac−), and **Vir**, whether it resists (Virʳ) or is killed by
    (Virˢ) a certain virus.

    | | needs | Lac | Vir |
    | :-- | :-- | :-- | :-- |
    | strain A | substances 1 and 2 | Lac+ | Virˢ |
    | strain B | substances 3 and 4 | Lac− | Virʳ |

    **Experiment 1.** Two billion cells of A alone on a bare plate: nothing
    grows. B alone: nothing. Two billion of each, mixed, washed and spread:
    **312 colonies**.

    **Experiment 2.** The 312 colonies, scored for Lac and Vir:

    | colony type | count |
    | :-- | --: |
    | Lac+ Virˢ (like A) | 128 |
    | Lac− Virʳ (like B) | 141 |
    | Lac+ Virʳ | 21 |
    | Lac− Virˢ | 22 |

    **Experiment 3.** A third trait, **Gal** (galactose fermentation), is
    added. The cross is repeated with strains that differ in each pair of
    traits, and each time the share of colonies with a mixed combination
    (one trait from each parent) is counted: Lac and Vir, about 14%; Lac
    and Gal, about 5%; Gal and Vir, about 9%.

    **Your task.**

    1. List every explanation for the 312 colonies, with an observation
       that would rule each out.
    2. What would Experiment 2 show if the two traits were inherited
       independently? What does it actually show?
    3. What relation do the three percentages of Experiment 3 obey, and
       what picture does that relation force on you?
    4. Do the cells pass material by touching, or through the broth?
       Design one apparatus that decides.
    5. Predict one thing your explanation says must happen that nobody has
       looked at yet.

![Three petri dishes of bare growth medium: strain A alone is empty, strain B alone is empty, and the dish spread with a mixture of both strains carries scattered colonies](../assets/images/problems/bacterial-hybrids.svg){ width="560" }

*Experiment 1 as three plates. Schematic: the dots stand for colonies and are not a count. Drawn for this site (CC BY 4.0).*

## Why it is in the course

Section 5, "Inferences, Hypotheses, Explanations", opens with Chamberlin's
*The Method of Multiple Working Hypotheses* (session 25) and Platt's *Strong
Inference* (session 27). It ends in session 30 with Judson's chapter on
theory and this problem, the last one in the schedule. The version
reconstructed here asks for both readings on one set of numbers.

Colonies where there should be none have several honest explanations.
"Facts before explanations of facts" (the syllabus's phrase for session 04)
means listing them all before choosing one. Then traits nobody selected
narrow the choice, and three measurements obey a relation that none of
them shows alone. No biology is needed. The syllabus says the exercises
"depend as little as possible on knowledge of any particular subject area".

## Where it comes from

The phrase "bacterial hybrids" was already in print in 1924, in the title
of a paper by E. Almquist. Until the mid-1940s, though, bacteria were
widely assumed to lie outside genetics: no visible chromosomes, no sex,
nothing to cross.

In 1946 Joshua Lederberg, then a graduate student, and Edward Tatum mixed
two strains of *Escherichia coli* K-12, each unable to make several
substances it needed. They recovered rare colonies that grew where neither
parent could. What those colonies meant was disputed for years. Lederberg
shared the 1958 Nobel Prize in Physiology or Medicine for this work, and
in 1996 he looked back on how sharply it had been contested. How the
dispute was settled is in the Resolution below.

![Scanning electron micrograph of rod-shaped Escherichia coli cells, digitally coloured](../assets/images/problems/bacterial-hybrids-ecoli.jpg){ width="560" }

*Escherichia coli at about 10,000×. Photo by Eric Erbe, digital colourization by Christopher Pooley, USDA Agricultural Research Service. Public domain, via Wikimedia Commons.*

??? tip "Hints"

    - First explain the two plates that grew nothing. What do they rule out?
    - Independent traits behave like two coin flips. What counts would that
      give?
    - Add two of the percentages and compare with the third.
    - For question 4, you need a vessel where broth is shared but cells are
      not.

??? success "Resolution"

    **Linkage.** Independence predicts about 78 in each class. Instead the
    parental types make up 269 of 312 (86%): Lac and Vir usually travel
    together. They are *linked*. In 1947 Lederberg reported this kind of
    linkage among unselected traits, including lactose fermentation and
    phage resistance.

    **Order.** 5 + 9 = 14, and no other pairing works. Frequencies that add
    like distances lie on a line, with Gal between Lac and Vir. What passes
    between the cells is an ordered arrangement, not a bag of separate
    factors.

    **The rivals.** The control plates all but exclude back-mutation.
    Re-streaking one colony alone on a bare plate tests cross-feeding: if it
    grows by itself, it is a new kind of cell. The diffusible substance fell
    to Bernard Davis's 1950 U-tube: a sintered glass filter let broth
    through but no cell, and no recombinants appeared. The cells must touch.

    **What it turned out to be.** Transfer by contact, now called bacterial
    conjugation. William Hayes showed in 1953 that it runs one way, from a
    donor to a recipient. Élie Wollman, François Jacob and Hayes then
    interrupted matings at timed intervals (1956) and saw markers arrive in
    sequence. The map eventually closed on itself: the *E. coli* chromosome
    is a circle.

    **A caveat.** The tidy sum was built into the made-up data; real
    recombination frequencies add only approximately.

## Sources

- **Arthur T. Winfree**, *The Art of Scientific Discovery* (ECOL 479/579), course handout; the session-30 schedule line and its link markup — [Wayback Machine capture, 20 April 2002](https://web.archive.org/web/20020420212713/http://eebweb.arizona.edu/Faculty/Winfree/handout_479.htm){target=_blank} 🔓
- **Joshua Lederberg and Edward L. Tatum**, "Gene Recombination in Escherichia coli", *Nature* 158, 558 (1946) — [doi:10.1038/158558a0](https://doi.org/10.1038/158558a0){target=_blank} 🔒
- **Edward L. Tatum and Joshua Lederberg**, "Gene Recombination in the Bacterium Escherichia coli", *Journal of Bacteriology* 53(6), 673–684 (1947) — [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC518375/){target=_blank} 🔓
- **Joshua Lederberg**, "Gene Recombination and Linked Segregations in Escherichia Coli", *Genetics* 32(5), 505–525 (1947) — [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC1209393/){target=_blank} 🔓
- **Bernard D. Davis**, "Nonfiltrability of the Agents of Genetic Recombination in Escherichia coli", *Journal of Bacteriology* 60(4), 507–508 (1950) — [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC385908/){target=_blank} 🔓
- **William Hayes**, "Observations on a Transmissible Agent Determining Sexual Differentiation in Bacterium coli", *Journal of General Microbiology* 8(1), 72–88 (1953) — [doi:10.1099/00221287-8-1-72](https://doi.org/10.1099/00221287-8-1-72){target=_blank} 🔒
- **Élie L. Wollman, François Jacob and William Hayes**, "Conjugation and Genetic Recombination in Escherichia coli K-12", *Cold Spring Harbor Symposia on Quantitative Biology* 21, 141–162 (1956) — [doi:10.1101/sqb.1956.021.01.012](https://doi.org/10.1101/sqb.1956.021.01.012){target=_blank} 🔒
- **Joshua Lederberg**, "Genetic Recombination in Escherichia coli: Disputation at Cold Spring Harbor, 1946–1996", *Genetics* 144(2), 439–443 (1996) — [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC1207540/){target=_blank} 🔓
- **E. Almquist**, "Investigations on Bacterial Hybrids", *Journal of Infectious Diseases* 35(4), 341–346 (1924) — [doi:10.1093/infdis/35.4.341](https://doi.org/10.1093/infdis/35.4.341){target=_blank} 🔒 (cited only for the phrase in its title)
- **Arthur T. Winfree**, *The Art of Scientific Discovery*, original course syllabus — [PDF](https://github.com/tyson-swetnam/aosd/blob/main/docs/assets/aosd_syllabus.pdf){target=_blank} 🔓

!!! note "How sure are we that this is Winfree's problem?"

    The syllabus gives only the name, the session and the reading. In
    Winfree's handout, the link on this item points to a bookmark named
    `Lac_Vir`; its target was never archived. Such bookmarks elsewhere name
    the subject behind a playful title ("Paired Observations" points to
    `Keplers_Laws`). Lac (lactose fermentation) and virus resistance were
    the traits scored in the early *E. coli* crosses, so the subject is
    fairly secure. That reading is the editors' inference, not Winfree's
    text. What is lost is the exercise itself: his wording, his data and
    its form. Identification: **probable**.

    - **Reconstructing the Lederberg–Tatum reasoning** (high): the reading used on this page.
    - **The same episode as a multiple-working-hypotheses exercise** (medium): compatible with the first.
    - **Later *E. coli* genetics** (not weighed): Lac as the lac operon and Vir as a virulent phage such as lambda vir.
    - **An invented "toy genetics" table** (low): does not explain why Lac and Vir are named.

---

*Back to [Section 5](../section5.md) · [All problems](index.md) · [The schedule](../syllabus.md#section-5-inferences-hypotheses-explanations)*
