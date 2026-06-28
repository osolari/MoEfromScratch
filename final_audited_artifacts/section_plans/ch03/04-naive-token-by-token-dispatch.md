# Section plan: Chapter 3.4 - Naive token-by-token dispatch

## Local objective

Implement dispatch with loops first so the control flow is unmistakable.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

For each token and selected expert, call the expert and add gate-weighted output.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch03/fig-naive-token-by-token-dispatch}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch03/eq-naive-token-by-token-dispatch}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch03/lst-naive-token-by-token-dispatch}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The naive layer works, but the router choices are still fragile; top-1 routing exposes this clearly.

## Planned artifacts

- `latex_book_skeleton/figures/ch03/fig-naive-token-by-token-dispatch.tex` - TikZ. Shows: Loop-based dispatch arrows from token rows to selected expert calls.. Caption placeholder included. Label: `fig:ch03-naive-token-by-token-dispatch`.
- `latex_book_skeleton/tables/ch03/tab-naive-token-by-token-dispatch.tex` - Table. Defines: Naive dispatch variables and their role in the loop.. Caption placeholder included. Label: `tab:ch03-naive-token-by-token-dispatch`.
- `latex_book_skeleton/listings/ch03/lst-naive-token-by-token-dispatch.tex` - Python listing. Implements or sketches: NaiveMoELayer forward pass using explicit token and expert loops.. Caption placeholder included. Label: `lst:ch03-naive-token-by-token-dispatch`.
- `latex_book_skeleton/equations/ch03/eq-naive-token-by-token-dispatch.tex` - Equation. States: routed_out_t = sum_{j=1}^K gate_{tj} expert_{idx_{tj}}(x_t).. Label: `eq:ch03-naive-token-by-token-dispatch`.

## Code deliverable

Develop the code in `ch03/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Compare output shape to dense FFN output and inspect gates per token.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
