# Section plan: Chapter 7.1 - Expert imbalance as a training problem

## Local objective

Show that a technically correct router can still collapse onto a small number of experts.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Construct a score table where one expert receives most top-k selections.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch07/fig-expert-imbalance-as-a-training-problem}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch07/eq-expert-imbalance-as-a-training-problem}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch07/lst-expert-imbalance-as-a-training-problem}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: An auxiliary loss can reward agreement between probability mass and actual expert load.

## Planned artifacts

- `latex_book_skeleton/figures/ch07/fig-expert-imbalance-as-a-training-problem.tex` - TikZ. Shows: Collapsed routing histogram compared with balanced routing histogram.. Caption placeholder included. Label: `fig:ch07-expert-imbalance-as-a-training-problem`.
- `latex_book_skeleton/tables/ch07/tab-expert-imbalance-as-a-training-problem.tex` - Table. Defines: Symptoms of imbalance and the training behavior they affect.. Caption placeholder included. Label: `tab:ch07-expert-imbalance-as-a-training-problem`.
- `latex_book_skeleton/listings/ch07/lst-expert-imbalance-as-a-training-problem.tex` - Python listing. Implements or sketches: Synthetic imbalance generator for router-score diagnostics.. Caption placeholder included. Label: `lst:ch07-expert-imbalance-as-a-training-problem`.
- `latex_book_skeleton/equations/ch07/eq-expert-imbalance-as-a-training-problem.tex` - Equation. States: Target average load per expert is N*K/E routes.. Label: `eq:ch07-expert-imbalance-as-a-training-problem`.

## Code deliverable

Develop the code in `ch07/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Report max_load/mean_load and number of empty experts.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
