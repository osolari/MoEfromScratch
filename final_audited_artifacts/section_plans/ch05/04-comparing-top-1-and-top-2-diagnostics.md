# Section plan: Chapter 5.4 - Comparing top-1 and top-2 diagnostics

## Local objective

Use the same metrics to show how K changes load, drop rate, and routing entropy.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Run the same random batch through top-1 and top-2 routers with the same scores.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch05/fig-comparing-top-1-and-top-2-diagnostics}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch05/eq-comparing-top-1-and-top-2-diagnostics}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch05/lst-comparing-top-1-and-top-2-diagnostics}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Once routing variants share diagnostics, the next challenge is making dispatch less loop-heavy.

## Planned artifacts

- `latex_book_skeleton/figures/ch05/fig-comparing-top-1-and-top-2-diagnostics.tex` - TikZ. Shows: Side-by-side expert load histograms for K=1 and K=2.. Caption placeholder included. Label: `fig:ch05-comparing-top-1-and-top-2-diagnostics`.
- `latex_book_skeleton/tables/ch05/tab-comparing-top-1-and-top-2-diagnostics.tex` - Table. Defines: Comparison rows for active calls, max load, entropy, and gate concentration.. Caption placeholder included. Label: `tab:ch05-comparing-top-1-and-top-2-diagnostics`.
- `latex_book_skeleton/listings/ch05/lst-comparing-top-1-and-top-2-diagnostics.tex` - Python listing. Implements or sketches: compare_routing_modes(router_scores, k_values=[1,2]).. Caption placeholder included. Label: `lst:ch05-comparing-top-1-and-top-2-diagnostics`.
- `latex_book_skeleton/equations/ch05/eq-comparing-top-1-and-top-2-diagnostics.tex` - Equation. States: Active expert calls equal N*K before capacity limits.. Label: `eq:ch05-comparing-top-1-and-top-2-diagnostics`.

## Code deliverable

Develop the code in `ch05/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Save a comparison table and one histogram per routing mode.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
