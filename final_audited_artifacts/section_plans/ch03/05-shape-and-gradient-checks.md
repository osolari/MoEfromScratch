# Section plan: Chapter 3.5 - Shape and gradient checks

## Local objective

Make the first MoE layer testable before introducing more routing variants.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Run a two-layer smoke model and confirm all experts receive gradients when selected.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch03/fig-shape-and-gradient-checks}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch03/eq-shape-and-gradient-checks}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch03/lst-shape-and-gradient-checks}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The next chapter simplifies to top-1 routing to teach sparse dispatch one expert at a time.

## Planned artifacts

- `latex_book_skeleton/figures/ch03/fig-shape-and-gradient-checks.tex` - TikZ. Shows: Gradient flow diagram from loss through combine weights into router and selected experts.. Caption placeholder included. Label: `fig:ch03-shape-and-gradient-checks`.
- `latex_book_skeleton/tables/ch03/tab-shape-and-gradient-checks.tex` - Table. Defines: Test cases for shapes, gate sums, selected expert counts, and gradients.. Caption placeholder included. Label: `tab:ch03-shape-and-gradient-checks`.
- `latex_book_skeleton/listings/ch03/lst-shape-and-gradient-checks.tex` - Python listing. Implements or sketches: Unit tests for MoELayer output shape and gradient presence.. Caption placeholder included. Label: `lst:ch03-shape-and-gradient-checks`.
- `latex_book_skeleton/equations/ch03/eq-shape-and-gradient-checks.tex` - Equation. States: Loss gradient reaches gate and expert paths through the weighted sum.. Label: `eq:ch03-shape-and-gradient-checks`.

## Code deliverable

Develop the code in `ch03/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Count selected expert IDs and check nonzero gradients for selected expert parameters.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
