# Session starter: Chapter 10.4 - Training and sampling scripts

Develop only Chapter 10.4, **Training and sampling scripts**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch10/04-training-and-sampling-scripts.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch10/sections/04-training-and-sampling-scripts.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch10/fig-training-and-sampling-scripts}`
- `\input{tables/ch10/tab-training-and-sampling-scripts}`
- `\input{equations/ch10/eq-training-and-sampling-scripts}`
- `\input{listings/ch10/lst-training-and-sampling-scripts}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
