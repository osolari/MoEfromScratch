# Section plan: Chapter 2.3 - Causal self-attention as the context path

## Local objective

Build enough attention to make the baseline a real decoder while keeping MoE focus on the FFN.

## Reader promise

By the end of this section, the reader should be able to explain the mechanism, trace the relevant tensor shapes, implement the minimal code path or pseudocode, and run the listed diagnostic.

## Mini-example

Trace a single attention head with B=1, T=4, D=8.

## Required development flow

1. **Problem opening** - Start with the failure mode or missing capability that makes this section necessary.
2. **Visual anchor** - Include the planned figure immediately after the setup paragraph with `\input{figures/ch02/fig-causal-self-attention-as-the-context-path}`.
3. **Shape-aware mechanics** - Define tensor names and shapes before presenting the equation.
4. **Equation or algorithm** - Include `\input{equations/ch02/eq-causal-self-attention-as-the-context-path}` and explain each symbol in prose.
5. **Implementation listing** - Include `\input{listings/ch02/lst-causal-self-attention-as-the-context-path}` and annotate the non-obvious lines.
6. **Diagnostic check** - Use the table and diagnostic text to make correctness measurable.
7. **Bridge** - End with: After attention mixes context, the dense FFN transforms each token independently.

## Planned artifacts

- `latex_book_skeleton/figures/ch02/fig-causal-self-attention-as-the-context-path.tex` - TikZ. Shows: Causal mask applied to attention scores before softmax.. Caption placeholder included. Label: `fig:ch02-causal-self-attention-as-the-context-path`.
- `latex_book_skeleton/tables/ch02/tab-causal-self-attention-as-the-context-path.tex` - Table. Defines: Q, K, V, score, probability, and output shapes.. Caption placeholder included. Label: `tab:ch02-causal-self-attention-as-the-context-path`.
- `latex_book_skeleton/listings/ch02/lst-causal-self-attention-as-the-context-path.tex` - Python listing. Implements or sketches: Compact multi-head causal attention module.. Caption placeholder included. Label: `lst:ch02-causal-self-attention-as-the-context-path`.
- `latex_book_skeleton/equations/ch02/eq-causal-self-attention-as-the-context-path.tex` - Equation. States: Masked attention softmax(QK^T / sqrt(d_head))V.. Label: `eq:ch02-causal-self-attention-as-the-context-path`.

## Code deliverable

Develop the code in `ch02/01_main-chapter-code/` first as the smallest runnable version. If the logic is reused later, promote it to `common/` only after the section tests pass.

## Diagnostic requirement

Check that a token cannot attend to future positions.

## Acceptance checklist

- [ ] The section starts from a concrete problem, not an abstract definition.
- [ ] The first substantial artifact is a visual schematic.
- [ ] Every tensor has a shape before code appears.
- [ ] The implementation is smoke-testable on CPU.
- [ ] The diagnostic can fail when the implementation is wrong.
- [ ] All artifacts are included through `\input` and no raw `\includegraphics` appears in prose.
- [ ] The final paragraph bridges to the next section or chapter.
