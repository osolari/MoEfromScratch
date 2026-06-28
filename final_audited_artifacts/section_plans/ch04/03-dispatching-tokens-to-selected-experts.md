# Section plan: Chapter 4.3 - Dispatching tokens to selected experts

## Local objective

Run each expert only on the tokens assigned to it and scatter outputs back to token order.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Expert 0 receives token rows [0,3], expert 1 receives [1], and empty experts are skipped.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch04/fig-dispatching-tokens-to-selected-experts}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch04/eq-dispatching-tokens-to-selected-experts}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch04/lst-dispatching-tokens-to-selected-experts}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Routing can overload an expert, so we need to define expert capacity.

## Planned artifacts

- `latex_book_skeleton/figures/ch04/fig-dispatching-tokens-to-selected-experts.tex` - TikZ. Shows: Gather tokens into expert batches, process, then scatter back.. Caption placeholder included. Label: `fig:ch04-dispatching-tokens-to-selected-experts`.
- `latex_book_skeleton/tables/ch04/tab-dispatching-tokens-to-selected-experts.tex` - Table. Defines: Gather, expert batch, and scatter tensor shapes.. Caption placeholder included. Label: `tab:ch04-dispatching-tokens-to-selected-experts`.
- `latex_book_skeleton/listings/ch04/lst-dispatching-tokens-to-selected-experts.tex` - Python listing. Implements or sketches: Top1MoELayer dispatch and scatter implementation.. Caption placeholder included. Label: `lst:ch04-dispatching-tokens-to-selected-experts`.
- `latex_book_skeleton/equations/ch04/eq-dispatching-tokens-to-selected-experts.tex` - Equation. States: output[token_indices_i] = expert_i(x[token_indices_i]).. Label: `eq:ch04-dispatching-tokens-to-selected-experts`.

## Code deliverable

Develop the code in `ch04/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Assert output rows return to the original token order.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
