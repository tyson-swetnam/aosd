# Art Winfree's The Art of Scientific Discovery

These pages are based upon the late [Professor Art Winfree's](https://en.wikipedia.org/wiki/Arthur_Winfree) undergraduate seminar "[The Art of Scientific Discovery](https://web.archive.org/web/20040801000000*/http://eebweb.arizona.edu/faculty/winfree/Handout_479.htm)" at the University of Arizona.

While these materials are now in the public domain, this project respectfully acknowledges Professor Winfrees's ownership over the course materials. The original work was produced under the Arizona Board of Regents.

This work is licensed under a Creative Commons Attribution 4.0 International License. To view a copy of this license, visit: https://creativecommons.org/licenses/by/4.0/

Modifications have been made to the original material, including updates to the hyperlinks in the original Syllabus, and links to currently accessible readings.

## For AI agents

This site is published for people and for AI agents. `docs/` is an [Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) bundle, and the deployed site exposes it directly: [`llms.txt`](https://tyson-swetnam.github.io/aosd/llms.txt) (linked outline), [`llms-full.txt`](https://tyson-swetnam.github.io/aosd/llms-full.txt) (whole corpus), any page URL plus `index.md` for that page's Markdown with frontmatter, and `robots.txt` pointing at all of them. See [For AI agents](https://tyson-swetnam.github.io/aosd/about/ai-agents/) on the site and `AGENTS.md` in this repository.

## Building locally

```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/mkdocs serve
```

CI (`.github/workflows/main.yml`) validates the bundle, builds with `mkdocs build --strict`, runs `scripts/postbuild_agent_surface.py` and `scripts/check_site.py`, and deploys to GitHub Pages.
