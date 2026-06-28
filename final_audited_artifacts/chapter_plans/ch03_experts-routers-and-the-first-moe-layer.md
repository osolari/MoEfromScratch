# Chapter 3: Experts, routers, and the first MoE layer

**Part:** Part II - routing mechanics from scratch

**Role in the book:** Introduce the MoE layer as a transparent replacement for the dense FFN.

## This chapter covers

- How an expert is just an FFN with an expert identity.
- How a router turns token states into expert scores.
- How a naive loop implementation clarifies dispatch before optimization.

## Implementation milestone

Implement ExpertMLP, Router, and a naive TopKMoELayer that passes shape and gate checks.

## Section-by-section plan

### 3.1 Expert MLPs as named FFNs

**Objective:** Demystify experts by deriving them directly from the dense FFN module.

**Mini-example:** Clone the dense FFN four times and label the copies expert 0 through expert 3.

**Development flow:**

1. Open with the local problem: Demystify experts by deriving them directly from the dense FFN module.
2. Introduce the schematic: One dense FFN replaced by a bank of same-shape expert MLPs.
3. Walk through mechanics and shapes using: expert_i(x) maps R^D to R^D for every expert i.
4. Implement or pseudocode: ExpertMLP class with the same input-output contract as the dense FFN.
5. Verify with: Run all experts on the same token and compare output shapes.
6. Bridge: Experts need a token-dependent selection mechanism: the router.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch03/fig-expert-mlps-as-named-ffns.tex` - TikZ figure. Caption placeholder: One dense FFN replaced by a bank of same-shape expert MLPs. Label: `fig:ch03-expert-mlps-as-named-ffns`.
- `latex_book_skeleton/tables/ch03/tab-expert-mlps-as-named-ffns.tex` - Table. Caption placeholder: Dense FFN versus expert bank parameters, active parameters, and outputs. Label: `tab:ch03-expert-mlps-as-named-ffns`.
- `latex_book_skeleton/listings/ch03/lst-expert-mlps-as-named-ffns.tex` - Python listing. Caption placeholder: ExpertMLP class with the same input-output contract as the dense FFN. Label: `lst:ch03-expert-mlps-as-named-ffns`.
- `latex_book_skeleton/equations/ch03/eq-expert-mlps-as-named-ffns.tex` - Equation artifact. Placeholder: expert_i(x) maps R^D to R^D for every expert i. Label: `eq:ch03-expert-mlps-as-named-ffns`.

Detailed section file: `section_plans/ch03/01-expert-mlps-as-named-ffns.md`

### 3.2 Router scores and tensor shapes

**Objective:** Define router logits, router probabilities, and the flattening convention used throughout the book.

**Mini-example:** Flatten x from (B,T,D) to (N,D) and compute router_logits with E=4 experts.

**Development flow:**

1. Open with the local problem: Define router logits, router probabilities, and the flattening convention used throughout the book.
2. Introduce the schematic: Flattened token matrix multiplied by a router projection to produce an N by E score table.
3. Walk through mechanics and shapes using: router_logits = x_flat W_r + b_r.
4. Implement or pseudocode: Router module that returns logits and score tensors.
5. Verify with: Assert that the expert dimension equals n_experts and token dimension equals B*T.
6. Bridge: Scores become sparse when we select only the top experts per token.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch03/fig-router-scores-and-tensor-shapes.tex` - TikZ figure. Caption placeholder: Flattened token matrix multiplied by a router projection to produce an N by E score table. Label: `fig:ch03-router-scores-and-tensor-shapes`.
- `latex_book_skeleton/tables/ch03/tab-router-scores-and-tensor-shapes.tex` - Table. Caption placeholder: Router tensor shape contract for x, x_flat, logits, scores, topk_idx, and gates. Label: `tab:ch03-router-scores-and-tensor-shapes`.
- `latex_book_skeleton/listings/ch03/lst-router-scores-and-tensor-shapes.tex` - Python listing. Caption placeholder: Router module that returns logits and score tensors. Label: `lst:ch03-router-scores-and-tensor-shapes`.
- `latex_book_skeleton/equations/ch03/eq-router-scores-and-tensor-shapes.tex` - Equation artifact. Placeholder: router_logits = x_flat W_r + b_r. Label: `eq:ch03-router-scores-and-tensor-shapes`.

Detailed section file: `section_plans/ch03/02-router-scores-and-tensor-shapes.md`

### 3.3 Top-k selection without dispatch

**Objective:** Separate the selection problem from expert execution so readers can inspect router behavior first.

**Mini-example:** Compute top-2 expert IDs and scores for a four-token, four-expert score table.

**Development flow:**

1. Open with the local problem: Separate the selection problem from expert execution so readers can inspect router behavior first.
2. Introduce the schematic: Score matrix with the top-k entries highlighted in each row.
3. Walk through mechanics and shapes using: S_t = topk(score_t, K), one selected set per token.
4. Implement or pseudocode: torch.topk example that returns topk_score and topk_idx.
5. Verify with: Verify that every token has exactly K selected expert IDs.
6. Bridge: Selection tells us where tokens should go; dispatch actually sends them there.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch03/fig-top-k-selection-without-dispatch.tex` - TikZ figure. Caption placeholder: Score matrix with the top-k entries highlighted in each row. Label: `fig:ch03-top-k-selection-without-dispatch`.
- `latex_book_skeleton/tables/ch03/tab-top-k-selection-without-dispatch.tex` - Table. Caption placeholder: Manual top-k results for the toy score table. Label: `tab:ch03-top-k-selection-without-dispatch`.
- `latex_book_skeleton/listings/ch03/lst-top-k-selection-without-dispatch.tex` - Python listing. Caption placeholder: torch.topk example that returns topk_score and topk_idx. Label: `lst:ch03-top-k-selection-without-dispatch`.
- `latex_book_skeleton/equations/ch03/eq-top-k-selection-without-dispatch.tex` - Equation artifact. Placeholder: S_t = topk(score_t, K), one selected set per token. Label: `eq:ch03-top-k-selection-without-dispatch`.

Detailed section file: `section_plans/ch03/03-top-k-selection-without-dispatch.md`

### 3.4 Naive token-by-token dispatch

**Objective:** Implement dispatch with loops first so the control flow is unmistakable.

**Mini-example:** For each token and selected expert, call the expert and add gate-weighted output.

**Development flow:**

1. Open with the local problem: Implement dispatch with loops first so the control flow is unmistakable.
2. Introduce the schematic: Loop-based dispatch arrows from token rows to selected expert calls.
3. Walk through mechanics and shapes using: routed_out_t = sum_{j=1}^K gate_{tj} expert_{idx_{tj}}(x_t).
4. Implement or pseudocode: NaiveMoELayer forward pass using explicit token and expert loops.
5. Verify with: Compare output shape to dense FFN output and inspect gates per token.
6. Bridge: The naive layer works, but the router choices are still fragile; top-1 routing exposes this clearly.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch03/fig-naive-token-by-token-dispatch.tex` - TikZ figure. Caption placeholder: Loop-based dispatch arrows from token rows to selected expert calls. Label: `fig:ch03-naive-token-by-token-dispatch`.
- `latex_book_skeleton/tables/ch03/tab-naive-token-by-token-dispatch.tex` - Table. Caption placeholder: Naive dispatch variables and their role in the loop. Label: `tab:ch03-naive-token-by-token-dispatch`.
- `latex_book_skeleton/listings/ch03/lst-naive-token-by-token-dispatch.tex` - Python listing. Caption placeholder: NaiveMoELayer forward pass using explicit token and expert loops. Label: `lst:ch03-naive-token-by-token-dispatch`.
- `latex_book_skeleton/equations/ch03/eq-naive-token-by-token-dispatch.tex` - Equation artifact. Placeholder: routed_out_t = sum_{j=1}^K gate_{tj} expert_{idx_{tj}}(x_t). Label: `eq:ch03-naive-token-by-token-dispatch`.

Detailed section file: `section_plans/ch03/04-naive-token-by-token-dispatch.md`

### 3.5 Shape and gradient checks

**Objective:** Make the first MoE layer testable before introducing more routing variants.

**Mini-example:** Run a two-layer smoke model and confirm all experts receive gradients when selected.

**Development flow:**

1. Open with the local problem: Make the first MoE layer testable before introducing more routing variants.
2. Introduce the schematic: Gradient flow diagram from loss through combine weights into router and selected experts.
3. Walk through mechanics and shapes using: Loss gradient reaches gate and expert paths through the weighted sum.
4. Implement or pseudocode: Unit tests for MoELayer output shape and gradient presence.
5. Verify with: Count selected expert IDs and check nonzero gradients for selected expert parameters.
6. Bridge: The next chapter simplifies to top-1 routing to teach sparse dispatch one expert at a time.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch03/fig-shape-and-gradient-checks.tex` - TikZ figure. Caption placeholder: Gradient flow diagram from loss through combine weights into router and selected experts. Label: `fig:ch03-shape-and-gradient-checks`.
- `latex_book_skeleton/tables/ch03/tab-shape-and-gradient-checks.tex` - Table. Caption placeholder: Test cases for shapes, gate sums, selected expert counts, and gradients. Label: `tab:ch03-shape-and-gradient-checks`.
- `latex_book_skeleton/listings/ch03/lst-shape-and-gradient-checks.tex` - Python listing. Caption placeholder: Unit tests for MoELayer output shape and gradient presence. Label: `lst:ch03-shape-and-gradient-checks`.
- `latex_book_skeleton/equations/ch03/eq-shape-and-gradient-checks.tex` - Equation artifact. Placeholder: Loss gradient reaches gate and expert paths through the weighted sum. Label: `eq:ch03-shape-and-gradient-checks`.

Detailed section file: `section_plans/ch03/05-shape-and-gradient-checks.md`

### 3.6 Chapter summary and handoff

**Objective:** Summarize the first complete MoE layer and prepare for routing variants.

**Mini-example:** Re-run the four-token example through ExpertMLP, Router, top-k, dispatch, and combine.

**Development flow:**

1. Open with the local problem: Summarize the first complete MoE layer and prepare for routing variants.
2. Introduce the schematic: End-to-end first MoE layer pipeline.
3. Walk through mechanics and shapes using: MoE layer invariant y has the same shape as x.
4. Implement or pseudocode: Minimal integration snippet replacing DenseFFN with NaiveMoELayer.
5. Verify with: Reader checkpoint: identify where routing, expert computation, and combine happen in code.
6. Bridge: Top-1 routing is the cleanest way to see sparse expert assignment and load imbalance.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch03/fig-chapter-summary-and-handoff.tex` - TikZ figure. Caption placeholder: End-to-end first MoE layer pipeline. Label: `fig:ch03-chapter-summary-and-handoff`.
- `latex_book_skeleton/tables/ch03/tab-chapter-summary-and-handoff.tex` - Table. Caption placeholder: Completed components and known limitations. Label: `tab:ch03-chapter-summary-and-handoff`.
- `latex_book_skeleton/listings/ch03/lst-chapter-summary-and-handoff.tex` - Python listing. Caption placeholder: Minimal integration snippet replacing DenseFFN with NaiveMoELayer. Label: `lst:ch03-chapter-summary-and-handoff`.
- `latex_book_skeleton/equations/ch03/eq-chapter-summary-and-handoff.tex` - Equation artifact. Placeholder: MoE layer invariant y has the same shape as x. Label: `eq:ch03-chapter-summary-and-handoff`.

Detailed section file: `section_plans/ch03/06-chapter-summary-and-handoff.md`
