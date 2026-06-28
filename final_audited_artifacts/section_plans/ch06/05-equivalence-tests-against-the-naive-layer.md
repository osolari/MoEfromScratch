# Section plan: Chapter 6.5 - Equivalence tests against the naive layer

## Local objective

Prove the vectorized implementation matches the simple implementation in the no-overflow case.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Use fixed router scores and identical expert weights for both layers.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch06/fig-equivalence-tests-against-the-naive-layer}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch06/eq-equivalence-tests-against-the-naive-layer}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch06/lst-equivalence-tests-against-the-naive-layer}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: With efficient dispatch available, we can focus on the training losses that shape router behavior.

## Planned artifacts

- `latex_book_skeleton/figures/ch06/fig-equivalence-tests-against-the-naive-layer.tex` - TikZ. Shows: Two implementation paths producing matching output tensors.. Caption placeholder included. Label: `fig:ch06-equivalence-tests-against-the-naive-layer`.
- `latex_book_skeleton/tables/ch06/tab-equivalence-tests-against-the-naive-layer.tex` - Table. Defines: Test matrix for K, E, D, capacity factor, dtype, and overflow setting.. Caption placeholder included. Label: `tab:ch06-equivalence-tests-against-the-naive-layer`.
- `latex_book_skeleton/listings/ch06/lst-equivalence-tests-against-the-naive-layer.tex` - Python listing. Implements or sketches: pytest-style allclose test comparing naive and vectorized MoE.. Caption placeholder included. Label: `lst:ch06-equivalence-tests-against-the-naive-layer`.
- `latex_book_skeleton/equations/ch06/eq-equivalence-tests-against-the-naive-layer.tex` - Equation. States: max_abs_diff = max(|y_naive - y_vec|).. Label: `eq:ch06-equivalence-tests-against-the-naive-layer`.

## Code deliverable

Develop the code in `ch06/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Fail if max_abs_diff exceeds tolerance in no-overflow settings.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
