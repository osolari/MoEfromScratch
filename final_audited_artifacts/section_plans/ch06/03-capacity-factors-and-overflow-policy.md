# Section plan: Chapter 6.3 - Capacity factors and overflow policy

## Local objective

Explain how capacity controls memory and what the implementation does with overflow routes.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Use N=12, E=4, K=2 and capacity factors 1.0 and 1.25.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch06/fig-capacity-factors-and-overflow-policy}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch06/eq-capacity-factors-and-overflow-policy}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch06/lst-capacity-factors-and-overflow-policy}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: After expert batches are processed, outputs must be unpacked and combined.

## Planned artifacts

- `latex_book_skeleton/figures/ch06/fig-capacity-factors-and-overflow-policy.tex` - TikZ. Shows: Capacity slots per expert with accepted, padded, and overflow routes.. Caption placeholder included. Label: `fig:ch06-capacity-factors-and-overflow-policy`.
- `latex_book_skeleton/tables/ch06/tab-capacity-factors-and-overflow-policy.tex` - Table. Defines: Capacity factor scenarios and their accepted route counts.. Caption placeholder included. Label: `tab:ch06-capacity-factors-and-overflow-policy`.
- `latex_book_skeleton/listings/ch06/lst-capacity-factors-and-overflow-policy.tex` - Python listing. Implements or sketches: compute_expert_capacity and overflow mask code.. Caption placeholder included. Label: `lst:ch06-capacity-factors-and-overflow-policy`.
- `latex_book_skeleton/equations/ch06/eq-capacity-factors-and-overflow-policy.tex` - Equation. States: capacity = ceil(capacity_factor * N*K / E).. Label: `eq:ch06-capacity-factors-and-overflow-policy`.

## Code deliverable

Develop the code in `ch06/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Log overflow route count and overflow fraction.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
