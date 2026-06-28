# Section plan: Chapter 9.3 - Biased selection and unbiased combine

## Local objective

Implement the central invariant of the final reference model.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

A token selects experts using score+bias, then gates are computed from the original selected scores.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch09/fig-biased-selection-and-unbiased-combine}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch09/eq-biased-selection-and-unbiased-combine}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch09/lst-biased-selection-and-unbiased-combine}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The bias vector needs an update rule based on observed expert load.

## Planned artifacts

- `latex_book_skeleton/figures/ch09/fig-biased-selection-and-unbiased-combine.tex` - TikZ. Shows: Two score streams: biased scores for top-k, unbiased scores for gate normalization.. Caption placeholder included. Label: `fig:ch09-biased-selection-and-unbiased-combine`.
- `latex_book_skeleton/tables/ch09/tab-biased-selection-and-unbiased-combine.tex` - Table. Defines: Selection tensor versus combine tensor and where each is used.. Caption placeholder included. Label: `tab:ch09-biased-selection-and-unbiased-combine`.
- `latex_book_skeleton/listings/ch09/lst-biased-selection-and-unbiased-combine.tex` - Python listing. Implements or sketches: Router forward pass returning topk_idx from biased scores and gates from unbiased selected scores.. Caption placeholder included. Label: `lst:ch09-biased-selection-and-unbiased-combine`.
- `latex_book_skeleton/equations/ch09/eq-biased-selection-and-unbiased-combine.tex` - Equation. States: idx = topk(score + b); gate = normalize(score[idx]).. Label: `eq:ch09-biased-selection-and-unbiased-combine`.

## Code deliverable

Develop the code in `ch09/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Unit test that changing bias can change expert IDs while gate values still come from raw scores.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
