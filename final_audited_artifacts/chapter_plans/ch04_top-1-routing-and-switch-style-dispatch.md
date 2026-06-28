# Chapter 4: Top-1 routing and Switch-style dispatch

**Part:** Part II - routing mechanics from scratch

**Role in the book:** Build the simplest sparse router and expose the expert-load problem.

## This chapter covers

- How top-1 routing sends each token to exactly one expert.
- How capacity and dropped tokens appear when experts are overloaded.
- How expert-load diagnostics make routing failures visible.

## Implementation milestone

Implement Top1Router, Top1MoELayer, routing masks, load histograms, and optional capacity handling.

## Section-by-section plan

### 4.1 Why top-1 routing is the simplest sparse case

**Objective:** Use one-expert-per-token routing to reduce the dispatch problem to assignment plus combine.

**Mini-example:** Route six tokens to four experts with K=1 and mark each token assignment.

**Development flow:**

1. Open with the local problem: Use one-expert-per-token routing to reduce the dispatch problem to assignment plus combine.
2. Introduce the schematic: Token rows each connected to one selected expert.
3. Walk through mechanics and shapes using: expert_idx_t = argmax_i score_{t,i}.
4. Implement or pseudocode: Top1Router forward pass returning expert_idx and gate.
5. Verify with: Verify each token has one expert and one scalar gate.
6. Bridge: The single expert ID can be converted into an assignment mask.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch04/fig-why-top-1-routing-is-the-simplest-sparse-case.tex` - TikZ figure. Caption placeholder: Token rows each connected to one selected expert. Label: `fig:ch04-why-top-1-routing-is-the-simplest-sparse-case`.
- `latex_book_skeleton/tables/ch04/tab-why-top-1-routing-is-the-simplest-sparse-case.tex` - Table. Caption placeholder: Top-1 routing variables compared with top-k routing variables. Label: `tab:ch04-why-top-1-routing-is-the-simplest-sparse-case`.
- `latex_book_skeleton/listings/ch04/lst-why-top-1-routing-is-the-simplest-sparse-case.tex` - Python listing. Caption placeholder: Top1Router forward pass returning expert_idx and gate. Label: `lst:ch04-why-top-1-routing-is-the-simplest-sparse-case`.
- `latex_book_skeleton/equations/ch04/eq-why-top-1-routing-is-the-simplest-sparse-case.tex` - Equation artifact. Placeholder: expert_idx_t = argmax_i score_{t,i}. Label: `eq:ch04-why-top-1-routing-is-the-simplest-sparse-case`.

Detailed section file: `section_plans/ch04/01-why-top-1-routing-is-the-simplest-sparse-case.md`

### 4.2 Assignment masks and expert buckets

**Objective:** Convert token expert IDs into per-expert token groups.

**Mini-example:** Bucket six token indices into four expert lists.

**Development flow:**

1. Open with the local problem: Convert token expert IDs into per-expert token groups.
2. Introduce the schematic: Assignment mask as a sparse N by E matrix and as expert buckets.
3. Walk through mechanics and shapes using: mask_{t,i} = 1 when expert_idx_t = i.
4. Implement or pseudocode: Build expert_to_token_indices from top-1 expert IDs.
5. Verify with: Sum the mask across experts to confirm each token is assigned once.
6. Bridge: Once tokens are bucketed, expert modules process only their assigned tokens.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch04/fig-assignment-masks-and-expert-buckets.tex` - TikZ figure. Caption placeholder: Assignment mask as a sparse N by E matrix and as expert buckets. Label: `fig:ch04-assignment-masks-and-expert-buckets`.
- `latex_book_skeleton/tables/ch04/tab-assignment-masks-and-expert-buckets.tex` - Table. Caption placeholder: Mask representation versus bucket representation trade-offs. Label: `tab:ch04-assignment-masks-and-expert-buckets`.
- `latex_book_skeleton/listings/ch04/lst-assignment-masks-and-expert-buckets.tex` - Python listing. Caption placeholder: Build expert_to_token_indices from top-1 expert IDs. Label: `lst:ch04-assignment-masks-and-expert-buckets`.
- `latex_book_skeleton/equations/ch04/eq-assignment-masks-and-expert-buckets.tex` - Equation artifact. Placeholder: mask_{t,i} = 1 when expert_idx_t = i. Label: `eq:ch04-assignment-masks-and-expert-buckets`.

Detailed section file: `section_plans/ch04/02-assignment-masks-and-expert-buckets.md`

### 4.3 Dispatching tokens to selected experts

**Objective:** Run each expert only on the tokens assigned to it and scatter outputs back to token order.

**Mini-example:** Expert 0 receives token rows [0,3], expert 1 receives [1], and empty experts are skipped.

**Development flow:**

1. Open with the local problem: Run each expert only on the tokens assigned to it and scatter outputs back to token order.
2. Introduce the schematic: Gather tokens into expert batches, process, then scatter back.
3. Walk through mechanics and shapes using: output[token_indices_i] = expert_i(x[token_indices_i]).
4. Implement or pseudocode: Top1MoELayer dispatch and scatter implementation.
5. Verify with: Assert output rows return to the original token order.
6. Bridge: Routing can overload an expert, so we need to define expert capacity.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch04/fig-dispatching-tokens-to-selected-experts.tex` - TikZ figure. Caption placeholder: Gather tokens into expert batches, process, then scatter back. Label: `fig:ch04-dispatching-tokens-to-selected-experts`.
- `latex_book_skeleton/tables/ch04/tab-dispatching-tokens-to-selected-experts.tex` - Table. Caption placeholder: Gather, expert batch, and scatter tensor shapes. Label: `tab:ch04-dispatching-tokens-to-selected-experts`.
- `latex_book_skeleton/listings/ch04/lst-dispatching-tokens-to-selected-experts.tex` - Python listing. Caption placeholder: Top1MoELayer dispatch and scatter implementation. Label: `lst:ch04-dispatching-tokens-to-selected-experts`.
- `latex_book_skeleton/equations/ch04/eq-dispatching-tokens-to-selected-experts.tex` - Equation artifact. Placeholder: output[token_indices_i] = expert_i(x[token_indices_i]). Label: `eq:ch04-dispatching-tokens-to-selected-experts`.

Detailed section file: `section_plans/ch04/03-dispatching-tokens-to-selected-experts.md`

### 4.4 Capacity and dropped tokens

**Objective:** Introduce the capacity factor and the consequences of too many tokens choosing the same expert.

**Mini-example:** Set capacity=2 for four experts and show what happens when four tokens select expert 0.

**Development flow:**

1. Open with the local problem: Introduce the capacity factor and the consequences of too many tokens choosing the same expert.
2. Introduce the schematic: Overloaded expert bucket with accepted and dropped token slots.
3. Walk through mechanics and shapes using: capacity = ceil(capacity_factor * N / E).
4. Implement or pseudocode: Capacity-aware top-1 dispatch with dropped-token accounting.
5. Verify with: Report dropped_token_count and per-expert accepted counts.
6. Bridge: Capacity exposes routing imbalance; histograms make the imbalance easy to see.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch04/fig-capacity-and-dropped-tokens.tex` - TikZ figure. Caption placeholder: Overloaded expert bucket with accepted and dropped token slots. Label: `fig:ch04-capacity-and-dropped-tokens`.
- `latex_book_skeleton/tables/ch04/tab-capacity-and-dropped-tokens.tex` - Table. Caption placeholder: Capacity factor, expert capacity, accepted tokens, dropped tokens, and residual fallback. Label: `tab:ch04-capacity-and-dropped-tokens`.
- `latex_book_skeleton/listings/ch04/lst-capacity-and-dropped-tokens.tex` - Python listing. Caption placeholder: Capacity-aware top-1 dispatch with dropped-token accounting. Label: `lst:ch04-capacity-and-dropped-tokens`.
- `latex_book_skeleton/equations/ch04/eq-capacity-and-dropped-tokens.tex` - Equation artifact. Placeholder: capacity = ceil(capacity_factor * N / E). Label: `eq:ch04-capacity-and-dropped-tokens`.

Detailed section file: `section_plans/ch04/04-capacity-and-dropped-tokens.md`

### 4.5 Load histograms and failure modes

**Objective:** Make expert collapse and underuse visible with simple diagnostics.

**Mini-example:** Create a synthetic router that sends most tokens to one expert and plot the load.

**Development flow:**

1. Open with the local problem: Make expert collapse and underuse visible with simple diagnostics.
2. Introduce the schematic: Expert-load histogram with one overloaded expert highlighted in imbalance red.
3. Walk through mechanics and shapes using: load_fraction_i = count_i / N.
4. Implement or pseudocode: Function that computes expert_load, load_fraction, and routing_entropy.
5. Verify with: Save a histogram and a warning if max load is much larger than average load.
6. Bridge: Top-1 is simple but brittle; top-2 routing gives each token a backup path and a weighted combine.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch04/fig-load-histograms-and-failure-modes.tex` - TikZ figure. Caption placeholder: Expert-load histogram with one overloaded expert highlighted in imbalance red. Label: `fig:ch04-load-histograms-and-failure-modes`.
- `latex_book_skeleton/tables/ch04/tab-load-histograms-and-failure-modes.tex` - Table. Caption placeholder: Failure modes: expert collapse, empty experts, high drop rate, low entropy. Label: `tab:ch04-load-histograms-and-failure-modes`.
- `latex_book_skeleton/listings/ch04/lst-load-histograms-and-failure-modes.tex` - Python listing. Caption placeholder: Function that computes expert_load, load_fraction, and routing_entropy. Label: `lst:ch04-load-histograms-and-failure-modes`.
- `latex_book_skeleton/equations/ch04/eq-load-histograms-and-failure-modes.tex` - Equation artifact. Placeholder: load_fraction_i = count_i / N. Label: `eq:ch04-load-histograms-and-failure-modes`.

Detailed section file: `section_plans/ch04/05-load-histograms-and-failure-modes.md`

### 4.6 Chapter summary and handoff

**Objective:** Consolidate top-1 routing as a working sparse layer and name its limitations.

**Mini-example:** Run the top-1 layer inside the dense decoder block and log load statistics.

**Development flow:**

1. Open with the local problem: Consolidate top-1 routing as a working sparse layer and name its limitations.
2. Introduce the schematic: Top-1 MoE block inside the Transformer decoder layer.
3. Walk through mechanics and shapes using: Top-1 output as one gated expert output per token.
4. Implement or pseudocode: Replace DenseFFN with Top1MoELayer in the baseline block.
5. Verify with: Compare validation loss smoke run with dense baseline, without claiming quality superiority.
6. Bridge: The next chapter generalizes the same layer to top-2 weighted expert combinations.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch04/fig-chapter-summary-and-handoff.tex` - TikZ figure. Caption placeholder: Top-1 MoE block inside the Transformer decoder layer. Label: `fig:ch04-chapter-summary-and-handoff`.
- `latex_book_skeleton/tables/ch04/tab-chapter-summary-and-handoff.tex` - Table. Caption placeholder: What top-1 solved versus what remains for top-2 routing. Label: `tab:ch04-chapter-summary-and-handoff`.
- `latex_book_skeleton/listings/ch04/lst-chapter-summary-and-handoff.tex` - Python listing. Caption placeholder: Replace DenseFFN with Top1MoELayer in the baseline block. Label: `lst:ch04-chapter-summary-and-handoff`.
- `latex_book_skeleton/equations/ch04/eq-chapter-summary-and-handoff.tex` - Equation artifact. Placeholder: Top-1 output as one gated expert output per token. Label: `eq:ch04-chapter-summary-and-handoff`.

Detailed section file: `section_plans/ch04/06-chapter-summary-and-handoff.md`
