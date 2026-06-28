# Section plan: Chapter 6.4 - Unpacking and weighted combine

## Local objective

Scatter expert-batch outputs back to token rows and apply route weights correctly.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

One token receives two routes; one overflow route is skipped while the accepted route contributes.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch06/fig-unpacking-and-weighted-combine}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch06/eq-unpacking-and-weighted-combine}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch06/lst-unpacking-and-weighted-combine}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The implementation is faster, but correctness tests must guard against silent routing mistakes.

## Planned artifacts

- `latex_book_skeleton/figures/ch06/fig-unpacking-and-weighted-combine.tex` - TikZ. Shows: Expert outputs unpacked through token and slot indices into routed_out.. Caption placeholder included. Label: `fig:ch06-unpacking-and-weighted-combine`.
- `latex_book_skeleton/tables/ch06/tab-unpacking-and-weighted-combine.tex` - Table. Defines: Accepted route table: token, expert, slot, gate, and output contribution.. Caption placeholder included. Label: `tab:ch06-unpacking-and-weighted-combine`.
- `latex_book_skeleton/listings/ch06/lst-unpacking-and-weighted-combine.tex` - Python listing. Implements or sketches: unpack_expert_outputs function using index_add or scatter_add.. Caption placeholder included. Label: `lst:ch06-unpacking-and-weighted-combine`.
- `latex_book_skeleton/equations/ch06/eq-unpacking-and-weighted-combine.tex` - Equation. States: routed_out[token] += gate * expert_out[expert, slot].. Label: `eq:ch06-unpacking-and-weighted-combine`.

## Code deliverable

Develop the code in `ch06/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Compare vectorized output to naive output when capacity is large enough for no overflow.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
