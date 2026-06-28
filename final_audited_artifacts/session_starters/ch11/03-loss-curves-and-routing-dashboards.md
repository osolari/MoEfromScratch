# Session starter: Chapter 11.3 - Loss curves and routing dashboards

Develop only Chapter 11.3, **Loss curves and routing dashboards**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch11/03-loss-curves-and-routing-dashboards.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch11/sections/03-loss-curves-and-routing-dashboards.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch11/fig-loss-curves-and-routing-dashboards}`
- `\input{tables/ch11/tab-loss-curves-and-routing-dashboards}`
- `\input{equations/ch11/eq-loss-curves-and-routing-dashboards}`
- `\input{listings/ch11/lst-loss-curves-and-routing-dashboards}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
