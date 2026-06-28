---
name: moe-models-from-scratch-developer
description: use when planning, drafting, editing, or proofreading the latex-first technical book moe models from scratch. triggers include developing individual sections, enforcing standalone latex artifact wrappers, maintaining the minideepseekmoe model contract, generating tikz figure table listing equation plans, coordinating chapter code, or using the included section-development briefs.
---

# MoE Models from Scratch Developer

Use this skill to develop *MoE Models from Scratch* in LaTeX. The skill coordinates the overall book structure and points to section-specific development briefs that should be loaded only for the section currently being written.

## Start here

1. Identify the target section by chapter and section number.
2. Load the corresponding file under `references/section-skills/chXX/`.
3. Draft only the target section's `.tex` prose and update only its planned artifact wrappers.
4. Compile the LaTeX project and run the section's diagnostic or smoke test.
5. Proofread against `references/proofread-checklist.md`.

## Non-negotiable development rules

- Develop the production book in LaTeX.
- Keep section prose in the planned `latex_book_skeleton/chapters/chXX/sections/*.tex` file.
- Do not inline `figure`, `table`, `lstlisting`, or `equation` environments in section prose.
- Include every planned artifact through a standalone `.tex` wrapper and `\input{...}`.
- Do not allow figures or tables to float into later sections; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active in the compiled LaTeX project.
- Use TikZ for mechanism schematics.
- Use generated PDF assets only for plots, dashboards, and diagnostics; include them through figure wrappers.
- Preserve the MiniDeepSeekMoE invariant wherever router bias appears: router bias affects selection only; final combine weights are computed from unbiased selected scores.
- Follow the teaching flow: problem opening -> visual anchor -> tensor/math mechanics -> implementation listing -> diagnostic -> bridge.
- Avoid broad surveys inside local sections; make every section falsifiable with its diagnostic.


## Reference model invariant

Preserve the `MiniDeepSeekMoE-16x2` contract:

```text
y_t = x_t
    + sum(shared_experts(x_t))
    + sum_{i in topk(score_t + bias)} gate_i routed_expert_i(x_t)
```

The router bias vector can affect expert selection. It must not be used to compute the final normalized combine weights.

## References to load as needed

### Global references

- `references/overall-structure.md`
- `references/theme-and-artifact-contract.md`
- `references/proofread-checklist.md`
- `references/codebase-development-contract.md`
- `references/separate-session-workflow.md`
- `references/reference-model-spec.md`
- `references/section-skill-index.csv`

### Chapter guides

- Chapter 1: `From dense compute to conditional compute` -> `references/chapter-skills/ch01.md`
- Chapter 2: `A dense Transformer baseline from scratch` -> `references/chapter-skills/ch02.md`
- Chapter 3: `Experts, routers, and the first MoE layer` -> `references/chapter-skills/ch03.md`
- Chapter 4: `Top-1 routing and Switch-style dispatch` -> `references/chapter-skills/ch04.md`
- Chapter 5: `Top-2 routing and weighted expert combination` -> `references/chapter-skills/ch05.md`
- Chapter 6: `Vectorized dispatch, capacity, and routing efficiency` -> `references/chapter-skills/ch06.md`
- Chapter 7: `Router training and load-balancing losses` -> `references/chapter-skills/ch07.md`
- Chapter 8: `Shared experts and fine-grained routed experts` -> `references/chapter-skills/ch08.md`
- Chapter 9: `Auxiliary-loss-free load balancing` -> `references/chapter-skills/ch09.md`
- Chapter 10: `Assembling MiniDeepSeekMoE end to end` -> `references/chapter-skills/ch10.md`
- Chapter 11: `Training, diagnostics, and controlled experiments` -> `references/chapter-skills/ch11.md`
- Chapter 12: `Inference, performance, and scaling beyond the toy model` -> `references/chapter-skills/ch12.md`

### Section-specific briefs

- Section 1.1: `The dense FFN bottleneck` -> `references/section-skills/ch01/01-the-dense-ffn-bottleneck.md`
- Section 1.2: `Conditional compute as the central idea` -> `references/section-skills/ch01/02-conditional-compute-as-the-central-idea.md`
- Section 1.3: `A tiny routing story` -> `references/section-skills/ch01/03-a-tiny-routing-story.md`
- Section 1.4: `What from scratch means for this book` -> `references/section-skills/ch01/04-what-from-scratch-means-for-this-book.md`
- Section 1.5: `The MiniDeepSeekMoE build ladder` -> `references/section-skills/ch01/05-the-minideepseekmoe-build-ladder.md`
- Section 1.6: `Chapter summary and handoff` -> `references/section-skills/ch01/06-chapter-summary-and-handoff.md`
- Section 2.1: `Dataset and token batches` -> `references/section-skills/ch02/01-dataset-and-token-batches.md`
- Section 2.2: `Token and position embeddings` -> `references/section-skills/ch02/02-token-and-position-embeddings.md`
- Section 2.3: `Causal self-attention as the context path` -> `references/section-skills/ch02/03-causal-self-attention-as-the-context-path.md`
- Section 2.4: `Dense feed-forward block as the replacement target` -> `references/section-skills/ch02/04-dense-feed-forward-block-as-the-replacement-target.md`
- Section 2.5: `Training loop and sampling baseline` -> `references/section-skills/ch02/05-training-loop-and-sampling-baseline.md`
- Section 2.6: `Baseline diagnostics and comparison slots` -> `references/section-skills/ch02/06-baseline-diagnostics-and-comparison-slots.md`
- Section 3.1: `Expert MLPs as named FFNs` -> `references/section-skills/ch03/01-expert-mlps-as-named-ffns.md`
- Section 3.2: `Router scores and tensor shapes` -> `references/section-skills/ch03/02-router-scores-and-tensor-shapes.md`
- Section 3.3: `Top-k selection without dispatch` -> `references/section-skills/ch03/03-top-k-selection-without-dispatch.md`
- Section 3.4: `Naive token-by-token dispatch` -> `references/section-skills/ch03/04-naive-token-by-token-dispatch.md`
- Section 3.5: `Shape and gradient checks` -> `references/section-skills/ch03/05-shape-and-gradient-checks.md`
- Section 3.6: `Chapter summary and handoff` -> `references/section-skills/ch03/06-chapter-summary-and-handoff.md`
- Section 4.1: `Why top-1 routing is the simplest sparse case` -> `references/section-skills/ch04/01-why-top-1-routing-is-the-simplest-sparse-case.md`
- Section 4.2: `Assignment masks and expert buckets` -> `references/section-skills/ch04/02-assignment-masks-and-expert-buckets.md`
- Section 4.3: `Dispatching tokens to selected experts` -> `references/section-skills/ch04/03-dispatching-tokens-to-selected-experts.md`
- Section 4.4: `Capacity and dropped tokens` -> `references/section-skills/ch04/04-capacity-and-dropped-tokens.md`
- Section 4.5: `Load histograms and failure modes` -> `references/section-skills/ch04/05-load-histograms-and-failure-modes.md`
- Section 4.6: `Chapter summary and handoff` -> `references/section-skills/ch04/06-chapter-summary-and-handoff.md`
- Section 5.1: `Why top-2 changes the routing story` -> `references/section-skills/ch05/01-why-top-2-changes-the-routing-story.md`
- Section 5.2: `Normalizing selected router scores` -> `references/section-skills/ch05/02-normalizing-selected-router-scores.md`
- Section 5.3: `Dispatch for two expert paths per token` -> `references/section-skills/ch05/03-dispatch-for-two-expert-paths-per-token.md`
- Section 5.4: `Comparing top-1 and top-2 diagnostics` -> `references/section-skills/ch05/04-comparing-top-1-and-top-2-diagnostics.md`
- Section 5.5: `Numerical stability in top-k gates` -> `references/section-skills/ch05/05-numerical-stability-in-top-k-gates.md`
- Section 5.6: `Chapter summary and handoff` -> `references/section-skills/ch05/06-chapter-summary-and-handoff.md`
- Section 6.1: `Flattened tokens as the dispatch unit` -> `references/section-skills/ch06/01-flattened-tokens-as-the-dispatch-unit.md`
- Section 6.2: `Expert batch construction` -> `references/section-skills/ch06/02-expert-batch-construction.md`
- Section 6.3: `Capacity factors and overflow policy` -> `references/section-skills/ch06/03-capacity-factors-and-overflow-policy.md`
- Section 6.4: `Unpacking and weighted combine` -> `references/section-skills/ch06/04-unpacking-and-weighted-combine.md`
- Section 6.5: `Equivalence tests against the naive layer` -> `references/section-skills/ch06/05-equivalence-tests-against-the-naive-layer.md`
- Section 6.6: `Chapter summary and handoff` -> `references/section-skills/ch06/06-chapter-summary-and-handoff.md`
- Section 7.1: `Expert imbalance as a training problem` -> `references/section-skills/ch07/01-expert-imbalance-as-a-training-problem.md`
- Section 7.2: `Auxiliary load-balancing loss` -> `references/section-skills/ch07/02-auxiliary-load-balancing-loss.md`
- Section 7.3: `Integrating auxiliary loss into training` -> `references/section-skills/ch07/03-integrating-auxiliary-loss-into-training.md`
- Section 7.4: `Router score scale and z-loss` -> `references/section-skills/ch07/04-router-score-scale-and-z-loss.md`
- Section 7.5: `Routing dashboards and training logs` -> `references/section-skills/ch07/05-routing-dashboards-and-training-logs.md`
- Section 7.6: `Chapter summary and handoff` -> `references/section-skills/ch07/06-chapter-summary-and-handoff.md`
- Section 8.1: `The role of shared experts` -> `references/section-skills/ch08/01-the-role-of-shared-experts.md`
- Section 8.2: `Fine-grained routed expert segmentation` -> `references/section-skills/ch08/02-fine-grained-routed-expert-segmentation.md`
- Section 8.3: `The MiniDeepSeekMoE layer contract` -> `references/section-skills/ch08/03-the-minideepseekmoe-layer-contract.md`
- Section 8.4: `Combining shared and routed outputs` -> `references/section-skills/ch08/04-combining-shared-and-routed-outputs.md`
- Section 8.5: `Specialization diagnostics` -> `references/section-skills/ch08/05-specialization-diagnostics.md`
- Section 8.6: `Chapter summary and handoff` -> `references/section-skills/ch08/06-chapter-summary-and-handoff.md`
- Section 9.1: `The limitation of auxiliary balancing` -> `references/section-skills/ch09/01-the-limitation-of-auxiliary-balancing.md`
- Section 9.2: `Router bias as non-trainable state` -> `references/section-skills/ch09/02-router-bias-as-non-trainable-state.md`
- Section 9.3: `Biased selection and unbiased combine` -> `references/section-skills/ch09/03-biased-selection-and-unbiased-combine.md`
- Section 9.4: `Dynamic bias update from expert load` -> `references/section-skills/ch09/04-dynamic-bias-update-from-expert-load.md`
- Section 9.5: `Comparing balancing methods` -> `references/section-skills/ch09/05-comparing-balancing-methods.md`
- Section 9.6: `Chapter summary and handoff` -> `references/section-skills/ch09/06-chapter-summary-and-handoff.md`
- Section 10.1: `Configuration objects and model variants` -> `references/section-skills/ch10/01-configuration-objects-and-model-variants.md`
- Section 10.2: `Decoder block with dense prefix and MoE layers` -> `references/section-skills/ch10/02-decoder-block-with-dense-prefix-and-moe-layers.md`
- Section 10.3: `Forward pass outputs and loss dictionary` -> `references/section-skills/ch10/03-forward-pass-outputs-and-loss-dictionary.md`
- Section 10.4: `Training and sampling scripts` -> `references/section-skills/ch10/04-training-and-sampling-scripts.md`
- Section 10.5: `Full-model smoke tests` -> `references/section-skills/ch10/05-full-model-smoke-tests.md`
- Section 10.6: `Chapter summary and handoff` -> `references/section-skills/ch10/06-chapter-summary-and-handoff.md`
- Section 11.1: `Experiment design for a from-scratch book` -> `references/section-skills/ch11/01-experiment-design-for-a-from-scratch-book.md`
- Section 11.2: `Dataset preparation and reproducibility` -> `references/section-skills/ch11/02-dataset-preparation-and-reproducibility.md`
- Section 11.3: `Loss curves and routing dashboards` -> `references/section-skills/ch11/03-loss-curves-and-routing-dashboards.md`
- Section 11.4: `Ablation matrix: dense, top-1, top-2, shared, and bias-balanced` -> `references/section-skills/ch11/04-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.md`
- Section 11.5: `Interpreting expert behavior carefully` -> `references/section-skills/ch11/05-interpreting-expert-behavior-carefully.md`
- Section 11.6: `Chapter summary and handoff` -> `references/section-skills/ch11/06-chapter-summary-and-handoff.md`
- Section 12.1: `Autoregressive inference with sparse FFNs` -> `references/section-skills/ch12/01-autoregressive-inference-with-sparse-ffns.md`
- Section 12.2: `Batching routed tokens at inference` -> `references/section-skills/ch12/02-batching-routed-tokens-at-inference.md`
- Section 12.3: `Compute, memory, and active-parameter accounting` -> `references/section-skills/ch12/03-compute-memory-and-active-parameter-accounting.md`
- Section 12.4: `Expert parallelism and all-to-all communication` -> `references/section-skills/ch12/04-expert-parallelism-and-all-to-all-communication.md`
- Section 12.5: `Mapping the book model to production MoE families` -> `references/section-skills/ch12/05-mapping-the-book-model-to-production-moe-families.md`
- Section 12.6: `Book summary and next steps` -> `references/section-skills/ch12/06-book-summary-and-next-steps.md`

## Output expectations

For a section-development task, return the updated LaTeX prose and any changed wrapper or code files. The section prose must keep artifact environments out of the prose file and include artifacts only by `\input`.

For a proofreading task, report concrete fixes against the checklist, especially missing shape definitions, misplaced figures, weak diagnostics, incorrect router-bias behavior, or raw artifact environments in prose.
