# Session starter: Chapter 7.2 - Auxiliary load-balancing loss

Develop only Chapter 7.2, **Auxiliary load-balancing loss**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch07/02-auxiliary-load-balancing-loss.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch07/sections/02-auxiliary-load-balancing-loss.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch07/fig-auxiliary-load-balancing-loss}`
- `\input{tables/ch07/tab-auxiliary-load-balancing-loss}`
- `\input{equations/ch07/eq-auxiliary-load-balancing-loss}`
- `\input{listings/ch07/lst-auxiliary-load-balancing-loss}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
