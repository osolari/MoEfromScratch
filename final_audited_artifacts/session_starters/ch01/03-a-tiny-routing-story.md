# Session starter: Chapter 1.3 - A tiny routing story

Develop only Chapter 1.3, **A tiny routing story**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch01/03-a-tiny-routing-story.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch01/sections/03-a-tiny-routing-story.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch01/fig-a-tiny-routing-story}`
- `\input{tables/ch01/tab-a-tiny-routing-story}`
- `\input{equations/ch01/eq-a-tiny-routing-story}`
- `\input{listings/ch01/lst-a-tiny-routing-story}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
