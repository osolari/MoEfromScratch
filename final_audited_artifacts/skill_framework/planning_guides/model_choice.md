# Model choice - MiniDeepSeekMoE

## One-sentence choice

The book should build **MiniDeepSeekMoE**, a small decoder-only causal language model whose dense FFN blocks are progressively replaced by sparse MoE blocks with routed experts, shared experts, and bias-based load balancing.

## Why this is the right center of gravity

The source book's strategy is not to clone every production detail first. It starts with the failure mode, isolates the architectural idea, turns the idea into a diagram, turns the diagram into equations, and then turns the equations into from-scratch code. MiniDeepSeekMoE fits that strategy exactly.

A full DeepSeek-V3 clone would make the book too broad. It would force the reader to learn MLA, distributed all-to-all routing, FP8 training, multi-token prediction, production kernels, and large-scale data pipelines before the MoE idea has been made clear. MiniDeepSeekMoE keeps those links visible but makes the MoE mechanism the central build.

## Architecture summary

MiniDeepSeekMoE contains the usual causal language-model shell:

1. token and position embeddings,
2. repeated decoder blocks,
3. causal self-attention,
4. an MoE feed-forward replacement,
5. final normalization and language-model head.

The MoE replacement is the main subject of the book. It consists of:

- a router that scores each token against routed experts,
- top-k expert selection,
- sparse token dispatch,
- weighted expert output combination,
- shared experts that always process every token,
- an optional capacity mechanism for older-style MoE chapters,
- a final auxiliary-loss-free dynamic bias update in the DeepSeek-style chapters.

## Final MoE layer formula

For token representation `x_t`, the final reference MoE layer should be written conceptually as:

```text
y_t = x_t
    + sum_s SharedExpert_s(x_t)
    + sum_{i in TopK(score(x_t) + b)} gate_i(x_t) RoutedExpert_i(x_t)
```

The selection uses the biased scores, but the output gates are computed from the original unbiased selected scores. This distinction should be emphasized because it is the cleanest way to explain the DeepSeek-style bias update: the bias affects who is selected, not how much each selected expert contributes after selection.

## Progressive development path

MiniDeepSeekMoE should not appear fully formed in Chapter 1. It should be assembled through milestones:

1. Dense FFN baseline.
2. Naive all-experts ensemble, to show why dense expert evaluation is too expensive.
3. Top-1 sparse MoE, to introduce routing and dispatch.
4. Top-2 sparse MoE, to introduce weighted combinations.
5. Auxiliary/load-balancing losses and capacity.
6. Shared experts and fine-grained routed experts.
7. Bias-based balancing and router diagnostics.
8. Full MiniDeepSeekMoE LM training.
9. Systems-aware dispatch and inference considerations.

This lets the reader understand every part of the final model before the full implementation appears.
