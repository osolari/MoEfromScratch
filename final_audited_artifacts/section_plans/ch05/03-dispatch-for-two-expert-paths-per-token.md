# Section plan: Chapter 5.3 - Dispatch for two expert paths per token

## Local objective

Adapt the dispatch loop so each selected expert path contributes to the same output row.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Token 0 goes to experts 1 and 3; both outputs are accumulated into output[0].

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch05/fig-dispatch-for-two-expert-paths-per-token}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch05/eq-dispatch-for-two-expert-paths-per-token}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch05/lst-dispatch-for-two-expert-paths-per-token}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Top-2 dispatch is correct but still slow; vectorization comes after the routing math is clear.

## Planned artifacts

- `latex_book_skeleton/figures/ch05/fig-dispatch-for-two-expert-paths-per-token.tex` - TikZ. Shows: Two paths per token gathered into expert batches and accumulated back.. Caption placeholder included. Label: `fig:ch05-dispatch-for-two-expert-paths-per-token`.
- `latex_book_skeleton/tables/ch05/tab-dispatch-for-two-expert-paths-per-token.tex` - Table. Defines: Data structures for topk_idx, gates, expert batches, and output accumulation.. Caption placeholder included. Label: `tab:ch05-dispatch-for-two-expert-paths-per-token`.
- `latex_book_skeleton/listings/ch05/lst-dispatch-for-two-expert-paths-per-token.tex` - Python listing. Implements or sketches: Top2MoELayer forward pass with nested selected-expert accumulation.. Caption placeholder included. Label: `lst:ch05-dispatch-for-two-expert-paths-per-token`.
- `latex_book_skeleton/equations/ch05/eq-dispatch-for-two-expert-paths-per-token.tex` - Equation. States: out_t += gate_{tj} expert_{idx_{tj}}(x_t).. Label: `eq:ch05-dispatch-for-two-expert-paths-per-token`.

## Code deliverable

Develop the code in `ch05/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Check output changes when gates are manually swapped.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
