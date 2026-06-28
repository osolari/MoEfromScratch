# Phase 5 section brief index

Each row points to the self-contained section-development brief and session starter.

| Section | Title | Brief | Session starter |
|---:|---|---|---|
| 1.1 | The dense FFN bottleneck | `section_development_briefs/ch01/01-the-dense-ffn-bottleneck.md` | `session_starters/ch01/01-the-dense-ffn-bottleneck.md` |
| 1.2 | Conditional compute as the central idea | `section_development_briefs/ch01/02-conditional-compute-as-the-central-idea.md` | `session_starters/ch01/02-conditional-compute-as-the-central-idea.md` |
| 1.3 | A tiny routing story | `section_development_briefs/ch01/03-a-tiny-routing-story.md` | `session_starters/ch01/03-a-tiny-routing-story.md` |
| 1.4 | What from scratch means for this book | `section_development_briefs/ch01/04-what-from-scratch-means-for-this-book.md` | `session_starters/ch01/04-what-from-scratch-means-for-this-book.md` |
| 1.5 | The MiniDeepSeekMoE build ladder | `section_development_briefs/ch01/05-the-minideepseekmoe-build-ladder.md` | `session_starters/ch01/05-the-minideepseekmoe-build-ladder.md` |
| 1.6 | Chapter summary and handoff | `section_development_briefs/ch01/06-chapter-summary-and-handoff.md` | `session_starters/ch01/06-chapter-summary-and-handoff.md` |
| 2.1 | Dataset and token batches | `section_development_briefs/ch02/01-dataset-and-token-batches.md` | `session_starters/ch02/01-dataset-and-token-batches.md` |
| 2.2 | Token and position embeddings | `section_development_briefs/ch02/02-token-and-position-embeddings.md` | `session_starters/ch02/02-token-and-position-embeddings.md` |
| 2.3 | Causal self-attention as the context path | `section_development_briefs/ch02/03-causal-self-attention-as-the-context-path.md` | `session_starters/ch02/03-causal-self-attention-as-the-context-path.md` |
| 2.4 | Dense feed-forward block as the replacement target | `section_development_briefs/ch02/04-dense-feed-forward-block-as-the-replacement-target.md` | `session_starters/ch02/04-dense-feed-forward-block-as-the-replacement-target.md` |
| 2.5 | Training loop and sampling baseline | `section_development_briefs/ch02/05-training-loop-and-sampling-baseline.md` | `session_starters/ch02/05-training-loop-and-sampling-baseline.md` |
| 2.6 | Baseline diagnostics and comparison slots | `section_development_briefs/ch02/06-baseline-diagnostics-and-comparison-slots.md` | `session_starters/ch02/06-baseline-diagnostics-and-comparison-slots.md` |
| 3.1 | Expert MLPs as named FFNs | `section_development_briefs/ch03/01-expert-mlps-as-named-ffns.md` | `session_starters/ch03/01-expert-mlps-as-named-ffns.md` |
| 3.2 | Router scores and tensor shapes | `section_development_briefs/ch03/02-router-scores-and-tensor-shapes.md` | `session_starters/ch03/02-router-scores-and-tensor-shapes.md` |
| 3.3 | Top-k selection without dispatch | `section_development_briefs/ch03/03-top-k-selection-without-dispatch.md` | `session_starters/ch03/03-top-k-selection-without-dispatch.md` |
| 3.4 | Naive token-by-token dispatch | `section_development_briefs/ch03/04-naive-token-by-token-dispatch.md` | `session_starters/ch03/04-naive-token-by-token-dispatch.md` |
| 3.5 | Shape and gradient checks | `section_development_briefs/ch03/05-shape-and-gradient-checks.md` | `session_starters/ch03/05-shape-and-gradient-checks.md` |
| 3.6 | Chapter summary and handoff | `section_development_briefs/ch03/06-chapter-summary-and-handoff.md` | `session_starters/ch03/06-chapter-summary-and-handoff.md` |
| 4.1 | Why top-1 routing is the simplest sparse case | `section_development_briefs/ch04/01-why-top-1-routing-is-the-simplest-sparse-case.md` | `session_starters/ch04/01-why-top-1-routing-is-the-simplest-sparse-case.md` |
| 4.2 | Assignment masks and expert buckets | `section_development_briefs/ch04/02-assignment-masks-and-expert-buckets.md` | `session_starters/ch04/02-assignment-masks-and-expert-buckets.md` |
| 4.3 | Dispatching tokens to selected experts | `section_development_briefs/ch04/03-dispatching-tokens-to-selected-experts.md` | `session_starters/ch04/03-dispatching-tokens-to-selected-experts.md` |
| 4.4 | Capacity and dropped tokens | `section_development_briefs/ch04/04-capacity-and-dropped-tokens.md` | `session_starters/ch04/04-capacity-and-dropped-tokens.md` |
| 4.5 | Load histograms and failure modes | `section_development_briefs/ch04/05-load-histograms-and-failure-modes.md` | `session_starters/ch04/05-load-histograms-and-failure-modes.md` |
| 4.6 | Chapter summary and handoff | `section_development_briefs/ch04/06-chapter-summary-and-handoff.md` | `session_starters/ch04/06-chapter-summary-and-handoff.md` |
| 5.1 | Why top-2 changes the routing story | `section_development_briefs/ch05/01-why-top-2-changes-the-routing-story.md` | `session_starters/ch05/01-why-top-2-changes-the-routing-story.md` |
| 5.2 | Normalizing selected router scores | `section_development_briefs/ch05/02-normalizing-selected-router-scores.md` | `session_starters/ch05/02-normalizing-selected-router-scores.md` |
| 5.3 | Dispatch for two expert paths per token | `section_development_briefs/ch05/03-dispatch-for-two-expert-paths-per-token.md` | `session_starters/ch05/03-dispatch-for-two-expert-paths-per-token.md` |
| 5.4 | Comparing top-1 and top-2 diagnostics | `section_development_briefs/ch05/04-comparing-top-1-and-top-2-diagnostics.md` | `session_starters/ch05/04-comparing-top-1-and-top-2-diagnostics.md` |
| 5.5 | Numerical stability in top-k gates | `section_development_briefs/ch05/05-numerical-stability-in-top-k-gates.md` | `session_starters/ch05/05-numerical-stability-in-top-k-gates.md` |
| 5.6 | Chapter summary and handoff | `section_development_briefs/ch05/06-chapter-summary-and-handoff.md` | `session_starters/ch05/06-chapter-summary-and-handoff.md` |
| 6.1 | Flattened tokens as the dispatch unit | `section_development_briefs/ch06/01-flattened-tokens-as-the-dispatch-unit.md` | `session_starters/ch06/01-flattened-tokens-as-the-dispatch-unit.md` |
| 6.2 | Expert batch construction | `section_development_briefs/ch06/02-expert-batch-construction.md` | `session_starters/ch06/02-expert-batch-construction.md` |
| 6.3 | Capacity factors and overflow policy | `section_development_briefs/ch06/03-capacity-factors-and-overflow-policy.md` | `session_starters/ch06/03-capacity-factors-and-overflow-policy.md` |
| 6.4 | Unpacking and weighted combine | `section_development_briefs/ch06/04-unpacking-and-weighted-combine.md` | `session_starters/ch06/04-unpacking-and-weighted-combine.md` |
| 6.5 | Equivalence tests against the naive layer | `section_development_briefs/ch06/05-equivalence-tests-against-the-naive-layer.md` | `session_starters/ch06/05-equivalence-tests-against-the-naive-layer.md` |
| 6.6 | Chapter summary and handoff | `section_development_briefs/ch06/06-chapter-summary-and-handoff.md` | `session_starters/ch06/06-chapter-summary-and-handoff.md` |
| 7.1 | Expert imbalance as a training problem | `section_development_briefs/ch07/01-expert-imbalance-as-a-training-problem.md` | `session_starters/ch07/01-expert-imbalance-as-a-training-problem.md` |
| 7.2 | Auxiliary load-balancing loss | `section_development_briefs/ch07/02-auxiliary-load-balancing-loss.md` | `session_starters/ch07/02-auxiliary-load-balancing-loss.md` |
| 7.3 | Integrating auxiliary loss into training | `section_development_briefs/ch07/03-integrating-auxiliary-loss-into-training.md` | `session_starters/ch07/03-integrating-auxiliary-loss-into-training.md` |
| 7.4 | Router score scale and z-loss | `section_development_briefs/ch07/04-router-score-scale-and-z-loss.md` | `session_starters/ch07/04-router-score-scale-and-z-loss.md` |
| 7.5 | Routing dashboards and training logs | `section_development_briefs/ch07/05-routing-dashboards-and-training-logs.md` | `session_starters/ch07/05-routing-dashboards-and-training-logs.md` |
| 7.6 | Chapter summary and handoff | `section_development_briefs/ch07/06-chapter-summary-and-handoff.md` | `session_starters/ch07/06-chapter-summary-and-handoff.md` |
| 8.1 | The role of shared experts | `section_development_briefs/ch08/01-the-role-of-shared-experts.md` | `session_starters/ch08/01-the-role-of-shared-experts.md` |
| 8.2 | Fine-grained routed expert segmentation | `section_development_briefs/ch08/02-fine-grained-routed-expert-segmentation.md` | `session_starters/ch08/02-fine-grained-routed-expert-segmentation.md` |
| 8.3 | The MiniDeepSeekMoE layer contract | `section_development_briefs/ch08/03-the-minideepseekmoe-layer-contract.md` | `session_starters/ch08/03-the-minideepseekmoe-layer-contract.md` |
| 8.4 | Combining shared and routed outputs | `section_development_briefs/ch08/04-combining-shared-and-routed-outputs.md` | `session_starters/ch08/04-combining-shared-and-routed-outputs.md` |
| 8.5 | Specialization diagnostics | `section_development_briefs/ch08/05-specialization-diagnostics.md` | `session_starters/ch08/05-specialization-diagnostics.md` |
| 8.6 | Chapter summary and handoff | `section_development_briefs/ch08/06-chapter-summary-and-handoff.md` | `session_starters/ch08/06-chapter-summary-and-handoff.md` |
| 9.1 | The limitation of auxiliary balancing | `section_development_briefs/ch09/01-the-limitation-of-auxiliary-balancing.md` | `session_starters/ch09/01-the-limitation-of-auxiliary-balancing.md` |
| 9.2 | Router bias as non-trainable state | `section_development_briefs/ch09/02-router-bias-as-non-trainable-state.md` | `session_starters/ch09/02-router-bias-as-non-trainable-state.md` |
| 9.3 | Biased selection and unbiased combine | `section_development_briefs/ch09/03-biased-selection-and-unbiased-combine.md` | `session_starters/ch09/03-biased-selection-and-unbiased-combine.md` |
| 9.4 | Dynamic bias update from expert load | `section_development_briefs/ch09/04-dynamic-bias-update-from-expert-load.md` | `session_starters/ch09/04-dynamic-bias-update-from-expert-load.md` |
| 9.5 | Comparing balancing methods | `section_development_briefs/ch09/05-comparing-balancing-methods.md` | `session_starters/ch09/05-comparing-balancing-methods.md` |
| 9.6 | Chapter summary and handoff | `section_development_briefs/ch09/06-chapter-summary-and-handoff.md` | `session_starters/ch09/06-chapter-summary-and-handoff.md` |
| 10.1 | Configuration objects and model variants | `section_development_briefs/ch10/01-configuration-objects-and-model-variants.md` | `session_starters/ch10/01-configuration-objects-and-model-variants.md` |
| 10.2 | Decoder block with dense prefix and MoE layers | `section_development_briefs/ch10/02-decoder-block-with-dense-prefix-and-moe-layers.md` | `session_starters/ch10/02-decoder-block-with-dense-prefix-and-moe-layers.md` |
| 10.3 | Forward pass outputs and loss dictionary | `section_development_briefs/ch10/03-forward-pass-outputs-and-loss-dictionary.md` | `session_starters/ch10/03-forward-pass-outputs-and-loss-dictionary.md` |
| 10.4 | Training and sampling scripts | `section_development_briefs/ch10/04-training-and-sampling-scripts.md` | `session_starters/ch10/04-training-and-sampling-scripts.md` |
| 10.5 | Full-model smoke tests | `section_development_briefs/ch10/05-full-model-smoke-tests.md` | `session_starters/ch10/05-full-model-smoke-tests.md` |
| 10.6 | Chapter summary and handoff | `section_development_briefs/ch10/06-chapter-summary-and-handoff.md` | `session_starters/ch10/06-chapter-summary-and-handoff.md` |
| 11.1 | Experiment design for a from-scratch book | `section_development_briefs/ch11/01-experiment-design-for-a-from-scratch-book.md` | `session_starters/ch11/01-experiment-design-for-a-from-scratch-book.md` |
| 11.2 | Dataset preparation and reproducibility | `section_development_briefs/ch11/02-dataset-preparation-and-reproducibility.md` | `session_starters/ch11/02-dataset-preparation-and-reproducibility.md` |
| 11.3 | Loss curves and routing dashboards | `section_development_briefs/ch11/03-loss-curves-and-routing-dashboards.md` | `session_starters/ch11/03-loss-curves-and-routing-dashboards.md` |
| 11.4 | Ablation matrix: dense, top-1, top-2, shared, and bias-balanced | `section_development_briefs/ch11/04-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.md` | `session_starters/ch11/04-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.md` |
| 11.5 | Interpreting expert behavior carefully | `section_development_briefs/ch11/05-interpreting-expert-behavior-carefully.md` | `session_starters/ch11/05-interpreting-expert-behavior-carefully.md` |
| 11.6 | Chapter summary and handoff | `section_development_briefs/ch11/06-chapter-summary-and-handoff.md` | `session_starters/ch11/06-chapter-summary-and-handoff.md` |
| 12.1 | Autoregressive inference with sparse FFNs | `section_development_briefs/ch12/01-autoregressive-inference-with-sparse-ffns.md` | `session_starters/ch12/01-autoregressive-inference-with-sparse-ffns.md` |
| 12.2 | Batching routed tokens at inference | `section_development_briefs/ch12/02-batching-routed-tokens-at-inference.md` | `session_starters/ch12/02-batching-routed-tokens-at-inference.md` |
| 12.3 | Compute, memory, and active-parameter accounting | `section_development_briefs/ch12/03-compute-memory-and-active-parameter-accounting.md` | `session_starters/ch12/03-compute-memory-and-active-parameter-accounting.md` |
| 12.4 | Expert parallelism and all-to-all communication | `section_development_briefs/ch12/04-expert-parallelism-and-all-to-all-communication.md` | `session_starters/ch12/04-expert-parallelism-and-all-to-all-communication.md` |
| 12.5 | Mapping the book model to production MoE families | `section_development_briefs/ch12/05-mapping-the-book-model-to-production-moe-families.md` | `session_starters/ch12/05-mapping-the-book-model-to-production-moe-families.md` |
| 12.6 | Book summary and next steps | `section_development_briefs/ch12/06-book-summary-and-next-steps.md` | `session_starters/ch12/06-book-summary-and-next-steps.md` |
