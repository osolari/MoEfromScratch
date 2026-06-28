# Session starter: Chapter 10.2 - Decoder block with dense prefix and MoE layers

Develop only Chapter 10.2, **Decoder block with dense prefix and MoE layers**, for *MoE Models from Scratch*.

Use the detailed brief at:

`section_development_briefs/ch10/02-decoder-block-with-dense-prefix-and-moe-layers.md`

Must produce LaTeX section prose at:

`latex_book_skeleton/chapters/ch10/sections/02-decoder-block-with-dense-prefix-and-moe-layers.tex`

Must update artifacts only through standalone `.tex` wrappers:

- `\input{figures/ch10/fig-decoder-block-with-dense-prefix-and-moe-layers}`
- `\input{tables/ch10/tab-decoder-block-with-dense-prefix-and-moe-layers}`
- `\input{equations/ch10/eq-decoder-block-with-dense-prefix-and-moe-layers}`
- `\input{listings/ch10/lst-decoder-block-with-dense-prefix-and-moe-layers}`

Follow the section arc: problem opening -> visual anchor -> shapes/math -> implementation -> diagnostic -> bridge. Preserve the color map and artifact wrapper contract from the brief.

Keep figures and tables in their owning section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
