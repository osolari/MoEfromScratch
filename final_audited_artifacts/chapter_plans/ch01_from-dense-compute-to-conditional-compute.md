# Chapter 1: From dense compute to conditional compute

**Part:** Part I - foundations and baseline

**Role in the book:** Motivate MoE from the dense FFN bottleneck and establish the build ladder.

## This chapter covers

- Why dense Transformer feed-forward layers dominate parameter and compute growth.
- How conditional compute changes the cost story without changing the decoder interface.
- The MiniDeepSeekMoE roadmap that the rest of the book implements.

## Implementation milestone

Create chapter notebooks that calculate simple parameter/FLOP estimates and visualize token-to-expert routing with hand-built tensors.

## Section-by-section plan

### 1.1 The dense FFN bottleneck

**Objective:** Show that the dense feed-forward block is the natural place to introduce sparsity because every token pays for every hidden unit.

**Mini-example:** Use a four-token batch with d_model=8 and an FFN expansion factor of 4; count multiply-adds for all tokens.

**Development flow:**

1. Open with the local problem: Show that the dense feed-forward block is the natural place to introduce sparsity because every token pays for every hidden unit.
2. Introduce the schematic: Dense decoder block with the FFN path highlighted as the always-on compute region.
3. Walk through mechanics and shapes using: Dense FFN cost estimate using D, H, and number of tokens N.
4. Implement or pseudocode: Tiny function that estimates dense FFN parameters and per-token matrix multiplies.
5. Verify with: A small cost table proving that increasing H increases every token path.
6. Bridge: Once the bottleneck is visible, the next question is whether every token really needs the same FFN.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch01/fig-the-dense-ffn-bottleneck.tex` - TikZ figure. Caption placeholder: Dense decoder block with the FFN path highlighted as the always-on compute region. Label: `fig:ch01-the-dense-ffn-bottleneck`.
- `latex_book_skeleton/tables/ch01/tab-the-dense-ffn-bottleneck.tex` - Table. Caption placeholder: Parameter and activation shape comparison for attention, dense FFN, and the residual path. Label: `tab:ch01-the-dense-ffn-bottleneck`.
- `latex_book_skeleton/listings/ch01/lst-the-dense-ffn-bottleneck.tex` - Python listing. Caption placeholder: Tiny function that estimates dense FFN parameters and per-token matrix multiplies. Label: `lst:ch01-the-dense-ffn-bottleneck`.
- `latex_book_skeleton/equations/ch01/eq-the-dense-ffn-bottleneck.tex` - Equation artifact. Placeholder: Dense FFN cost estimate using D, H, and number of tokens N. Label: `eq:ch01-the-dense-ffn-bottleneck`.

Detailed section file: `section_plans/ch01/01-the-dense-ffn-bottleneck.md`

### 1.2 Conditional compute as the central idea

**Objective:** Introduce MoE as selective FFN computation rather than a mysterious new model family.

**Mini-example:** Route four tokens to two of four available experts and compare activated parameters against total parameters.

**Development flow:**

1. Open with the local problem: Introduce MoE as selective FFN computation rather than a mysterious new model family.
2. Introduce the schematic: Tokens split through a router into a sparse subset of experts, then recombine.
3. Walk through mechanics and shapes using: Activated-parameter view: total expert bank versus top-k expert use per token.
4. Implement or pseudocode: Pseudocode that chooses expert IDs for tokens and reports active expert count.
5. Verify with: Compute the active fraction for E=4, K=2 and E=16, K=2.
6. Bridge: Selective compute creates a new component: the router, which needs its own tensor contract.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch01/fig-conditional-compute-as-the-central-idea.tex` - TikZ figure. Caption placeholder: Tokens split through a router into a sparse subset of experts, then recombine. Label: `fig:ch01-conditional-compute-as-the-central-idea`.
- `latex_book_skeleton/tables/ch01/tab-conditional-compute-as-the-central-idea.tex` - Table. Caption placeholder: Dense versus conditional-compute vocabulary: FFN, expert, router, active parameters, total parameters. Label: `tab:ch01-conditional-compute-as-the-central-idea`.
- `latex_book_skeleton/listings/ch01/lst-conditional-compute-as-the-central-idea.tex` - Python listing. Caption placeholder: Pseudocode that chooses expert IDs for tokens and reports active expert count. Label: `lst:ch01-conditional-compute-as-the-central-idea`.
- `latex_book_skeleton/equations/ch01/eq-conditional-compute-as-the-central-idea.tex` - Equation artifact. Placeholder: Activated-parameter view: total expert bank versus top-k expert use per token. Label: `eq:ch01-conditional-compute-as-the-central-idea`.

Detailed section file: `section_plans/ch01/02-conditional-compute-as-the-central-idea.md`

### 1.3 A tiny routing story

**Objective:** Give readers a concrete token-by-token routing example before any model code appears.

**Mini-example:** Use tokens [cat, sat, code, runs], four experts, and top-2 routing weights.

**Development flow:**

1. Open with the local problem: Give readers a concrete token-by-token routing example before any model code appears.
2. Introduce the schematic: A storyboard of router scores, selected experts, expert outputs, and weighted combine.
3. Walk through mechanics and shapes using: Weighted expert output y_t = sum gate_i expert_i(x_t).
4. Implement or pseudocode: Manual PyTorch tensor example that applies torch.topk and normalized weights.
5. Verify with: Check that gates for each token sum to one after top-k normalization.
6. Bridge: This toy flow becomes the shape contract for every later implementation.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch01/fig-a-tiny-routing-story.tex` - TikZ figure. Caption placeholder: A storyboard of router scores, selected experts, expert outputs, and weighted combine. Label: `fig:ch01-a-tiny-routing-story`.
- `latex_book_skeleton/tables/ch01/tab-a-tiny-routing-story.tex` - Table. Caption placeholder: Toy router-score matrix with top-2 expert choices and normalized gates. Label: `tab:ch01-a-tiny-routing-story`.
- `latex_book_skeleton/listings/ch01/lst-a-tiny-routing-story.tex` - Python listing. Caption placeholder: Manual PyTorch tensor example that applies torch.topk and normalized weights. Label: `lst:ch01-a-tiny-routing-story`.
- `latex_book_skeleton/equations/ch01/eq-a-tiny-routing-story.tex` - Equation artifact. Placeholder: Weighted expert output y_t = sum gate_i expert_i(x_t). Label: `eq:ch01-a-tiny-routing-story`.

Detailed section file: `section_plans/ch01/03-a-tiny-routing-story.md`

### 1.4 What from scratch means for this book

**Objective:** Define the implementation boundary: small readable modules, explicit tensors, and diagnostics before optimization.

**Mini-example:** Contrast a one-line library MoE call with a transparent router, dispatch, expert, and combine pipeline.

**Development flow:**

1. Open with the local problem: Define the implementation boundary: small readable modules, explicit tensors, and diagnostics before optimization.
2. Introduce the schematic: Layered build approach from scalar example to vectorized PyTorch to training script.
3. Walk through mechanics and shapes using: Interface invariant: MoE layer maps (B,T,D) to (B,T,D).
4. Implement or pseudocode: Skeleton class layout for Router, ExpertMLP, MoELayer, and MiniDeepSeekMoE.
5. Verify with: Checklist that every chapter must include shapes, a code path, and a verification artifact.
6. Bridge: With the boundary defined, we can plan the exact model we will build.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch01/fig-what-from-scratch-means-for-this-book.tex` - TikZ figure. Caption placeholder: Layered build approach from scalar example to vectorized PyTorch to training script. Label: `fig:ch01-what-from-scratch-means-for-this-book`.
- `latex_book_skeleton/tables/ch01/tab-what-from-scratch-means-for-this-book.tex` - Table. Caption placeholder: Included and excluded scope for the book, including distributed training and production kernels. Label: `tab:ch01-what-from-scratch-means-for-this-book`.
- `latex_book_skeleton/listings/ch01/lst-what-from-scratch-means-for-this-book.tex` - Python listing. Caption placeholder: Skeleton class layout for Router, ExpertMLP, MoELayer, and MiniDeepSeekMoE. Label: `lst:ch01-what-from-scratch-means-for-this-book`.
- `latex_book_skeleton/equations/ch01/eq-what-from-scratch-means-for-this-book.tex` - Equation artifact. Placeholder: Interface invariant: MoE layer maps (B,T,D) to (B,T,D). Label: `eq:ch01-what-from-scratch-means-for-this-book`.

Detailed section file: `section_plans/ch01/04-what-from-scratch-means-for-this-book.md`

### 1.5 The MiniDeepSeekMoE build ladder

**Objective:** Preview the book path from dense baseline to shared experts, fine-grained experts, and router-bias balancing.

**Mini-example:** Use the smoke-test configuration with two layers, four routed experts, and one shared expert.

**Development flow:**

1. Open with the local problem: Preview the book path from dense baseline to shared experts, fine-grained experts, and router-bias balancing.
2. Introduce the schematic: Roadmap ladder: dense baseline, top-1, top-2, capacity, auxiliary loss, shared experts, bias balancing, full model.
3. Walk through mechanics and shapes using: Final layer formula combining residual, shared expert output, and routed expert output.
4. Implement or pseudocode: Configuration dictionary for MiniDeepSeekMoE-Smoke and MiniDeepSeekMoE-16x2.
5. Verify with: Milestone checklist that marks which diagnostics appear by each chapter.
6. Bridge: The first build step is a dense Transformer baseline that gives the MoE layer somewhere to live.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch01/fig-the-minideepseekmoe-build-ladder.tex` - TikZ figure. Caption placeholder: Roadmap ladder: dense baseline, top-1, top-2, capacity, auxiliary loss, shared experts, bias balancing, full model. Label: `fig:ch01-the-minideepseekmoe-build-ladder`.
- `latex_book_skeleton/tables/ch01/tab-the-minideepseekmoe-build-ladder.tex` - Table. Caption placeholder: Chapter-by-chapter implementation milestones and expected code outputs. Label: `tab:ch01-the-minideepseekmoe-build-ladder`.
- `latex_book_skeleton/listings/ch01/lst-the-minideepseekmoe-build-ladder.tex` - Python listing. Caption placeholder: Configuration dictionary for MiniDeepSeekMoE-Smoke and MiniDeepSeekMoE-16x2. Label: `lst:ch01-the-minideepseekmoe-build-ladder`.
- `latex_book_skeleton/equations/ch01/eq-the-minideepseekmoe-build-ladder.tex` - Equation artifact. Placeholder: Final layer formula combining residual, shared expert output, and routed expert output. Label: `eq:ch01-the-minideepseekmoe-build-ladder`.

Detailed section file: `section_plans/ch01/05-the-minideepseekmoe-build-ladder.md`

### 1.6 Chapter summary and handoff

**Objective:** Close the motivation chapter with the vocabulary and constraints the reader will reuse.

**Mini-example:** Revisit the four-token example and label every object with its future tensor name.

**Development flow:**

1. Open with the local problem: Close the motivation chapter with the vocabulary and constraints the reader will reuse.
2. Introduce the schematic: Concept map linking tokens, router scores, top-k experts, gates, and combined output.
3. Walk through mechanics and shapes using: Shape summary for x, router_logits, topk_idx, gates, and y.
4. Implement or pseudocode: Sanity-check function signatures that later chapters must satisfy.
5. Verify with: Reader checkpoint: identify which part of the dense model will be replaced by MoE.
6. Bridge: Next we build the dense decoder baseline so the replacement is meaningful.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch01/fig-chapter-summary-and-handoff.tex` - TikZ figure. Caption placeholder: Concept map linking tokens, router scores, top-k experts, gates, and combined output. Label: `fig:ch01-chapter-summary-and-handoff`.
- `latex_book_skeleton/tables/ch01/tab-chapter-summary-and-handoff.tex` - Table. Caption placeholder: Glossary of first-use terms for the rest of the book. Label: `tab:ch01-chapter-summary-and-handoff`.
- `latex_book_skeleton/listings/ch01/lst-chapter-summary-and-handoff.tex` - Python listing. Caption placeholder: Sanity-check function signatures that later chapters must satisfy. Label: `lst:ch01-chapter-summary-and-handoff`.
- `latex_book_skeleton/equations/ch01/eq-chapter-summary-and-handoff.tex` - Equation artifact. Placeholder: Shape summary for x, router_logits, topk_idx, gates, and y. Label: `eq:ch01-chapter-summary-and-handoff`.

Detailed section file: `section_plans/ch01/06-chapter-summary-and-handoff.md`
