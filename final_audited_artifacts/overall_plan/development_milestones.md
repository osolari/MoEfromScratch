# Development milestones

The book should be developed in milestone order so each later chapter can rely on tested code from earlier chapters.

## Chapter 1: From dense compute to conditional compute

**Implementation milestone:** Create chapter notebooks that calculate simple parameter/FLOP estimates and visualize token-to-expert routing with hand-built tensors.

**Exit checks:**

- The chapter compiles in LaTeX with every planned artifact included through `\input`.
- The code path runs in the smoke configuration.
- The diagnostic artifact demonstrates at least one failure mode or sanity check.
- The final paragraph bridges to the next chapter's limitation.

## Chapter 2: A dense Transformer baseline from scratch

**Implementation milestone:** Produce a dense decoder implementation, train loop, sample script, and validation-loss baseline.

**Exit checks:**

- The chapter compiles in LaTeX with every planned artifact included through `\input`.
- The code path runs in the smoke configuration.
- The diagnostic artifact demonstrates at least one failure mode or sanity check.
- The final paragraph bridges to the next chapter's limitation.

## Chapter 3: Experts, routers, and the first MoE layer

**Implementation milestone:** Implement ExpertMLP, Router, and a naive TopKMoELayer that passes shape and gate checks.

**Exit checks:**

- The chapter compiles in LaTeX with every planned artifact included through `\input`.
- The code path runs in the smoke configuration.
- The diagnostic artifact demonstrates at least one failure mode or sanity check.
- The final paragraph bridges to the next chapter's limitation.

## Chapter 4: Top-1 routing and Switch-style dispatch

**Implementation milestone:** Implement Top1Router, Top1MoELayer, routing masks, load histograms, and optional capacity handling.

**Exit checks:**

- The chapter compiles in LaTeX with every planned artifact included through `\input`.
- The code path runs in the smoke configuration.
- The diagnostic artifact demonstrates at least one failure mode or sanity check.
- The final paragraph bridges to the next chapter's limitation.

## Chapter 5: Top-2 routing and weighted expert combination

**Implementation milestone:** Implement Top2Router and Top2MoELayer with normalized gates, duplicate-safe dispatch, and comparison diagnostics.

**Exit checks:**

- The chapter compiles in LaTeX with every planned artifact included through `\input`.
- The code path runs in the smoke configuration.
- The diagnostic artifact demonstrates at least one failure mode or sanity check.
- The final paragraph bridges to the next chapter's limitation.

## Chapter 6: Vectorized dispatch, capacity, and routing efficiency

**Implementation milestone:** Implement vectorized dispatch utilities, capacity-aware routing, and correctness tests against naive top-2 output.

**Exit checks:**

- The chapter compiles in LaTeX with every planned artifact included through `\input`.
- The code path runs in the smoke configuration.
- The diagnostic artifact demonstrates at least one failure mode or sanity check.
- The final paragraph bridges to the next chapter's limitation.

## Chapter 7: Router training and load-balancing losses

**Implementation milestone:** Implement auxiliary load-balancing loss, optional router z-loss, entropy diagnostics, and trainer integration.

**Exit checks:**

- The chapter compiles in LaTeX with every planned artifact included through `\input`.
- The code path runs in the smoke configuration.
- The diagnostic artifact demonstrates at least one failure mode or sanity check.
- The final paragraph bridges to the next chapter's limitation.

## Chapter 8: Shared experts and fine-grained routed experts

**Implementation milestone:** Implement SharedExpertMLP, FineGrainedExpertBank, and MiniDeepSeekMoELayer with shared plus routed outputs.

**Exit checks:**

- The chapter compiles in LaTeX with every planned artifact included through `\input`.
- The code path runs in the smoke configuration.
- The diagnostic artifact demonstrates at least one failure mode or sanity check.
- The final paragraph bridges to the next chapter's limitation.

## Chapter 9: Auxiliary-loss-free load balancing

**Implementation milestone:** Implement router_bias state, biased top-k selection, unbiased gate computation, and no-gradient bias updates from observed load.

**Exit checks:**

- The chapter compiles in LaTeX with every planned artifact included through `\input`.
- The code path runs in the smoke configuration.
- The diagnostic artifact demonstrates at least one failure mode or sanity check.
- The final paragraph bridges to the next chapter's limitation.

## Chapter 10: Assembling MiniDeepSeekMoE end to end

**Implementation milestone:** Produce the final model.py, config.py, train.py, sample.py, and tests for the MiniDeepSeekMoE implementation.

**Exit checks:**

- The chapter compiles in LaTeX with every planned artifact included through `\input`.
- The code path runs in the smoke configuration.
- The diagnostic artifact demonstrates at least one failure mode or sanity check.
- The final paragraph bridges to the next chapter's limitation.

## Chapter 11: Training, diagnostics, and controlled experiments

**Implementation milestone:** Build experiment scripts, diagnostic plot generation, and ablation tables for dense versus MoE variants.

**Exit checks:**

- The chapter compiles in LaTeX with every planned artifact included through `\input`.
- The code path runs in the smoke configuration.
- The diagnostic artifact demonstrates at least one failure mode or sanity check.
- The final paragraph bridges to the next chapter's limitation.

## Chapter 12: Inference, performance, and scaling beyond the toy model

**Implementation milestone:** Add inference helpers, active-compute estimators, simple profiling scripts, and conceptual scaling diagrams.

**Exit checks:**

- The chapter compiles in LaTeX with every planned artifact included through `\input`.
- The code path runs in the smoke configuration.
- The diagnostic artifact demonstrates at least one failure mode or sanity check.
- The final paragraph bridges to the next chapter's limitation.
