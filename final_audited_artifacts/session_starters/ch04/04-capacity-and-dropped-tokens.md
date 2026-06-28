# Session starter: Chapter 4.4 - Capacity and dropped tokens

Develop only Chapter 4.4, **Capacity and dropped tokens**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch04/04-capacity-and-dropped-tokens.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch04/sections/04-capacity-and-dropped-tokens.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch04/fig-capacity-and-dropped-tokens}`
- `\input{tables/ch04/tab-capacity-and-dropped-tokens}`
- `\input{equations/ch04/eq-capacity-and-dropped-tokens}`
- `\input{listings/ch04/lst-capacity-and-dropped-tokens}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
