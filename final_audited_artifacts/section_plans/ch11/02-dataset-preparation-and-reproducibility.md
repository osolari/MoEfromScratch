# Section plan: Chapter 11.2 - Dataset preparation and reproducibility

## Local objective

Make dataset setup deterministic and lightweight enough for readers to rerun.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Prepare a small corpus split into train and validation binary or tensor files.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch11/fig-dataset-preparation-and-reproducibility}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch11/eq-dataset-preparation-and-reproducibility}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch11/lst-dataset-preparation-and-reproducibility}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: Training logs must include both language and routing metrics.

## Planned artifacts

- `latex_book_skeleton/figures/ch11/fig-dataset-preparation-and-reproducibility.tex` - TikZ. Shows: Raw text to tokenized train/validation artifacts.. Caption placeholder included. Label: `fig:ch11-dataset-preparation-and-reproducibility`.
- `latex_book_skeleton/tables/ch11/tab-dataset-preparation-and-reproducibility.tex` - Table. Defines: Dataset artifacts, paths, and regeneration commands.. Caption placeholder included. Label: `tab:ch11-dataset-preparation-and-reproducibility`.
- `latex_book_skeleton/listings/ch11/lst-dataset-preparation-and-reproducibility.tex` - Python listing. Implements or sketches: prepare.py script with deterministic split and saved metadata.. Caption placeholder included. Label: `lst:ch11-dataset-preparation-and-reproducibility`.
- `latex_book_skeleton/equations/ch11/eq-dataset-preparation-and-reproducibility.tex` - Equation. States: Train/validation split ratio and token count definitions.. Label: `eq:ch11-dataset-preparation-and-reproducibility`.

## Code deliverable

Develop the code in `ch11/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Print token counts, split sizes, and a decoded sample from each split.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
