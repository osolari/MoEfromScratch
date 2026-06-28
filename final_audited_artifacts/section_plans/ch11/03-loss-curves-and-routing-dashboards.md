# Section plan: Chapter 11.3 - Loss curves and routing dashboards

## Local objective

Create consistent plots that make model behavior inspectable after every run.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Plot validation loss, load balance score, entropy, and drop rate from one JSONL log.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch11/fig-loss-curves-and-routing-dashboards}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch11/eq-loss-curves-and-routing-dashboards}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch11/lst-loss-curves-and-routing-dashboards}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: With dashboards ready, ablation experiments can compare design choices.

## Planned artifacts

- `latex_book_skeleton/figures/ch11/fig-loss-curves-and-routing-dashboards.tex` - TikZ. Shows: Standard diagnostic dashboard layout for a chapter experiment.. Caption placeholder included. Label: `fig:ch11-loss-curves-and-routing-dashboards`.
- `latex_book_skeleton/tables/ch11/tab-loss-curves-and-routing-dashboards.tex` - Table. Defines: Plot names, source metrics, and interpretation cautions.. Caption placeholder included. Label: `tab:ch11-loss-curves-and-routing-dashboards`.
- `latex_book_skeleton/listings/ch11/lst-loss-curves-and-routing-dashboards.tex` - Python listing. Implements or sketches: plot_experiment_dashboard.py reading logs and saving PDF figures.. Caption placeholder included. Label: `lst:ch11-loss-curves-and-routing-dashboards`.
- `latex_book_skeleton/equations/ch11/eq-loss-curves-and-routing-dashboards.tex` - Equation. States: Load-balance score based on coefficient of variation across expert loads.. Label: `eq:ch11-loss-curves-and-routing-dashboards`.

## Code deliverable

Develop the code in `ch11/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Save dashboard figures through LaTeX wrappers, never raw includegraphics in prose.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
