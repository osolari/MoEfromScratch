# Chapter 6: Vectorized dispatch, capacity, and routing efficiency

**Part:** Part II - routing mechanics from scratch

**Role in the book:** Move from readable loops to scalable tensor operations without changing the MoE math.

## This chapter covers

- How flattened tokens and expert batches make MoE dispatch vectorizable.
- How capacity limits create predictable tensor sizes and overflow behavior.
- How to test equivalence between naive and vectorized implementations.

## Implementation milestone

Implement vectorized dispatch utilities, capacity-aware routing, and correctness tests against naive top-2 output.

## Section-by-section plan

### 6.1 Flattened tokens as the dispatch unit

**Objective:** Standardize on N=B*T flattened tokens so routing code ignores batch layout until the final reshape.

**Mini-example:** Flatten B=2, T=3, D=4 into N=6 token rows and recover B,T,D afterward.

**Development flow:**

1. Open with the local problem: Standardize on N=B*T flattened tokens so routing code ignores batch layout until the final reshape.
2. Introduce the schematic: Batch-sequence grid flattened into a token table for routing.
3. Walk through mechanics and shapes using: n = b*T + t maps (b,t) to flat token index.
4. Implement or pseudocode: flatten_tokens and unflatten_tokens helper functions.
5. Verify with: Round-trip flatten/unflatten equality check.
6. Bridge: Flat token rows can be sorted or bucketed by expert assignment.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch06/fig-flattened-tokens-as-the-dispatch-unit.tex` - TikZ figure. Caption placeholder: Batch-sequence grid flattened into a token table for routing. Label: `fig:ch06-flattened-tokens-as-the-dispatch-unit`.
- `latex_book_skeleton/tables/ch06/tab-flattened-tokens-as-the-dispatch-unit.tex` - Table. Caption placeholder: Mapping between batch index, time index, flat index, and token vector. Label: `tab:ch06-flattened-tokens-as-the-dispatch-unit`.
- `latex_book_skeleton/listings/ch06/lst-flattened-tokens-as-the-dispatch-unit.tex` - Python listing. Caption placeholder: flatten_tokens and unflatten_tokens helper functions. Label: `lst:ch06-flattened-tokens-as-the-dispatch-unit`.
- `latex_book_skeleton/equations/ch06/eq-flattened-tokens-as-the-dispatch-unit.tex` - Equation artifact. Placeholder: n = b*T + t maps (b,t) to flat token index. Label: `eq:ch06-flattened-tokens-as-the-dispatch-unit`.

Detailed section file: `section_plans/ch06/01-flattened-tokens-as-the-dispatch-unit.md`

### 6.2 Expert batch construction

**Objective:** Build dense per-expert mini-batches from sparse token assignments.

**Mini-example:** Create an expert batch tensor with shape (E, capacity, D).

**Development flow:**

1. Open with the local problem: Build dense per-expert mini-batches from sparse token assignments.
2. Introduce the schematic: Sparse token assignments packed into a fixed-size expert batch grid.
3. Walk through mechanics and shapes using: expert_batch[i, slot, :] = x_flat[token_idx].
4. Implement or pseudocode: pack_tokens_by_expert function for top-k assignments.
5. Verify with: Ensure each accepted route has exactly one expert slot.
6. Bridge: Fixed-size expert batches require a capacity rule.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch06/fig-expert-batch-construction.tex` - TikZ figure. Caption placeholder: Sparse token assignments packed into a fixed-size expert batch grid. Label: `fig:ch06-expert-batch-construction`.
- `latex_book_skeleton/tables/ch06/tab-expert-batch-construction.tex` - Table. Caption placeholder: expert_batch, combine_weights, token_indices, and slot_indices shapes. Label: `tab:ch06-expert-batch-construction`.
- `latex_book_skeleton/listings/ch06/lst-expert-batch-construction.tex` - Python listing. Caption placeholder: pack_tokens_by_expert function for top-k assignments. Label: `lst:ch06-expert-batch-construction`.
- `latex_book_skeleton/equations/ch06/eq-expert-batch-construction.tex` - Equation artifact. Placeholder: expert_batch[i, slot, :] = x_flat[token_idx]. Label: `eq:ch06-expert-batch-construction`.

Detailed section file: `section_plans/ch06/02-expert-batch-construction.md`

### 6.3 Capacity factors and overflow policy

**Objective:** Explain how capacity controls memory and what the implementation does with overflow routes.

**Mini-example:** Use N=12, E=4, K=2 and capacity factors 1.0 and 1.25.

**Development flow:**

1. Open with the local problem: Explain how capacity controls memory and what the implementation does with overflow routes.
2. Introduce the schematic: Capacity slots per expert with accepted, padded, and overflow routes.
3. Walk through mechanics and shapes using: capacity = ceil(capacity_factor * N*K / E).
4. Implement or pseudocode: compute_expert_capacity and overflow mask code.
5. Verify with: Log overflow route count and overflow fraction.
6. Bridge: After expert batches are processed, outputs must be unpacked and combined.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch06/fig-capacity-factors-and-overflow-policy.tex` - TikZ figure. Caption placeholder: Capacity slots per expert with accepted, padded, and overflow routes. Label: `fig:ch06-capacity-factors-and-overflow-policy`.
- `latex_book_skeleton/tables/ch06/tab-capacity-factors-and-overflow-policy.tex` - Table. Caption placeholder: Capacity factor scenarios and their accepted route counts. Label: `tab:ch06-capacity-factors-and-overflow-policy`.
- `latex_book_skeleton/listings/ch06/lst-capacity-factors-and-overflow-policy.tex` - Python listing. Caption placeholder: compute_expert_capacity and overflow mask code. Label: `lst:ch06-capacity-factors-and-overflow-policy`.
- `latex_book_skeleton/equations/ch06/eq-capacity-factors-and-overflow-policy.tex` - Equation artifact. Placeholder: capacity = ceil(capacity_factor * N*K / E). Label: `eq:ch06-capacity-factors-and-overflow-policy`.

Detailed section file: `section_plans/ch06/03-capacity-factors-and-overflow-policy.md`

### 6.4 Unpacking and weighted combine

**Objective:** Scatter expert-batch outputs back to token rows and apply route weights correctly.

**Mini-example:** One token receives two routes; one overflow route is skipped while the accepted route contributes.

**Development flow:**

1. Open with the local problem: Scatter expert-batch outputs back to token rows and apply route weights correctly.
2. Introduce the schematic: Expert outputs unpacked through token and slot indices into routed_out.
3. Walk through mechanics and shapes using: routed_out[token] += gate * expert_out[expert, slot].
4. Implement or pseudocode: unpack_expert_outputs function using index_add or scatter_add.
5. Verify with: Compare vectorized output to naive output when capacity is large enough for no overflow.
6. Bridge: The implementation is faster, but correctness tests must guard against silent routing mistakes.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch06/fig-unpacking-and-weighted-combine.tex` - TikZ figure. Caption placeholder: Expert outputs unpacked through token and slot indices into routed_out. Label: `fig:ch06-unpacking-and-weighted-combine`.
- `latex_book_skeleton/tables/ch06/tab-unpacking-and-weighted-combine.tex` - Table. Caption placeholder: Accepted route table: token, expert, slot, gate, and output contribution. Label: `tab:ch06-unpacking-and-weighted-combine`.
- `latex_book_skeleton/listings/ch06/lst-unpacking-and-weighted-combine.tex` - Python listing. Caption placeholder: unpack_expert_outputs function using index_add or scatter_add. Label: `lst:ch06-unpacking-and-weighted-combine`.
- `latex_book_skeleton/equations/ch06/eq-unpacking-and-weighted-combine.tex` - Equation artifact. Placeholder: routed_out[token] += gate * expert_out[expert, slot]. Label: `eq:ch06-unpacking-and-weighted-combine`.

Detailed section file: `section_plans/ch06/04-unpacking-and-weighted-combine.md`

### 6.5 Equivalence tests against the naive layer

**Objective:** Prove the vectorized implementation matches the simple implementation in the no-overflow case.

**Mini-example:** Use fixed router scores and identical expert weights for both layers.

**Development flow:**

1. Open with the local problem: Prove the vectorized implementation matches the simple implementation in the no-overflow case.
2. Introduce the schematic: Two implementation paths producing matching output tensors.
3. Walk through mechanics and shapes using: max_abs_diff = max(|y_naive - y_vec|).
4. Implement or pseudocode: pytest-style allclose test comparing naive and vectorized MoE.
5. Verify with: Fail if max_abs_diff exceeds tolerance in no-overflow settings.
6. Bridge: With efficient dispatch available, we can focus on the training losses that shape router behavior.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch06/fig-equivalence-tests-against-the-naive-layer.tex` - TikZ figure. Caption placeholder: Two implementation paths producing matching output tensors. Label: `fig:ch06-equivalence-tests-against-the-naive-layer`.
- `latex_book_skeleton/tables/ch06/tab-equivalence-tests-against-the-naive-layer.tex` - Table. Caption placeholder: Test matrix for K, E, D, capacity factor, dtype, and overflow setting. Label: `tab:ch06-equivalence-tests-against-the-naive-layer`.
- `latex_book_skeleton/listings/ch06/lst-equivalence-tests-against-the-naive-layer.tex` - Python listing. Caption placeholder: pytest-style allclose test comparing naive and vectorized MoE. Label: `lst:ch06-equivalence-tests-against-the-naive-layer`.
- `latex_book_skeleton/equations/ch06/eq-equivalence-tests-against-the-naive-layer.tex` - Equation artifact. Placeholder: max_abs_diff = max(|y_naive - y_vec|). Label: `eq:ch06-equivalence-tests-against-the-naive-layer`.

Detailed section file: `section_plans/ch06/05-equivalence-tests-against-the-naive-layer.md`

### 6.6 Chapter summary and handoff

**Objective:** Summarize the efficient routing pipeline and the new capacity diagnostics.

**Mini-example:** Trace one batch through flatten, top-k, pack, expert compute, unpack, and reshape.

**Development flow:**

1. Open with the local problem: Summarize the efficient routing pipeline and the new capacity diagnostics.
2. Introduce the schematic: Full vectorized dispatch pipeline.
3. Walk through mechanics and shapes using: No-overflow equivalence condition y_vec approx y_naive.
4. Implement or pseudocode: VectorizedMoELayer forward skeleton with named helper calls.
5. Verify with: Reader checkpoint: identify where dropped routes enter the output calculation.
6. Bridge: The next chapter adds router training objectives so experts are used more evenly.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch06/fig-chapter-summary-and-handoff.tex` - TikZ figure. Caption placeholder: Full vectorized dispatch pipeline. Label: `fig:ch06-chapter-summary-and-handoff`.
- `latex_book_skeleton/tables/ch06/tab-chapter-summary-and-handoff.tex` - Table. Caption placeholder: Naive versus vectorized implementation responsibilities. Label: `tab:ch06-chapter-summary-and-handoff`.
- `latex_book_skeleton/listings/ch06/lst-chapter-summary-and-handoff.tex` - Python listing. Caption placeholder: VectorizedMoELayer forward skeleton with named helper calls. Label: `lst:ch06-chapter-summary-and-handoff`.
- `latex_book_skeleton/equations/ch06/eq-chapter-summary-and-handoff.tex` - Equation artifact. Placeholder: No-overflow equivalence condition y_vec approx y_naive. Label: `eq:ch06-chapter-summary-and-handoff`.

Detailed section file: `section_plans/ch06/06-chapter-summary-and-handoff.md`
