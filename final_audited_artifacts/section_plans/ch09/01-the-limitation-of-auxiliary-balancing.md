# Section plan: Chapter 9.1 - The limitation of auxiliary balancing

## Local objective

Explain why a separate balancing mechanism is attractive after readers have implemented auxiliary losses.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Show total_loss changes when aux_coef changes even with the same LM loss.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch09/fig-the-limitation-of-auxiliary-balancing}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch09/eq-the-limitation-of-auxiliary-balancing}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch09/lst-the-limitation-of-auxiliary-balancing}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Router bias moves balance control into the selection rule rather than the loss.

## Planned artifacts

- `latex_book_skeleton/figures/ch09/fig-the-limitation-of-auxiliary-balancing.tex` - TikZ. Shows: Auxiliary loss path entering the optimization objective beside LM loss.. Caption placeholder included. Label: `fig:ch09-the-limitation-of-auxiliary-balancing`.
- `latex_book_skeleton/tables/ch09/tab-the-limitation-of-auxiliary-balancing.tex` - Table. Defines: Auxiliary balancing benefits and trade-offs.. Caption placeholder included. Label: `tab:ch09-the-limitation-of-auxiliary-balancing`.
- `latex_book_skeleton/listings/ch09/lst-the-limitation-of-auxiliary-balancing.tex` - Python listing. Implements or sketches: Experiment config that toggles aux_loss on and off for the same model.. Caption placeholder included. Label: `lst:ch09-the-limitation-of-auxiliary-balancing`.
- `latex_book_skeleton/equations/ch09/eq-the-limitation-of-auxiliary-balancing.tex` - Equation. States: total_loss includes auxiliary term in the baseline approach.. Label: `eq:ch09-the-limitation-of-auxiliary-balancing`.

## Code deliverable

Develop the code in `ch09/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Compare LM loss and load balance separately, not only total loss.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
