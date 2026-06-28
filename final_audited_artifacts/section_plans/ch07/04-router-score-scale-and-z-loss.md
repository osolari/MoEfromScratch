# Section plan: Chapter 7.4 - Router score scale and z-loss

## Local objective

Introduce a simple regularizer for overly large router logits or scores.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Compare a modest logit row with a very large logit row that creates near-hard routing.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch07/fig-router-score-scale-and-z-loss}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch07/eq-router-score-scale-and-z-loss}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch07/lst-router-score-scale-and-z-loss}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The regularizers become useful only if the diagnostics are visible during training.

## Planned artifacts

- `latex_book_skeleton/figures/ch07/fig-router-score-scale-and-z-loss.tex` - TikZ. Shows: Router logit scale affects probability sharpness before top-k selection.. Caption placeholder included. Label: `fig:ch07-router-score-scale-and-z-loss`.
- `latex_book_skeleton/tables/ch07/tab-router-score-scale-and-z-loss.tex` - Table. Defines: Router regularization options: z-loss, entropy, noise, and clipping.. Caption placeholder included. Label: `tab:ch07-router-score-scale-and-z-loss`.
- `latex_book_skeleton/listings/ch07/lst-router-score-scale-and-z-loss.tex` - Python listing. Implements or sketches: router_z_loss function and optional coefficient in the training config.. Caption placeholder included. Label: `lst:ch07-router-score-scale-and-z-loss`.
- `latex_book_skeleton/equations/ch07/eq-router-score-scale-and-z-loss.tex` - Equation. States: z_loss based on squared logsumexp of router logits.. Label: `eq:ch07-router-score-scale-and-z-loss`.

## Code deliverable

Develop the code in `ch07/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Track router score max, entropy, and z-loss over training.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
