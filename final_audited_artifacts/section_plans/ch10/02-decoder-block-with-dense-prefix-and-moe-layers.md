# Section plan: Chapter 10.2 - Decoder block with dense prefix and MoE layers

## Local objective

Assemble layers so early dense computation can precede sparse MoE layers if configured.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Use one dense prefix layer followed by MoE blocks in the default config.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch10/fig-decoder-block-with-dense-prefix-and-moe-layers}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch10/eq-decoder-block-with-dense-prefix-and-moe-layers}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch10/lst-decoder-block-with-dense-prefix-and-moe-layers}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The model forward pass must carry routing metrics out of each MoE layer.

## Planned artifacts

- `latex_book_skeleton/figures/ch10/fig-decoder-block-with-dense-prefix-and-moe-layers.tex` - TikZ. Shows: Stack of decoder blocks showing dense prefix and repeated MoE layers.. Caption placeholder included. Label: `fig:ch10-decoder-block-with-dense-prefix-and-moe-layers`.
- `latex_book_skeleton/tables/ch10/tab-decoder-block-with-dense-prefix-and-moe-layers.tex` - Table. Defines: Layer type by index for smoke, default, and larger teaching configs.. Caption placeholder included. Label: `tab:ch10-decoder-block-with-dense-prefix-and-moe-layers`.
- `latex_book_skeleton/listings/ch10/lst-decoder-block-with-dense-prefix-and-moe-layers.tex` - Python listing. Implements or sketches: DecoderBlock factory that chooses DenseFFN or MiniDeepSeekMoELayer.. Caption placeholder included. Label: `lst:ch10-decoder-block-with-dense-prefix-and-moe-layers`.
- `latex_book_skeleton/equations/ch10/eq-decoder-block-with-dense-prefix-and-moe-layers.tex` - Equation. States: block(x) = x + attention(norm(x)); x = x + ffn_or_moe(norm(x)).. Label: `eq:ch10-decoder-block-with-dense-prefix-and-moe-layers`.

## Code deliverable

Develop the code in `ch10/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

List layer types during model initialization.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
