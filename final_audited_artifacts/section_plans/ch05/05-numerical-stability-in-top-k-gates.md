# Section plan: Chapter 5.5 - Numerical stability in top-k gates

## Local objective

Prevent gate normalization edge cases before they become training bugs.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Use tiny selected scores and demonstrate epsilon-safe normalization.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch05/fig-numerical-stability-in-top-k-gates}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch05/eq-numerical-stability-in-top-k-gates}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch05/lst-numerical-stability-in-top-k-gates}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Now that top-2 is correct, we can rewrite the dispatch to scale beyond tiny examples.

## Planned artifacts

- `latex_book_skeleton/figures/ch05/fig-numerical-stability-in-top-k-gates.tex` - TikZ. Shows: Gate normalization failure and epsilon-stabilized path.. Caption placeholder included. Label: `fig:ch05-numerical-stability-in-top-k-gates`.
- `latex_book_skeleton/tables/ch05/tab-numerical-stability-in-top-k-gates.tex` - Table. Defines: Potential failures: zero sums, dtype mismatch, overflow, and unintended detached gates.. Caption placeholder included. Label: `tab:ch05-numerical-stability-in-top-k-gates`.
- `latex_book_skeleton/listings/ch05/lst-numerical-stability-in-top-k-gates.tex` - Python listing. Implements or sketches: stable_normalize_selected_scores function with epsilon and dtype checks.. Caption placeholder included. Label: `lst:ch05-numerical-stability-in-top-k-gates`.
- `latex_book_skeleton/equations/ch05/eq-numerical-stability-in-top-k-gates.tex` - Equation. States: gate = selected_scores / clamp(sum(selected_scores), eps).. Label: `eq:ch05-numerical-stability-in-top-k-gates`.

## Code deliverable

Develop the code in `ch05/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Unit tests for finite gates and gradients under small scores.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
