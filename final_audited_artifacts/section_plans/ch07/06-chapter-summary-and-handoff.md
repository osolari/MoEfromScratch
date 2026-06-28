# Section plan: Chapter 7.6 - Chapter summary and handoff

## Local objective

Frame auxiliary balancing as the baseline that auxiliary-loss-free balancing will later improve on.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Compare training metrics with aux_coef=0 and aux_coef>0 in a smoke run.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch07/fig-chapter-summary-and-handoff}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch07/eq-chapter-summary-and-handoff}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch07/lst-chapter-summary-and-handoff}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: MiniDeepSeekMoE keeps the routing lessons but changes expert structure before changing the balancing method.

## Planned artifacts

- `latex_book_skeleton/figures/ch07/fig-chapter-summary-and-handoff.tex` - TikZ. Shows: Before-and-after load histograms for auxiliary balancing.. Caption placeholder included. Label: `fig:ch07-chapter-summary-and-handoff`.
- `latex_book_skeleton/tables/ch07/tab-chapter-summary-and-handoff.tex` - Table. Defines: What auxiliary loss fixes and what trade-offs remain.. Caption placeholder included. Label: `tab:ch07-chapter-summary-and-handoff`.
- `latex_book_skeleton/listings/ch07/lst-chapter-summary-and-handoff.tex` - Python listing. Implements or sketches: Config presets for no-balancing and auxiliary-balancing runs.. Caption placeholder included. Label: `lst:ch07-chapter-summary-and-handoff`.
- `latex_book_skeleton/equations/ch07/eq-chapter-summary-and-handoff.tex` - Equation. States: Model objective includes both LM and routing terms in this chapter.. Label: `eq:ch07-chapter-summary-and-handoff`.

## Code deliverable

Develop the code in `ch07/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Reader checkpoint: explain why aux_loss must be logged separately from LM loss.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
