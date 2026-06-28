# Section plan: Chapter 6.1 - Flattened tokens as the dispatch unit

## Local objective

Standardize on N=B*T flattened tokens so routing code ignores batch layout until the final reshape.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Flatten B=2, T=3, D=4 into N=6 token rows and recover B,T,D afterward.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch06/fig-flattened-tokens-as-the-dispatch-unit}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch06/eq-flattened-tokens-as-the-dispatch-unit}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch06/lst-flattened-tokens-as-the-dispatch-unit}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Flat token rows can be sorted or bucketed by expert assignment.

## Planned artifacts

- `latex_book_skeleton/figures/ch06/fig-flattened-tokens-as-the-dispatch-unit.tex` - TikZ. Shows: Batch-sequence grid flattened into a token table for routing.. Caption placeholder included. Label: `fig:ch06-flattened-tokens-as-the-dispatch-unit`.
- `latex_book_skeleton/tables/ch06/tab-flattened-tokens-as-the-dispatch-unit.tex` - Table. Defines: Mapping between batch index, time index, flat index, and token vector.. Caption placeholder included. Label: `tab:ch06-flattened-tokens-as-the-dispatch-unit`.
- `latex_book_skeleton/listings/ch06/lst-flattened-tokens-as-the-dispatch-unit.tex` - Python listing. Implements or sketches: flatten_tokens and unflatten_tokens helper functions.. Caption placeholder included. Label: `lst:ch06-flattened-tokens-as-the-dispatch-unit`.
- `latex_book_skeleton/equations/ch06/eq-flattened-tokens-as-the-dispatch-unit.tex` - Equation. States: n = b*T + t maps (b,t) to flat token index.. Label: `eq:ch06-flattened-tokens-as-the-dispatch-unit`.

## Code deliverable

Develop the code in `ch06/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Round-trip flatten/unflatten equality check.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
