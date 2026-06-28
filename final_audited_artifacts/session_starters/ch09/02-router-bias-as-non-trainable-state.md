# Session starter: Chapter 9.2 - Router bias as non-trainable state

Develop only Chapter 9.2, **Router bias as non-trainable state**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch09/02-router-bias-as-non-trainable-state.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch09/sections/02-router-bias-as-non-trainable-state.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch09/fig-router-bias-as-non-trainable-state}`
- `\input{tables/ch09/tab-router-bias-as-non-trainable-state}`
- `\input{equations/ch09/eq-router-bias-as-non-trainable-state}`
- `\input{listings/ch09/lst-router-bias-as-non-trainable-state}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
