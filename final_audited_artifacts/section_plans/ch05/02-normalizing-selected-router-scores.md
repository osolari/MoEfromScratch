# Section plan: Chapter 5.2 - Normalizing selected router scores

## Local objective

Turn top-2 scores into gates that sum to one for each token.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Normalize selected scores [0.8, 0.2] and [0.51, 0.49] and compare combines.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch05/fig-normalizing-selected-router-scores}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch05/eq-normalizing-selected-router-scores}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch05/lst-normalizing-selected-router-scores}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The normalized gates weight two expert outputs per token.

## Planned artifacts

- `latex_book_skeleton/figures/ch05/fig-normalizing-selected-router-scores.tex` - TikZ. Shows: Top-2 score row transformed into a two-weight gate vector.. Caption placeholder included. Label: `fig:ch05-normalizing-selected-router-scores`.
- `latex_book_skeleton/tables/ch05/tab-normalizing-selected-router-scores.tex` - Table. Defines: Raw scores, selected scores, normalized gates, and gate sums.. Caption placeholder included. Label: `tab:ch05-normalizing-selected-router-scores`.
- `latex_book_skeleton/listings/ch05/lst-normalizing-selected-router-scores.tex` - Python listing. Implements or sketches: selected_scores / selected_scores.sum(dim=-1, keepdim=True).. Caption placeholder included. Label: `lst:ch05-normalizing-selected-router-scores`.
- `latex_book_skeleton/equations/ch05/eq-normalizing-selected-router-scores.tex` - Equation. States: gate_{tj} = score_{t,idx_{tj}} / sum_l score_{t,idx_{tl}}.. Label: `eq:ch05-normalizing-selected-router-scores`.

## Code deliverable

Develop the code in `ch05/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Assert torch.allclose(gates.sum(-1), ones).

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
