# Section plan: Chapter 12.3 - Compute, memory, and active-parameter accounting

## Local objective

Give readers a sober way to discuss total parameters, active parameters, and practical memory costs.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Compare dense FFN, 16x2 MoE, and 64x6 teaching config parameter counts.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch12/fig-compute-memory-and-active-parameter-accounting}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch12/eq-compute-memory-and-active-parameter-accounting}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch12/lst-compute-memory-and-active-parameter-accounting}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: At production scale, experts are often spread across devices, introducing communication.

## Planned artifacts

- `latex_book_skeleton/figures/ch12/fig-compute-memory-and-active-parameter-accounting.tex` - TikZ. Shows: Stacked bars for total parameters and active parameters per token.. Caption placeholder included. Label: `fig:ch12-compute-memory-and-active-parameter-accounting`.
- `latex_book_skeleton/tables/ch12/tab-compute-memory-and-active-parameter-accounting.tex` - Table. Defines: Total parameters, active parameters, estimated activation memory, and expert calls by config.. Caption placeholder included. Label: `tab:ch12-compute-memory-and-active-parameter-accounting`.
- `latex_book_skeleton/listings/ch12/lst-compute-memory-and-active-parameter-accounting.tex` - Python listing. Implements or sketches: estimate_moe_compute.py producing parameter and active-compute estimates.. Caption placeholder included. Label: `lst:ch12-compute-memory-and-active-parameter-accounting`.
- `latex_book_skeleton/equations/ch12/eq-compute-memory-and-active-parameter-accounting.tex` - Equation. States: Active expert FFN parameters per token approximately K times one routed expert plus shared experts.. Label: `eq:ch12-compute-memory-and-active-parameter-accounting`.

## Code deliverable

Develop the code in `ch12/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Check estimates against model.count_parameters breakdown.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
