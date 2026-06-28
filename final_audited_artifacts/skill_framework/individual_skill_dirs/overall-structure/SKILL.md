---
name: moe-models-from-scratch-overall-developer
description: use when planning, drafting, editing, or proofreading the latex-first book moe models from scratch. triggers include coordinating chapter flow, enforcing standalone latex artifact wrappers, maintaining the minideepseekmoe reference model, or preparing section-development handoffs.
---

# MoE Models from Scratch overall developer

Use this skill-style markdown to coordinate the full book-development project. It can be pasted into a new chat or copied into a `SKILL.md` file.

## Mission

Develop *MoE Models from Scratch* as a LaTeX-first, from-scratch technical book centered on `MiniDeepSeekMoE`, a small DeepSeekMoE-inspired decoder-only model that teaches sparse routing, expert dispatch, shared experts, fine-grained routed experts, and auxiliary-loss-free router-bias balancing.

## Non-negotiable development rules

- Develop the production book in LaTeX.
- Keep section prose in the planned `latex_book_skeleton/chapters/chXX/sections/*.tex` file.
- Do not inline `figure`, `table`, `lstlisting`, or `equation` environments in section prose.
- Do not allow figures or tables to float into a later section; default figure/table wrappers use `[H]`, with `placeins`/`\FloatBarrier` active when compiling.
- Include every planned artifact through a standalone `.tex` wrapper and `\input{...}`.
- Use TikZ for mechanism schematics.
- Use generated PDF assets only for plots, dashboards, and diagnostics; include them through figure wrappers.
- Preserve the MiniDeepSeekMoE invariant wherever router bias appears: router bias affects selection only; final combine weights are computed from unbiased selected scores.
- Follow the teaching flow: problem opening -> visual anchor -> tensor/math mechanics -> implementation listing -> diagnostic -> bridge.
- Avoid broad surveys inside local sections; make every section falsifiable with its diagnostic.


## Reference model contract

- Teaching model name: `MiniDeepSeekMoE-16x2`.
- Model type: decoder-only causal language model.
- Default depth: 6 layers.
- Width: 512.
- Attention heads: 8.
- Routed experts: 16.
- Shared experts: 2.
- Routed experts per token: 2.
- Final router scoring: sigmoid affinity.
- Final selection: `topk(score + router_bias)`.
- Final combine: normalize selected unbiased scores.
- Final balancing: non-trainable dynamic router bias updated from observed expert load.

Layer equation to preserve in prose and code:

```text
y_t = x_t
    + sum(shared_experts(x_t))
    + sum_{i in topk(score_t + bias)} gate_i routed_expert_i(x_t)
```

The bias vector changes which experts are selected. It does not enter the final gate normalization.

## Chapter skill files

| Chapter | Title | Standalone file | Individual `SKILL.md` mirror |
|---:|---|---|---|
| 1 | From dense compute to conditional compute | `standalone_skill_mds/chapters/ch01.skill.md` | `individual_skill_dirs/chapters/ch01/SKILL.md` |
| 2 | A dense Transformer baseline from scratch | `standalone_skill_mds/chapters/ch02.skill.md` | `individual_skill_dirs/chapters/ch02/SKILL.md` |
| 3 | Experts, routers, and the first MoE layer | `standalone_skill_mds/chapters/ch03.skill.md` | `individual_skill_dirs/chapters/ch03/SKILL.md` |
| 4 | Top-1 routing and Switch-style dispatch | `standalone_skill_mds/chapters/ch04.skill.md` | `individual_skill_dirs/chapters/ch04/SKILL.md` |
| 5 | Top-2 routing and weighted expert combination | `standalone_skill_mds/chapters/ch05.skill.md` | `individual_skill_dirs/chapters/ch05/SKILL.md` |
| 6 | Vectorized dispatch, capacity, and routing efficiency | `standalone_skill_mds/chapters/ch06.skill.md` | `individual_skill_dirs/chapters/ch06/SKILL.md` |
| 7 | Router training and load-balancing losses | `standalone_skill_mds/chapters/ch07.skill.md` | `individual_skill_dirs/chapters/ch07/SKILL.md` |
| 8 | Shared experts and fine-grained routed experts | `standalone_skill_mds/chapters/ch08.skill.md` | `individual_skill_dirs/chapters/ch08/SKILL.md` |
| 9 | Auxiliary-loss-free load balancing | `standalone_skill_mds/chapters/ch09.skill.md` | `individual_skill_dirs/chapters/ch09/SKILL.md` |
| 10 | Assembling MiniDeepSeekMoE end to end | `standalone_skill_mds/chapters/ch10.skill.md` | `individual_skill_dirs/chapters/ch10/SKILL.md` |
| 11 | Training, diagnostics, and controlled experiments | `standalone_skill_mds/chapters/ch11.skill.md` | `individual_skill_dirs/chapters/ch11/SKILL.md` |
| 12 | Inference, performance, and scaling beyond the toy model | `standalone_skill_mds/chapters/ch12.skill.md` | `individual_skill_dirs/chapters/ch12/SKILL.md` |

## Section skill files

| Section | Title | Standalone file | Diagnostic |
|---:|---|---|---|
| 1.1 | The dense FFN bottleneck | `standalone_skill_mds/sections/ch01/01-the-dense-ffn-bottleneck.skill.md` | A small cost table proving that increasing H increases every token path. |
| 1.2 | Conditional compute as the central idea | `standalone_skill_mds/sections/ch01/02-conditional-compute-as-the-central-idea.skill.md` | Compute the active fraction for E=4, K=2 and E=16, K=2. |
| 1.3 | A tiny routing story | `standalone_skill_mds/sections/ch01/03-a-tiny-routing-story.skill.md` | Check that gates for each token sum to one after top-k normalization. |
| 1.4 | What from scratch means for this book | `standalone_skill_mds/sections/ch01/04-what-from-scratch-means-for-this-book.skill.md` | Checklist that every chapter must include shapes, a code path, and a verification artifact. |
| 1.5 | The MiniDeepSeekMoE build ladder | `standalone_skill_mds/sections/ch01/05-the-minideepseekmoe-build-ladder.skill.md` | Milestone checklist that marks which diagnostics appear by each chapter. |
| 1.6 | Chapter summary and handoff | `standalone_skill_mds/sections/ch01/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: identify which part of the dense model will be replaced by MoE. |
| 2.1 | Dataset and token batches | `standalone_skill_mds/sections/ch02/01-dataset-and-token-batches.skill.md` | Print the first input-target pair and decode it to verify shifting. |
| 2.2 | Token and position embeddings | `standalone_skill_mds/sections/ch02/02-token-and-position-embeddings.skill.md` | Assert output shape and confirm gradients flow to both embedding tables. |
| 2.3 | Causal self-attention as the context path | `standalone_skill_mds/sections/ch02/03-causal-self-attention-as-the-context-path.skill.md` | Check that a token cannot attend to future positions. |
| 2.4 | Dense feed-forward block as the replacement target | `standalone_skill_mds/sections/ch02/04-dense-feed-forward-block-as-the-replacement-target.skill.md` | Confirm FFN preserves the final D dimension. |
| 2.5 | Training loop and sampling baseline | `standalone_skill_mds/sections/ch02/05-training-loop-and-sampling-baseline.skill.md` | Track train and validation loss plus samples at fixed intervals. |
| 2.6 | Baseline diagnostics and comparison slots | `standalone_skill_mds/sections/ch02/06-baseline-diagnostics-and-comparison-slots.skill.md` | Write the first baseline row in the experiment comparison table. |
| 3.1 | Expert MLPs as named FFNs | `standalone_skill_mds/sections/ch03/01-expert-mlps-as-named-ffns.skill.md` | Run all experts on the same token and compare output shapes. |
| 3.2 | Router scores and tensor shapes | `standalone_skill_mds/sections/ch03/02-router-scores-and-tensor-shapes.skill.md` | Assert that the expert dimension equals n_experts and token dimension equals B*T. |
| 3.3 | Top-k selection without dispatch | `standalone_skill_mds/sections/ch03/03-top-k-selection-without-dispatch.skill.md` | Verify that every token has exactly K selected expert IDs. |
| 3.4 | Naive token-by-token dispatch | `standalone_skill_mds/sections/ch03/04-naive-token-by-token-dispatch.skill.md` | Compare output shape to dense FFN output and inspect gates per token. |
| 3.5 | Shape and gradient checks | `standalone_skill_mds/sections/ch03/05-shape-and-gradient-checks.skill.md` | Count selected expert IDs and check nonzero gradients for selected expert parameters. |
| 3.6 | Chapter summary and handoff | `standalone_skill_mds/sections/ch03/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: identify where routing, expert computation, and combine happen in code. |
| 4.1 | Why top-1 routing is the simplest sparse case | `standalone_skill_mds/sections/ch04/01-why-top-1-routing-is-the-simplest-sparse-case.skill.md` | Verify each token has one expert and one scalar gate. |
| 4.2 | Assignment masks and expert buckets | `standalone_skill_mds/sections/ch04/02-assignment-masks-and-expert-buckets.skill.md` | Sum the mask across experts to confirm each token is assigned once. |
| 4.3 | Dispatching tokens to selected experts | `standalone_skill_mds/sections/ch04/03-dispatching-tokens-to-selected-experts.skill.md` | Assert output rows return to the original token order. |
| 4.4 | Capacity and dropped tokens | `standalone_skill_mds/sections/ch04/04-capacity-and-dropped-tokens.skill.md` | Report dropped_token_count and per-expert accepted counts. |
| 4.5 | Load histograms and failure modes | `standalone_skill_mds/sections/ch04/05-load-histograms-and-failure-modes.skill.md` | Save a histogram and a warning if max load is much larger than average load. |
| 4.6 | Chapter summary and handoff | `standalone_skill_mds/sections/ch04/06-chapter-summary-and-handoff.skill.md` | Compare validation loss smoke run with dense baseline, without claiming quality superiority. |
| 5.1 | Why top-2 changes the routing story | `standalone_skill_mds/sections/ch05/01-why-top-2-changes-the-routing-story.skill.md` | Compare active expert calls per token for K=1 and K=2. |
| 5.2 | Normalizing selected router scores | `standalone_skill_mds/sections/ch05/02-normalizing-selected-router-scores.skill.md` | Assert torch.allclose(gates.sum(-1), ones). |
| 5.3 | Dispatch for two expert paths per token | `standalone_skill_mds/sections/ch05/03-dispatch-for-two-expert-paths-per-token.skill.md` | Check output changes when gates are manually swapped. |
| 5.4 | Comparing top-1 and top-2 diagnostics | `standalone_skill_mds/sections/ch05/04-comparing-top-1-and-top-2-diagnostics.skill.md` | Save a comparison table and one histogram per routing mode. |
| 5.5 | Numerical stability in top-k gates | `standalone_skill_mds/sections/ch05/05-numerical-stability-in-top-k-gates.skill.md` | Unit tests for finite gates and gradients under small scores. |
| 5.6 | Chapter summary and handoff | `standalone_skill_mds/sections/ch05/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: explain why gates sum to one after selecting top-k only. |
| 6.1 | Flattened tokens as the dispatch unit | `standalone_skill_mds/sections/ch06/01-flattened-tokens-as-the-dispatch-unit.skill.md` | Round-trip flatten/unflatten equality check. |
| 6.2 | Expert batch construction | `standalone_skill_mds/sections/ch06/02-expert-batch-construction.skill.md` | Ensure each accepted route has exactly one expert slot. |
| 6.3 | Capacity factors and overflow policy | `standalone_skill_mds/sections/ch06/03-capacity-factors-and-overflow-policy.skill.md` | Log overflow route count and overflow fraction. |
| 6.4 | Unpacking and weighted combine | `standalone_skill_mds/sections/ch06/04-unpacking-and-weighted-combine.skill.md` | Compare vectorized output to naive output when capacity is large enough for no overflow. |
| 6.5 | Equivalence tests against the naive layer | `standalone_skill_mds/sections/ch06/05-equivalence-tests-against-the-naive-layer.skill.md` | Fail if max_abs_diff exceeds tolerance in no-overflow settings. |
| 6.6 | Chapter summary and handoff | `standalone_skill_mds/sections/ch06/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: identify where dropped routes enter the output calculation. |
| 7.1 | Expert imbalance as a training problem | `standalone_skill_mds/sections/ch07/01-expert-imbalance-as-a-training-problem.skill.md` | Report max_load/mean_load and number of empty experts. |
| 7.2 | Auxiliary load-balancing loss | `standalone_skill_mds/sections/ch07/02-auxiliary-load-balancing-loss.skill.md` | Check loss is lower for balanced synthetic routing than collapsed routing. |
| 7.3 | Integrating auxiliary loss into training | `standalone_skill_mds/sections/ch07/03-integrating-auxiliary-loss-into-training.skill.md` | Log individual losses separately so balancing cannot hide LM degradation. |
| 7.4 | Router score scale and z-loss | `standalone_skill_mds/sections/ch07/04-router-score-scale-and-z-loss.skill.md` | Track router score max, entropy, and z-loss over training. |
| 7.5 | Routing dashboards and training logs | `standalone_skill_mds/sections/ch07/05-routing-dashboards-and-training-logs.skill.md` | Generate a dashboard PDF or image after a short smoke run. |
| 7.6 | Chapter summary and handoff | `standalone_skill_mds/sections/ch07/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: explain why aux_loss must be logged separately from LM loss. |
| 8.1 | The role of shared experts | `standalone_skill_mds/sections/ch08/01-the-role-of-shared-experts.skill.md` | Verify shared experts receive gradients for every token, not only selected tokens. |
| 8.2 | Fine-grained routed expert segmentation | `standalone_skill_mds/sections/ch08/02-fine-grained-routed-expert-segmentation.skill.md` | Compute total and active expert parameters for several segmentations. |
| 8.3 | The MiniDeepSeekMoE layer contract | `standalone_skill_mds/sections/ch08/03-the-minideepseekmoe-layer-contract.skill.md` | Assert layer output shape equals input shape under smoke and default configs. |
| 8.4 | Combining shared and routed outputs | `standalone_skill_mds/sections/ch08/04-combining-shared-and-routed-outputs.skill.md` | Ablate shared_out to zero and routed_out to zero to confirm both paths affect output. |
| 8.5 | Specialization diagnostics | `standalone_skill_mds/sections/ch08/05-specialization-diagnostics.skill.md` | Generate expert usage heatmaps without overclaiming semantic specialization. |
| 8.6 | Chapter summary and handoff | `standalone_skill_mds/sections/ch08/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: distinguish shared expert compute from routed active compute. |
| 9.1 | The limitation of auxiliary balancing | `standalone_skill_mds/sections/ch09/01-the-limitation-of-auxiliary-balancing.skill.md` | Compare LM loss and load balance separately, not only total loss. |
| 9.2 | Router bias as non-trainable state | `standalone_skill_mds/sections/ch09/02-router-bias-as-non-trainable-state.skill.md` | Assert router_bias.requires_grad is false and optimizer does not update it. |
| 9.3 | Biased selection and unbiased combine | `standalone_skill_mds/sections/ch09/03-biased-selection-and-unbiased-combine.skill.md` | Unit test that changing bias can change expert IDs while gate values still come from raw scores. |
| 9.4 | Dynamic bias update from expert load | `standalone_skill_mds/sections/ch09/04-dynamic-bias-update-from-expert-load.skill.md` | Track bias values over training beside expert loads. |
| 9.5 | Comparing balancing methods | `standalone_skill_mds/sections/ch09/05-comparing-balancing-methods.skill.md` | Produce a table with LM loss, aux loss if used, load balance score, entropy, and drop rate. |
| 9.6 | Chapter summary and handoff | `standalone_skill_mds/sections/ch09/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: explain why bias should not be included in combine weights. |
| 10.1 | Configuration objects and model variants | `standalone_skill_mds/sections/ch10/01-configuration-objects-and-model-variants.skill.md` | Print model summary and assert required fields exist. |
| 10.2 | Decoder block with dense prefix and MoE layers | `standalone_skill_mds/sections/ch10/02-decoder-block-with-dense-prefix-and-moe-layers.skill.md` | List layer types during model initialization. |
| 10.3 | Forward pass outputs and loss dictionary | `standalone_skill_mds/sections/ch10/03-forward-pass-outputs-and-loss-dictionary.skill.md` | Unit test for output keys under dense, auxiliary, and bias modes. |
| 10.4 | Training and sampling scripts | `standalone_skill_mds/sections/ch10/04-training-and-sampling-scripts.skill.md` | Verify checkpoint reload produces logits of the same shape. |
| 10.5 | Full-model smoke tests | `standalone_skill_mds/sections/ch10/05-full-model-smoke-tests.skill.md` | CI-style console summary for all smoke tests. |
| 10.6 | Chapter summary and handoff | `standalone_skill_mds/sections/ch10/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: run the smoke model and inspect router metrics. |
| 11.1 | Experiment design for a from-scratch book | `standalone_skill_mds/sections/ch11/01-experiment-design-for-a-from-scratch-book.skill.md` | Check that every experiment saves config, seed, logs, and git/code snapshot note. |
| 11.2 | Dataset preparation and reproducibility | `standalone_skill_mds/sections/ch11/02-dataset-preparation-and-reproducibility.skill.md` | Print token counts, split sizes, and a decoded sample from each split. |
| 11.3 | Loss curves and routing dashboards | `standalone_skill_mds/sections/ch11/03-loss-curves-and-routing-dashboards.skill.md` | Save dashboard figures through LaTeX wrappers, never raw includegraphics in prose. |
| 11.4 | Ablation matrix: dense, top-1, top-2, shared, and bias-balanced | `standalone_skill_mds/sections/ch11/04-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.skill.md` | Flag any run with unstable loss, high drop rate, or extreme expert collapse. |
| 11.5 | Interpreting expert behavior carefully | `standalone_skill_mds/sections/ch11/05-interpreting-expert-behavior-carefully.skill.md` | Generate a routing trace table and a usage heatmap. |
| 11.6 | Chapter summary and handoff | `standalone_skill_mds/sections/ch11/06-chapter-summary-and-handoff.skill.md` | Reader checkpoint: identify whether a routing issue is code, loss, capacity, or data related. |
| 12.1 | Autoregressive inference with sparse FFNs | `standalone_skill_mds/sections/ch12/01-autoregressive-inference-with-sparse-ffns.skill.md` | Print selected experts for each generated token in a short sample. |
| 12.2 | Batching routed tokens at inference | `standalone_skill_mds/sections/ch12/02-batching-routed-tokens-at-inference.skill.md` | Histogram expert batch sizes over a generated sequence. |
| 12.3 | Compute, memory, and active-parameter accounting | `standalone_skill_mds/sections/ch12/03-compute-memory-and-active-parameter-accounting.skill.md` | Check estimates against model.count_parameters breakdown. |
| 12.4 | Expert parallelism and all-to-all communication | `standalone_skill_mds/sections/ch12/04-expert-parallelism-and-all-to-all-communication.skill.md` | Thought experiment table estimating routed activation traffic for a small config. |
| 12.5 | Mapping the book model to production MoE families | `standalone_skill_mds/sections/ch12/05-mapping-the-book-model-to-production-moe-families.skill.md` | Reader checkpoint: identify which chapter implemented each production analogue. |
| 12.6 | Book summary and next steps | `standalone_skill_mds/sections/ch12/06-book-summary-and-next-steps.skill.md` | Final self-test: build, train smoke, inspect routing, sample text, and explain limitations. |

## Book-wide source style

# Book flow and language extraction

## Reusable chapter rhythm

Use the following rhythm as the default for *MoE Models from Scratch*:

1. **Chapter title**: numbered, direct, and technical. The title names the bottleneck or mechanism, not only the component.
2. **This chapter covers**: three bullets. Each bullet should correspond to a reader outcome: intuition, mechanism, implementation/verification.
3. **Bridge paragraph**: connect the prior chapter's result to the new problem. The source book repeatedly uses this to make the book feel like one build rather than isolated essays.
4. **Roadmap or context figure**: show where the current topic fits in the whole model or training pipeline.
5. **Problem-first motivation**: make the computational bottleneck concrete before introducing the solution.
6. **Visual walkthrough**: use a schematic diagram before equations or code.
7. **Tensor/math walkthrough**: specify shapes, projections, losses, or routing equations.
8. **From-scratch implementation**: present compact PyTorch or Python code, with code annotations when the listing is dense.
9. **Check or comparison**: include a toy run, memory/FLOP comparison, load histogram, routing visualization, or benchmark-style table.
10. **Summary and bridge**: close by naming what was built and why the next chapter is needed.

## Voice rules to preserve

- Use first-person plural sparingly but consistently: "we build", "we trace", "we now have".
- Prefer direct transitions: "Let's trace the flow", "Now we hit the key problem", "This is where the router enters".
- Introduce abstractions through a concrete failure mode. Example pattern: dense FFNs are expensive -> sparse experts activate only a subset -> routing creates load-balancing problems.
- Keep the reader oriented with shapes, small examples, and one-sentence takeaways after diagrams.
- Avoid long theorem-style blocks. The source style is practical and explanatory, not proof-heavy.
- End sections with a local payoff: what the reader can now understand, implement, measure, or debug.

## Quantitative writing signals extracted

- Chapters use a consistent three-bullet opening summary.
- Paragraphs average about 42.0 words across parsed chapter body paragraphs, with a median of 41.0 words.
- Transition phrases are common enough to matter: "let's" (112), "however" (42), "to understand" (40), "as illustrated" (22), and "step" (200).
- The book relies heavily on figures: 190 figure containers across eight chapters, compared with 63 listing/code containers and 9 table containers.

## Section-level explanation loop

Each major section should generally include these beats:

| Beat | Purpose | MoE-book equivalent |
|---|---|---|
| Bottleneck | Explain why the dense or naive method fails | dense FFN cost, unstable routing, expert collapse, all-to-all overhead |
| Schematic | Show the moving parts | tokens -> router -> top-k experts -> weighted combine |
| Shapes | Prevent ambiguity | `(batch, seq, d_model)`, `(tokens, n_experts)`, expert capacity |
| Equation | Pin down the operation | router softmax, top-k mask, auxiliary loss, z-loss, capacity overflow |
| Code | Make it executable | small PyTorch module with explicit dimensions |
| Diagnostic | Make it trustworthy | histograms, expert load tables, gradient checks, sanity tests |
| Bridge | Explain why the next layer of complexity is needed | top-1 routing -> top-2 routing -> balancing -> distributed MoE |

## Style guardrails for new prose

- Prefer short setup examples: 4 tokens, 4 experts, top-2 routing, small hidden sizes.
- Introduce names only after the reader sees the problem they solve.
- Do not overload one section with both algorithm and systems details. Separate routing math, PyTorch implementation, and distributed execution.
- When a figure appears, its surrounding prose must answer: what should the reader notice, and what changes after this figure?


## Book plan

# MoE Models from Scratch - overall book plan

## Book premise

*MoE Models from Scratch* teaches mixture-of-experts language models by rebuilding the sparse feed-forward path one mechanism at a time. The reader starts with a dense decoder baseline, replaces the FFN with routed experts, learns how routing fails, adds balancing and diagnostics, and finishes with a MiniDeepSeekMoE implementation that keeps the core ideas visible.

## Reference architecture

The book uses `MiniDeepSeekMoE-16x2` as the final target: a decoder-only causal language model with 16 routed experts, 2 shared experts, top-2 routed experts per token, fine-grained routed expert dimensions, and auxiliary-loss-free router-bias balancing. The smoke configuration uses 4 routed experts and 1 shared expert for CPU-friendly tests.

## Editorial rhythm

Every chapter follows this loop:

1. Start from a concrete bottleneck or failure mode.
2. Anchor the mechanism with a schematic diagram.
3. Specify tensor shapes before writing code.
4. Implement the smallest readable PyTorch version.
5. Add a diagnostic that can catch mistakes.
6. End by naming the limitation that motivates the next chapter.

## Part structure

### Part I - foundations and baseline

**Chapter 1: From dense compute to conditional compute** - Motivate MoE from the dense FFN bottleneck and establish the build ladder.

**Chapter 2: A dense Transformer baseline from scratch** - Build a minimal decoder-only language model before replacing the FFN with MoE.

### Part II - routing mechanics from scratch

**Chapter 3: Experts, routers, and the first MoE layer** - Introduce the MoE layer as a transparent replacement for the dense FFN.

**Chapter 4: Top-1 routing and Switch-style dispatch** - Build the simplest sparse router and expose the expert-load problem.

**Chapter 5: Top-2 routing and weighted expert combination** - Generalize sparse routing so each token can combine two expert transformations.

**Chapter 6: Vectorized dispatch, capacity, and routing efficiency** - Move from readable loops to scalable tensor operations without changing the MoE math.

### Part III - training routers and experts

**Chapter 7: Router training and load-balancing losses** - Teach the router to avoid expert collapse before moving to auxiliary-loss-free balancing.

**Chapter 8: Shared experts and fine-grained routed experts** - Implement the DeepSeekMoE-inspired expert structure for the reference model.

**Chapter 9: Auxiliary-loss-free load balancing** - Replace auxiliary balancing with a router-bias mechanism that affects selection but not combine weights.

### Part IV - assembling and training the model

**Chapter 10: Assembling MiniDeepSeekMoE end to end** - Integrate the final MoE layer into a complete decoder-only language model.

**Chapter 11: Training, diagnostics, and controlled experiments** - Use the model to answer concrete questions about routing, balance, and sparse capacity.

### Part V - inference and scale

**Chapter 12: Inference, performance, and scaling beyond the toy model** - Connect the from-scratch implementation to systems concerns without turning the book into a distributed-systems text.

## Appendices

- **Appendix A: LaTeX artifact and diagram rules** - Document the color map, input-only artifact rule, label conventions, and TikZ patterns.
- **Appendix B: Tensor shape checklist** - Collect every tensor symbol and shape used in routing, dispatch, balancing, and diagnostics.
- **Appendix C: Codebase smoke tests and reproducibility checklist** - Provide a compact checklist for validating notebooks, scripts, tests, figures, and LaTeX builds.


## Visual and artifact rules

## Visual theme summary

Use semantic LaTeX color names only.

| Role | LaTeX color | Hex | Use |
|---|---|---:|---|
| Main navy | `BookNavy` | `#000055` | chapter titles and structural headings |
| Deep blue | `BookDeepBlue` | `#141464` | neutral diagram text and arrows |
| Listing header | `BookListingHeader` | `#020056` | code listing title bars |
| Callout gray | `BookCalloutGray` | `#E6E6E6` | notes, checkpoints, and chapter-cover boxes |
| Code background | `BookCodeBg` | `#F2F2F2` | listing background |
| Token purple | `MoETokenPurple` | `#C060E0` | tokens and token-flow dots |
| Router cyan | `MoERouterCyan` | `#00A7C1` | routers, score matrices, dispatch arrows |
| Expert purple | `MoEExpertPurple` | `#9050FF` | generic routed experts |
| Active expert green | `MoEActiveGreen` | `#70D050` | selected experts and active routes |
| Output red | `MoEOutputRed` | `#F05050` | outputs, overflow, imbalance warnings |
| Capacity gold | `MoECapacityGold` | `#FFD080` | capacity, top-k slots, quotas, and bias state |
| Shared expert green | `MoESharedGreen` | `#A8DDA8` | shared experts and always-on paths |
| Muted gray | `MoEMutedGray` | `#D0D0D0` | inactive routes and background structures |
| Soft fill | `MoESoftFill` | `#F0F0FF` | grouping regions |

Use semantic TikZ styles from `styles/tikzstyles.tex`. Do not scatter raw hex colors through figure bodies.


# LaTeX artifact contract

All book development must stay LaTeX-first.

## Section rule

Every artifact is a separate `.tex` wrapper and is included from section prose with `\input`.

```latex
\input{figures/chXX/fig-section-slug}
\input{tables/chXX/tab-section-slug}
\input{equations/chXX/eq-section-slug}
\input{listings/chXX/lst-section-slug}
```

## Wrapper rules

- TikZ figure wrappers contain a complete `figure` environment, `tikzpicture`, `\caption`, and `\label`.
- PDF figure wrappers contain a complete `figure` environment, `\includegraphics[width=\BookFigureWidth]{...}`, `\caption`, and `\label`.
- Table wrappers contain a complete table environment, caption, label, and `booktabs`/`tabularx` styling.
- Listing wrappers use `lstlisting` with `style=bookpython`, caption, and label.
- Equation wrappers contain an equation environment and a stable `eq:` label.


## Proofread checklist

# Proofread checklist

- The section opens from a concrete local problem.
- The figure appears before dense math or code.
- Every tensor in the equation and code listing has a shape or role.
- The diagnostic can catch a realistic implementation bug.
- The table adds structure rather than repeating prose.
- No raw figure/table/listing/equation environments are in section prose.
- All artifacts are included by `\input`.
- The final paragraph bridges to the next planned section.
- The MiniDeepSeekMoE invariant is preserved where relevant: router bias affects selection only, not unbiased combine weights.
