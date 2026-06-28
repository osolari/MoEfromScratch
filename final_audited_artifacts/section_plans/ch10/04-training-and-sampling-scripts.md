# Section plan: Chapter 10.4 - Training and sampling scripts

## Local objective

Create runnable scripts that match the source codebase style: minimal, readable, and chapter-scoped.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Run train.py with a smoke config and sample.py from the saved checkpoint.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch10/fig-training-and-sampling-scripts}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch10/eq-training-and-sampling-scripts}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch10/lst-training-and-sampling-scripts}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: A full model needs full-model smoke tests before experiments are trusted.

## Planned artifacts

- `latex_book_skeleton/figures/ch10/fig-training-and-sampling-scripts.tex` - TikZ. Shows: Script workflow from config to training to checkpoint to sample text.. Caption placeholder included. Label: `fig:ch10-training-and-sampling-scripts`.
- `latex_book_skeleton/tables/ch10/tab-training-and-sampling-scripts.tex` - Table. Defines: Command-line arguments and their defaults.. Caption placeholder included. Label: `tab:ch10-training-and-sampling-scripts`.
- `latex_book_skeleton/listings/ch10/lst-training-and-sampling-scripts.tex` - Python listing. Implements or sketches: train.py main function with config loading, training loop, checkpointing, and sampling hook.. Caption placeholder included. Label: `lst:ch10-training-and-sampling-scripts`.
- `latex_book_skeleton/equations/ch10/eq-training-and-sampling-scripts.tex` - Equation. States: Checkpoint state includes model, optimizer, config, and router bias buffers.. Label: `eq:ch10-training-and-sampling-scripts`.

## Code deliverable

Develop the code in `ch10/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Verify checkpoint reload produces logits of the same shape.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
