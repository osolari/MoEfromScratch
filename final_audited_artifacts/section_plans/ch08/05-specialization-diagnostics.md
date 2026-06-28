# Section plan: Chapter 8.5 - Specialization diagnostics

## Local objective

Plan diagnostics that reveal whether routed experts are used differently across tokens.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Group tokens by simple categories or positions and inspect selected expert frequencies.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch08/fig-specialization-diagnostics}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch08/eq-specialization-diagnostics}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch08/lst-specialization-diagnostics}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The layer architecture is now complete; the next chapter replaces auxiliary loss with dynamic router bias balancing.

## Planned artifacts

- `latex_book_skeleton/figures/ch08/fig-specialization-diagnostics.tex` - TikZ. Shows: Expert usage heatmap by token group or position bucket.. Caption placeholder included. Label: `fig:ch08-specialization-diagnostics`.
- `latex_book_skeleton/tables/ch08/tab-specialization-diagnostics.tex` - Table. Defines: Specialization probes: token string, position, loss contribution, selected experts.. Caption placeholder included. Label: `tab:ch08-specialization-diagnostics`.
- `latex_book_skeleton/listings/ch08/lst-specialization-diagnostics.tex` - Python listing. Implements or sketches: collect_expert_usage_by_token helper.. Caption placeholder included. Label: `lst:ch08-specialization-diagnostics`.
- `latex_book_skeleton/equations/ch08/eq-specialization-diagnostics.tex` - Equation. States: Conditional usage frequency p(expert | token_group).. Label: `eq:ch08-specialization-diagnostics`.

## Code deliverable

Develop the code in `ch08/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Generate expert usage heatmaps without overclaiming semantic specialization.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
