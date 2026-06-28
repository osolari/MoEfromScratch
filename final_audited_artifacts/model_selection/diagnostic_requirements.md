# Diagnostic requirements for the chosen model

## Why diagnostics are mandatory

A sparse MoE can run and still be wrong. The router may collapse to a few experts, gates may be normalized incorrectly, capacity can silently drop tokens, and the dispatch/combine path can return the right shape while mixing outputs into the wrong token rows. The book must therefore treat diagnostics as part of the model, not as optional plots.

## Required diagnostics

| Diagnostic | Purpose | Artifact type |
|---|---|---|
| Shape trace table | Verify each tensor contract | table |
| Expert load histogram | Reveal overused and unused experts | generated PDF figure wrapper |
| Router probability heatmap | Show token-to-expert preference patterns | generated PDF figure wrapper |
| Gate-sum check | Confirm selected gates sum to 1 per token | code listing and table |
| Capacity overflow table | Track dropped tokens when capacity is enabled | table |
| Auxiliary-loss curve | Show effect of soft balance objective | plot |
| Bias value trace | Show self-correcting dynamic balancing | plot |
| Standard vs DeepSeek-style comparison | Demonstrate the payoff of shared experts and no-aux bias | table and plot |

## Required sanity checks

- Output shape equals input shape for every MoE layer.
- Each token selects exactly `K` routed experts unless a deliberate capacity/drop rule changes the effective count.
- Gates over selected routed experts sum to 1.
- Router bias is not in `model.parameters()`.
- Router bias affects selection but not the combine weights.
- Expert load counts are computed from selected indices, not from raw probability mass.
- Capacity calculations use flattened token count and top-k count consistently.

## Planned placeholder artifacts for Phase 4 onward

```text
figures/ch03/fig-topk-mask.tex
figures/ch04/fig-expert-load-histogram.tex
figures/ch06/fig-bias-feedback-loop.tex
tables/ch03/tab-routing-shapes.tex
tables/ch04/tab-load-balance-loss-terms.tex
listings/ch03/lst-topk-router.tex
listings/ch05/lst-sparse-dispatcher.tex
listings/ch06/lst-bias-update.tex
```
