# Section plan: Chapter 11.1 - Experiment design for a from-scratch book

## Local objective

Set realistic expectations for small-data experiments and define what can and cannot be concluded.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Use three smoke-scale runs to compare mechanics, not state-of-the-art quality.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch11/fig-experiment-design-for-a-from-scratch-book}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch11/eq-experiment-design-for-a-from-scratch-book}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch11/lst-experiment-design-for-a-from-scratch-book}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The data pipeline needs a repeatable preparation script.

## Planned artifacts

- `latex_book_skeleton/figures/ch11/fig-experiment-design-for-a-from-scratch-book.tex` - TikZ. Shows: Experiment funnel from smoke tests to short training runs to optional longer ablations.. Caption placeholder included. Label: `fig:ch11-experiment-design-for-a-from-scratch-book`.
- `latex_book_skeleton/tables/ch11/tab-experiment-design-for-a-from-scratch-book.tex` - Table. Defines: Claim types allowed by each experiment scale.. Caption placeholder included. Label: `tab:ch11-experiment-design-for-a-from-scratch-book`.
- `latex_book_skeleton/listings/ch11/lst-experiment-design-for-a-from-scratch-book.tex` - Python listing. Implements or sketches: Experiment manifest YAML with seeds, configs, and output directories.. Caption placeholder included. Label: `lst:ch11-experiment-design-for-a-from-scratch-book`.
- `latex_book_skeleton/equations/ch11/eq-experiment-design-for-a-from-scratch-book.tex` - Equation. States: Report mean and range across seeds when multiple seeds are used.. Label: `eq:ch11-experiment-design-for-a-from-scratch-book`.

## Code deliverable

Develop the code in `ch11/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Check that every experiment saves config, seed, logs, and git/code snapshot note.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
