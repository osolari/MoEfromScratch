# Section plan: Chapter 7.5 - Routing dashboards and training logs

## Local objective

Create the standard diagnostic views used for every later MoE experiment.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Log one training batch with load histogram, gate entropy, drop count, and loss terms.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch07/fig-routing-dashboards-and-training-logs}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch07/eq-routing-dashboards-and-training-logs}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch07/lst-routing-dashboards-and-training-logs}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: The next chapter changes the expert architecture itself by adding shared and fine-grained routed experts.

## Planned artifacts

- `latex_book_skeleton/figures/ch07/fig-routing-dashboards-and-training-logs.tex` - TikZ. Shows: Dashboard layout with loss curve, expert load histogram, gate entropy, and drop rate.. Caption placeholder included. Label: `fig:ch07-routing-dashboards-and-training-logs`.
- `latex_book_skeleton/tables/ch07/tab-routing-dashboards-and-training-logs.tex` - Table. Defines: Metric names, tensor source, frequency, and expected range.. Caption placeholder included. Label: `tab:ch07-routing-dashboards-and-training-logs`.
- `latex_book_skeleton/listings/ch07/lst-routing-dashboards-and-training-logs.tex` - Python listing. Implements or sketches: collect_router_metrics and plot_router_dashboard helpers.. Caption placeholder included. Label: `lst:ch07-routing-dashboards-and-training-logs`.
- `latex_book_skeleton/equations/ch07/eq-routing-dashboards-and-training-logs.tex` - Equation. States: Routing entropy over normalized selected gates.. Label: `eq:ch07-routing-dashboards-and-training-logs`.

## Code deliverable

Develop the code in `ch07/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Generate a dashboard PDF or image after a short smoke run.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
