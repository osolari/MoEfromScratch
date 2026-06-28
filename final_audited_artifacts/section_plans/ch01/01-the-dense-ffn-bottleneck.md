# Section plan: Chapter 1.1 - The dense FFN bottleneck

## Local objective

Show that the dense feed-forward block is the natural place to introduce sparsity because every token pays for every hidden unit.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Use a four-token batch with d_model=8 and an FFN expansion factor of 4; count multiply-adds for all tokens.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch01/fig-the-dense-ffn-bottleneck}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch01/eq-the-dense-ffn-bottleneck}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch01/lst-the-dense-ffn-bottleneck}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Once the bottleneck is visible, the next question is whether every token really needs the same FFN.

## Planned artifacts

- `latex_book_skeleton/figures/ch01/fig-the-dense-ffn-bottleneck.tex` - TikZ. Shows: Dense decoder block with the FFN path highlighted as the always-on compute region.. Caption placeholder included. Label: `fig:ch01-the-dense-ffn-bottleneck`.
- `latex_book_skeleton/tables/ch01/tab-the-dense-ffn-bottleneck.tex` - Table. Defines: Parameter and activation shape comparison for attention, dense FFN, and the residual path.. Caption placeholder included. Label: `tab:ch01-the-dense-ffn-bottleneck`.
- `latex_book_skeleton/listings/ch01/lst-the-dense-ffn-bottleneck.tex` - Python listing. Implements or sketches: Tiny function that estimates dense FFN parameters and per-token matrix multiplies.. Caption placeholder included. Label: `lst:ch01-the-dense-ffn-bottleneck`.
- `latex_book_skeleton/equations/ch01/eq-the-dense-ffn-bottleneck.tex` - Equation. States: Dense FFN cost estimate using D, H, and number of tokens N.. Label: `eq:ch01-the-dense-ffn-bottleneck`.

## Code deliverable

Develop the code in `ch01/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

A small cost table proving that increasing H increases every token path.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
