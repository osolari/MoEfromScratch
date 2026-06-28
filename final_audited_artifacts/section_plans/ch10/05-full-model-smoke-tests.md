# Section plan: Chapter 10.5 - Full-model smoke tests

## Local objective

Create a test suite that catches shape, routing, balancing, and serialization failures.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Run the smoke config on CPU for two forward/backward passes.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch10/fig-full-model-smoke-tests}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch10/eq-full-model-smoke-tests}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch10/lst-full-model-smoke-tests}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: With a complete tested implementation, the next chapter runs experiments and interprets diagnostics.

## Planned artifacts

- `latex_book_skeleton/figures/ch10/fig-full-model-smoke-tests.tex` - TikZ. Shows: Smoke-test pipeline with pass/fail checkpoints after each stage.. Caption placeholder included. Label: `fig:ch10-full-model-smoke-tests`.
- `latex_book_skeleton/tables/ch10/tab-full-model-smoke-tests.tex` - Table. Defines: Test names, purpose, and expected runtime tier.. Caption placeholder included. Label: `tab:ch10-full-model-smoke-tests`.
- `latex_book_skeleton/listings/ch10/lst-full-model-smoke-tests.tex` - Python listing. Implements or sketches: tests/test_minideepseekmoe_smoke.py with forward, backward, bias-update, and save-load tests.. Caption placeholder included. Label: `lst:ch10-full-model-smoke-tests`.
- `latex_book_skeleton/equations/ch10/eq-full-model-smoke-tests.tex` - Equation. States: No NaNs and finite loss invariant.. Label: `eq:ch10-full-model-smoke-tests`.

## Code deliverable

Develop the code in `ch10/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

CI-style console summary for all smoke tests.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
