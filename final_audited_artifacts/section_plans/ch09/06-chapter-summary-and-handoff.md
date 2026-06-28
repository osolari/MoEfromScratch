# Section plan: Chapter 9.6 - Chapter summary and handoff

## Local objective

Lock the final router behavior and document the invariants required by the complete model.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Trace one token through score, bias, selected experts, unbiased gates, expert outputs, and metrics.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch09/fig-chapter-summary-and-handoff}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch09/eq-chapter-summary-and-handoff}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch09/lst-chapter-summary-and-handoff}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: We can now build the full model with this routing block as the FFN replacement.

## Planned artifacts

- `latex_book_skeleton/figures/ch09/fig-chapter-summary-and-handoff.tex` - TikZ. Shows: Final router contract diagram with selection and combine paths separated.. Caption placeholder included. Label: `fig:ch09-chapter-summary-and-handoff`.
- `latex_book_skeleton/tables/ch09/tab-chapter-summary-and-handoff.tex` - Table. Defines: Final router invariants and tests.. Caption placeholder included. Label: `tab:ch09-chapter-summary-and-handoff`.
- `latex_book_skeleton/listings/ch09/lst-chapter-summary-and-handoff.tex` - Python listing. Implements or sketches: RouterBiasBalancer smoke test covering update and no-gradient behavior.. Caption placeholder included. Label: `lst:ch09-chapter-summary-and-handoff`.
- `latex_book_skeleton/equations/ch09/eq-chapter-summary-and-handoff.tex` - Equation. States: Final routing formula for MiniDeepSeekMoE.. Label: `eq:ch09-chapter-summary-and-handoff`.

## Code deliverable

Develop the code in `ch09/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Reader checkpoint: explain why bias should not be included in combine weights.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
