# Section plan: Chapter 2.6 - Baseline diagnostics and comparison slots

## Local objective

Prepare diagnostic hooks that will later compare dense and sparse models fairly.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Create a metrics dictionary with loss, tokens/sec, parameter count, and activation estimate.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch02/fig-baseline-diagnostics-and-comparison-slots}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch02/eq-baseline-diagnostics-and-comparison-slots}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch02/lst-baseline-diagnostics-and-comparison-slots}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The next chapter replaces the dense FFN with a small expert bank and a router.

## Planned artifacts

- `latex_book_skeleton/figures/ch02/fig-baseline-diagnostics-and-comparison-slots.tex` - TikZ. Shows: Dashboard placeholder for loss curves, parameter counts, and future routing metrics.. Caption placeholder included. Label: `fig:ch02-baseline-diagnostics-and-comparison-slots`.
- `latex_book_skeleton/tables/ch02/tab-baseline-diagnostics-and-comparison-slots.tex` - Table. Defines: Metrics available now versus metrics added by MoE layers.. Caption placeholder included. Label: `tab:ch02-baseline-diagnostics-and-comparison-slots`.
- `latex_book_skeleton/listings/ch02/lst-baseline-diagnostics-and-comparison-slots.tex` - Python listing. Implements or sketches: count_parameters and estimate_active_parameters helper functions.. Caption placeholder included. Label: `lst:ch02-baseline-diagnostics-and-comparison-slots`.
- `latex_book_skeleton/equations/ch02/eq-baseline-diagnostics-and-comparison-slots.tex` - Equation. States: Perplexity = exp(validation cross-entropy).. Label: `eq:ch02-baseline-diagnostics-and-comparison-slots`.

## Code deliverable

Develop the code in `ch02/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Write the first baseline row in the experiment comparison table.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
