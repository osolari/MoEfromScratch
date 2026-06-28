# Section plan: Chapter 7.2 - Auxiliary load-balancing loss

## Local objective

Implement the classic balancing baseline as a transparent, measurable loss term.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Compute expert load fractions and probability fractions for E=4 experts.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch07/fig-auxiliary-load-balancing-loss}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch07/eq-auxiliary-load-balancing-loss}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch07/lst-auxiliary-load-balancing-loss}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Auxiliary loss enters the total training objective with a coefficient.

## Planned artifacts

- `latex_book_skeleton/figures/ch07/fig-auxiliary-load-balancing-loss.tex` - TikZ. Shows: Two bars per expert: selected load and router probability mass.. Caption placeholder included. Label: `fig:ch07-auxiliary-load-balancing-loss`.
- `latex_book_skeleton/tables/ch07/tab-auxiliary-load-balancing-loss.tex` - Table. Defines: Inputs and outputs of the auxiliary loss function.. Caption placeholder included. Label: `tab:ch07-auxiliary-load-balancing-loss`.
- `latex_book_skeleton/listings/ch07/lst-auxiliary-load-balancing-loss.tex` - Python listing. Implements or sketches: load_balancing_loss function returning scalar aux_loss and metrics.. Caption placeholder included. Label: `lst:ch07-auxiliary-load-balancing-loss`.
- `latex_book_skeleton/equations/ch07/eq-auxiliary-load-balancing-loss.tex` - Equation. States: Auxiliary loss proportional to E * sum_i load_i * prob_i.. Label: `eq:ch07-auxiliary-load-balancing-loss`.

## Code deliverable

Develop the code in `ch07/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Check loss is lower for balanced synthetic routing than collapsed routing.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
