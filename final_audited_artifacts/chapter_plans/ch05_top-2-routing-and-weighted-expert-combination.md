# Chapter 5: Top-2 routing and weighted expert combination

**Part:** Part II - routing mechanics from scratch

**Role in the book:** Generalize sparse routing so each token can combine two expert transformations.

## This chapter covers

- How top-2 routing keeps sparse compute while reducing one-expert brittleness.
- How selected scores become normalized gates for weighted expert outputs.
- How to compare top-1 and top-2 layers with the same diagnostics.

## Implementation milestone

Implement Top2Router and Top2MoELayer with normalized gates, duplicate-safe dispatch, and comparison diagnostics.

## Section-by-section plan

### 5.1 Why top-2 changes the routing story

**Objective:** Explain top-2 routing as sparse ensemble behavior at the token level.

**Mini-example:** Use four tokens and four experts; each token chooses two experts with different weights.

**Development flow:**

1. Open with the local problem: Explain top-2 routing as sparse ensemble behavior at the token level.
2. Introduce the schematic: Token routes split into two weighted paths.
3. Walk through mechanics and shapes using: Each selected set S_t contains K=2 expert IDs.
4. Implement or pseudocode: Config switch from K=1 to K=2 and resulting tensor shapes.
5. Verify with: Compare active expert calls per token for K=1 and K=2.
6. Bridge: To make top-2 work, selected scores must become stable combine weights.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch05/fig-why-top-2-changes-the-routing-story.tex` - TikZ figure. Caption placeholder: Token routes split into two weighted paths. Label: `fig:ch05-why-top-2-changes-the-routing-story`.
- `latex_book_skeleton/tables/ch05/tab-why-top-2-changes-the-routing-story.tex` - Table. Caption placeholder: Top-1 versus top-2 routing behavior, cost, and diagnostics. Label: `tab:ch05-why-top-2-changes-the-routing-story`.
- `latex_book_skeleton/listings/ch05/lst-why-top-2-changes-the-routing-story.tex` - Python listing. Caption placeholder: Config switch from K=1 to K=2 and resulting tensor shapes. Label: `lst:ch05-why-top-2-changes-the-routing-story`.
- `latex_book_skeleton/equations/ch05/eq-why-top-2-changes-the-routing-story.tex` - Equation artifact. Placeholder: Each selected set S_t contains K=2 expert IDs. Label: `eq:ch05-why-top-2-changes-the-routing-story`.

Detailed section file: `section_plans/ch05/01-why-top-2-changes-the-routing-story.md`

### 5.2 Normalizing selected router scores

**Objective:** Turn top-2 scores into gates that sum to one for each token.

**Mini-example:** Normalize selected scores [0.8, 0.2] and [0.51, 0.49] and compare combines.

**Development flow:**

1. Open with the local problem: Turn top-2 scores into gates that sum to one for each token.
2. Introduce the schematic: Top-2 score row transformed into a two-weight gate vector.
3. Walk through mechanics and shapes using: gate_{tj} = score_{t,idx_{tj}} / sum_l score_{t,idx_{tl}}.
4. Implement or pseudocode: selected_scores / selected_scores.sum(dim=-1, keepdim=True).
5. Verify with: Assert torch.allclose(gates.sum(-1), ones).
6. Bridge: The normalized gates weight two expert outputs per token.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch05/fig-normalizing-selected-router-scores.tex` - TikZ figure. Caption placeholder: Top-2 score row transformed into a two-weight gate vector. Label: `fig:ch05-normalizing-selected-router-scores`.
- `latex_book_skeleton/tables/ch05/tab-normalizing-selected-router-scores.tex` - Table. Caption placeholder: Raw scores, selected scores, normalized gates, and gate sums. Label: `tab:ch05-normalizing-selected-router-scores`.
- `latex_book_skeleton/listings/ch05/lst-normalizing-selected-router-scores.tex` - Python listing. Caption placeholder: selected_scores / selected_scores.sum(dim=-1, keepdim=True). Label: `lst:ch05-normalizing-selected-router-scores`.
- `latex_book_skeleton/equations/ch05/eq-normalizing-selected-router-scores.tex` - Equation artifact. Placeholder: gate_{tj} = score_{t,idx_{tj}} / sum_l score_{t,idx_{tl}}. Label: `eq:ch05-normalizing-selected-router-scores`.

Detailed section file: `section_plans/ch05/02-normalizing-selected-router-scores.md`

### 5.3 Dispatch for two expert paths per token

**Objective:** Adapt the dispatch loop so each selected expert path contributes to the same output row.

**Mini-example:** Token 0 goes to experts 1 and 3; both outputs are accumulated into output[0].

**Development flow:**

1. Open with the local problem: Adapt the dispatch loop so each selected expert path contributes to the same output row.
2. Introduce the schematic: Two paths per token gathered into expert batches and accumulated back.
3. Walk through mechanics and shapes using: out_t += gate_{tj} expert_{idx_{tj}}(x_t).
4. Implement or pseudocode: Top2MoELayer forward pass with nested selected-expert accumulation.
5. Verify with: Check output changes when gates are manually swapped.
6. Bridge: Top-2 dispatch is correct but still slow; vectorization comes after the routing math is clear.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch05/fig-dispatch-for-two-expert-paths-per-token.tex` - TikZ figure. Caption placeholder: Two paths per token gathered into expert batches and accumulated back. Label: `fig:ch05-dispatch-for-two-expert-paths-per-token`.
- `latex_book_skeleton/tables/ch05/tab-dispatch-for-two-expert-paths-per-token.tex` - Table. Caption placeholder: Data structures for topk_idx, gates, expert batches, and output accumulation. Label: `tab:ch05-dispatch-for-two-expert-paths-per-token`.
- `latex_book_skeleton/listings/ch05/lst-dispatch-for-two-expert-paths-per-token.tex` - Python listing. Caption placeholder: Top2MoELayer forward pass with nested selected-expert accumulation. Label: `lst:ch05-dispatch-for-two-expert-paths-per-token`.
- `latex_book_skeleton/equations/ch05/eq-dispatch-for-two-expert-paths-per-token.tex` - Equation artifact. Placeholder: out_t += gate_{tj} expert_{idx_{tj}}(x_t). Label: `eq:ch05-dispatch-for-two-expert-paths-per-token`.

Detailed section file: `section_plans/ch05/03-dispatch-for-two-expert-paths-per-token.md`

### 5.4 Comparing top-1 and top-2 diagnostics

**Objective:** Use the same metrics to show how K changes load, drop rate, and routing entropy.

**Mini-example:** Run the same random batch through top-1 and top-2 routers with the same scores.

**Development flow:**

1. Open with the local problem: Use the same metrics to show how K changes load, drop rate, and routing entropy.
2. Introduce the schematic: Side-by-side expert load histograms for K=1 and K=2.
3. Walk through mechanics and shapes using: Active expert calls equal N*K before capacity limits.
4. Implement or pseudocode: compare_routing_modes(router_scores, k_values=[1,2]).
5. Verify with: Save a comparison table and one histogram per routing mode.
6. Bridge: Once routing variants share diagnostics, the next challenge is making dispatch less loop-heavy.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch05/fig-comparing-top-1-and-top-2-diagnostics.tex` - TikZ figure. Caption placeholder: Side-by-side expert load histograms for K=1 and K=2. Label: `fig:ch05-comparing-top-1-and-top-2-diagnostics`.
- `latex_book_skeleton/tables/ch05/tab-comparing-top-1-and-top-2-diagnostics.tex` - Table. Caption placeholder: Comparison rows for active calls, max load, entropy, and gate concentration. Label: `tab:ch05-comparing-top-1-and-top-2-diagnostics`.
- `latex_book_skeleton/listings/ch05/lst-comparing-top-1-and-top-2-diagnostics.tex` - Python listing. Caption placeholder: compare_routing_modes(router_scores, k_values=[1,2]). Label: `lst:ch05-comparing-top-1-and-top-2-diagnostics`.
- `latex_book_skeleton/equations/ch05/eq-comparing-top-1-and-top-2-diagnostics.tex` - Equation artifact. Placeholder: Active expert calls equal N*K before capacity limits. Label: `eq:ch05-comparing-top-1-and-top-2-diagnostics`.

Detailed section file: `section_plans/ch05/04-comparing-top-1-and-top-2-diagnostics.md`

### 5.5 Numerical stability in top-k gates

**Objective:** Prevent gate normalization edge cases before they become training bugs.

**Mini-example:** Use tiny selected scores and demonstrate epsilon-safe normalization.

**Development flow:**

1. Open with the local problem: Prevent gate normalization edge cases before they become training bugs.
2. Introduce the schematic: Gate normalization failure and epsilon-stabilized path.
3. Walk through mechanics and shapes using: gate = selected_scores / clamp(sum(selected_scores), eps).
4. Implement or pseudocode: stable_normalize_selected_scores function with epsilon and dtype checks.
5. Verify with: Unit tests for finite gates and gradients under small scores.
6. Bridge: Now that top-2 is correct, we can rewrite the dispatch to scale beyond tiny examples.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch05/fig-numerical-stability-in-top-k-gates.tex` - TikZ figure. Caption placeholder: Gate normalization failure and epsilon-stabilized path. Label: `fig:ch05-numerical-stability-in-top-k-gates`.
- `latex_book_skeleton/tables/ch05/tab-numerical-stability-in-top-k-gates.tex` - Table. Caption placeholder: Potential failures: zero sums, dtype mismatch, overflow, and unintended detached gates. Label: `tab:ch05-numerical-stability-in-top-k-gates`.
- `latex_book_skeleton/listings/ch05/lst-numerical-stability-in-top-k-gates.tex` - Python listing. Caption placeholder: stable_normalize_selected_scores function with epsilon and dtype checks. Label: `lst:ch05-numerical-stability-in-top-k-gates`.
- `latex_book_skeleton/equations/ch05/eq-numerical-stability-in-top-k-gates.tex` - Equation artifact. Placeholder: gate = selected_scores / clamp(sum(selected_scores), eps). Label: `eq:ch05-numerical-stability-in-top-k-gates`.

Detailed section file: `section_plans/ch05/05-numerical-stability-in-top-k-gates.md`

### 5.6 Chapter summary and handoff

**Objective:** Lock in the top-2 routing contract used by MiniDeepSeekMoE.

**Mini-example:** Trace one token through score, top-2 indices, gates, two experts, and final output.

**Development flow:**

1. Open with the local problem: Lock in the top-2 routing contract used by MiniDeepSeekMoE.
2. Introduce the schematic: Top-2 MoE layer end-to-end tensor map.
3. Walk through mechanics and shapes using: MoE output as a normalized weighted sum over two experts.
4. Implement or pseudocode: Test fixture that instantiates K=2 MoELayer and checks shape plus gate sums.
5. Verify with: Reader checkpoint: explain why gates sum to one after selecting top-k only.
6. Bridge: The next chapter keeps the same math but changes the implementation to vectorized dispatch and capacity-aware batching.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch05/fig-chapter-summary-and-handoff.tex` - TikZ figure. Caption placeholder: Top-2 MoE layer end-to-end tensor map. Label: `fig:ch05-chapter-summary-and-handoff`.
- `latex_book_skeleton/tables/ch05/tab-chapter-summary-and-handoff.tex` - Table. Caption placeholder: Top-2 contracts that later chapters must preserve. Label: `tab:ch05-chapter-summary-and-handoff`.
- `latex_book_skeleton/listings/ch05/lst-chapter-summary-and-handoff.tex` - Python listing. Caption placeholder: Test fixture that instantiates K=2 MoELayer and checks shape plus gate sums. Label: `lst:ch05-chapter-summary-and-handoff`.
- `latex_book_skeleton/equations/ch05/eq-chapter-summary-and-handoff.tex` - Equation artifact. Placeholder: MoE output as a normalized weighted sum over two experts. Label: `eq:ch05-chapter-summary-and-handoff`.

Detailed section file: `section_plans/ch05/06-chapter-summary-and-handoff.md`
