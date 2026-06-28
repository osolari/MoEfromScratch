# Section plan: Chapter 4.4 - Capacity and dropped tokens

## Local objective

Introduce the capacity factor and the consequences of too many tokens choosing the same expert.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Set capacity=2 for four experts and show what happens when four tokens select expert 0.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch04/fig-capacity-and-dropped-tokens}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch04/eq-capacity-and-dropped-tokens}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch04/lst-capacity-and-dropped-tokens}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Capacity exposes routing imbalance; histograms make the imbalance easy to see.

## Planned artifacts

- `latex_book_skeleton/figures/ch04/fig-capacity-and-dropped-tokens.tex` - TikZ. Shows: Overloaded expert bucket with accepted and dropped token slots.. Caption placeholder included. Label: `fig:ch04-capacity-and-dropped-tokens`.
- `latex_book_skeleton/tables/ch04/tab-capacity-and-dropped-tokens.tex` - Table. Defines: Capacity factor, expert capacity, accepted tokens, dropped tokens, and residual fallback.. Caption placeholder included. Label: `tab:ch04-capacity-and-dropped-tokens`.
- `latex_book_skeleton/listings/ch04/lst-capacity-and-dropped-tokens.tex` - Python listing. Implements or sketches: Capacity-aware top-1 dispatch with dropped-token accounting.. Caption placeholder included. Label: `lst:ch04-capacity-and-dropped-tokens`.
- `latex_book_skeleton/equations/ch04/eq-capacity-and-dropped-tokens.tex` - Equation. States: capacity = ceil(capacity_factor * N / E).. Label: `eq:ch04-capacity-and-dropped-tokens`.

## Code deliverable

Develop the code in `ch04/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Report dropped_token_count and per-expert accepted counts.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
