# Chapter 12: Inference, performance, and scaling beyond the toy model

**Part:** Part V - inference and scale

**Role in the book:** Connect the from-scratch implementation to systems concerns without turning the book into a distributed-systems text.

## This chapter covers

- How MoE affects inference flow, batching, and active-parameter accounting.
- Why expert parallelism and all-to-all communication appear at larger scale.
- How to map MiniDeepSeekMoE concepts to production-scale MoE models responsibly.

## Implementation milestone

Add inference helpers, active-compute estimators, simple profiling scripts, and conceptual scaling diagrams.

## Section-by-section plan

### 12.1 Autoregressive inference with sparse FFNs

**Objective:** Explain what changes and what stays the same when a trained MoE model generates text one token at a time.

**Mini-example:** Generate one new token and trace attention, router, selected experts, and logits.

**Development flow:**

1. Open with the local problem: Explain what changes and what stays the same when a trained MoE model generates text one token at a time.
2. Introduce the schematic: One-token inference path through attention cache and MoE layer.
3. Walk through mechanics and shapes using: Per-step active expert calls equal layers_with_moe * K for one token.
4. Implement or pseudocode: generate function with routing metrics optionally returned per step.
5. Verify with: Print selected experts for each generated token in a short sample.
6. Bridge: Batching multiple requests complicates the expert batches.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch12/fig-autoregressive-inference-with-sparse-ffns.tex` - TikZ figure. Caption placeholder: One-token inference path through attention cache and MoE layer. Label: `fig:ch12-autoregressive-inference-with-sparse-ffns`.
- `latex_book_skeleton/tables/ch12/tab-autoregressive-inference-with-sparse-ffns.tex` - Table. Caption placeholder: Training-time versus inference-time routing tensors. Label: `tab:ch12-autoregressive-inference-with-sparse-ffns`.
- `latex_book_skeleton/listings/ch12/lst-autoregressive-inference-with-sparse-ffns.tex` - Python listing. Caption placeholder: generate function with routing metrics optionally returned per step. Label: `lst:ch12-autoregressive-inference-with-sparse-ffns`.
- `latex_book_skeleton/equations/ch12/eq-autoregressive-inference-with-sparse-ffns.tex` - Equation artifact. Placeholder: Per-step active expert calls equal layers_with_moe * K for one token. Label: `eq:ch12-autoregressive-inference-with-sparse-ffns`.

Detailed section file: `section_plans/ch12/01-autoregressive-inference-with-sparse-ffns.md`

### 12.2 Batching routed tokens at inference

**Objective:** Show why MoE inference wants tokens for the same expert to be grouped efficiently.

**Mini-example:** Two prompts in a batch route their next token to different experts.

**Development flow:**

1. Open with the local problem: Show why MoE inference wants tokens for the same expert to be grouped efficiently.
2. Introduce the schematic: Inference batch tokens packed into expert-specific microbatches.
3. Walk through mechanics and shapes using: Expert batch size distribution at generation step s.
4. Implement or pseudocode: profile_inference_routes function collecting per-step expert batch sizes.
5. Verify with: Histogram expert batch sizes over a generated sequence.
6. Bridge: Compute and memory estimates clarify where the toy implementation stops scaling.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch12/fig-batching-routed-tokens-at-inference.tex` - TikZ figure. Caption placeholder: Inference batch tokens packed into expert-specific microbatches. Label: `fig:ch12-batching-routed-tokens-at-inference`.
- `latex_book_skeleton/tables/ch12/tab-batching-routed-tokens-at-inference.tex` - Table. Caption placeholder: Inference batching challenges: uneven loads, small expert batches, padding, latency. Label: `tab:ch12-batching-routed-tokens-at-inference`.
- `latex_book_skeleton/listings/ch12/lst-batching-routed-tokens-at-inference.tex` - Python listing. Caption placeholder: profile_inference_routes function collecting per-step expert batch sizes. Label: `lst:ch12-batching-routed-tokens-at-inference`.
- `latex_book_skeleton/equations/ch12/eq-batching-routed-tokens-at-inference.tex` - Equation artifact. Placeholder: Expert batch size distribution at generation step s. Label: `eq:ch12-batching-routed-tokens-at-inference`.

Detailed section file: `section_plans/ch12/02-batching-routed-tokens-at-inference.md`

### 12.3 Compute, memory, and active-parameter accounting

**Objective:** Give readers a sober way to discuss total parameters, active parameters, and practical memory costs.

**Mini-example:** Compare dense FFN, 16x2 MoE, and 64x6 teaching config parameter counts.

**Development flow:**

1. Open with the local problem: Give readers a sober way to discuss total parameters, active parameters, and practical memory costs.
2. Introduce the schematic: Stacked bars for total parameters and active parameters per token.
3. Walk through mechanics and shapes using: Active expert FFN parameters per token approximately K times one routed expert plus shared experts.
4. Implement or pseudocode: estimate_moe_compute.py producing parameter and active-compute estimates.
5. Verify with: Check estimates against model.count_parameters breakdown.
6. Bridge: At production scale, experts are often spread across devices, introducing communication.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch12/fig-compute-memory-and-active-parameter-accounting.tex` - TikZ figure. Caption placeholder: Stacked bars for total parameters and active parameters per token. Label: `fig:ch12-compute-memory-and-active-parameter-accounting`.
- `latex_book_skeleton/tables/ch12/tab-compute-memory-and-active-parameter-accounting.tex` - Table. Caption placeholder: Total parameters, active parameters, estimated activation memory, and expert calls by config. Label: `tab:ch12-compute-memory-and-active-parameter-accounting`.
- `latex_book_skeleton/listings/ch12/lst-compute-memory-and-active-parameter-accounting.tex` - Python listing. Caption placeholder: estimate_moe_compute.py producing parameter and active-compute estimates. Label: `lst:ch12-compute-memory-and-active-parameter-accounting`.
- `latex_book_skeleton/equations/ch12/eq-compute-memory-and-active-parameter-accounting.tex` - Equation artifact. Placeholder: Active expert FFN parameters per token approximately K times one routed expert plus shared experts. Label: `eq:ch12-compute-memory-and-active-parameter-accounting`.

Detailed section file: `section_plans/ch12/03-compute-memory-and-active-parameter-accounting.md`

### 12.4 Expert parallelism and all-to-all communication

**Objective:** Explain the systems picture conceptually while keeping implementation out of scope.

**Mini-example:** Two devices each host two experts; tokens must move to the device containing their selected experts.

**Development flow:**

1. Open with the local problem: Explain the systems picture conceptually while keeping implementation out of scope.
2. Introduce the schematic: Tokens routed across devices through an all-to-all exchange, expert compute, and return exchange.
3. Walk through mechanics and shapes using: Communication volume depends on routed token count, D, K, and bytes per element.
4. Implement or pseudocode: Conceptual pseudocode for distributed dispatch without runnable distributed code.
5. Verify with: Thought experiment table estimating routed activation traffic for a small config.
6. Bridge: This systems view helps map the toy model to public large-MoE architecture descriptions.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch12/fig-expert-parallelism-and-all-to-all-communication.tex` - TikZ figure. Caption placeholder: Tokens routed across devices through an all-to-all exchange, expert compute, and return exchange. Label: `fig:ch12-expert-parallelism-and-all-to-all-communication`.
- `latex_book_skeleton/tables/ch12/tab-expert-parallelism-and-all-to-all-communication.tex` - Table. Caption placeholder: Single-device MoE versus expert-parallel MoE responsibilities. Label: `tab:ch12-expert-parallelism-and-all-to-all-communication`.
- `latex_book_skeleton/listings/ch12/lst-expert-parallelism-and-all-to-all-communication.tex` - Python listing. Caption placeholder: Conceptual pseudocode for distributed dispatch without runnable distributed code. Label: `lst:ch12-expert-parallelism-and-all-to-all-communication`.
- `latex_book_skeleton/equations/ch12/eq-expert-parallelism-and-all-to-all-communication.tex` - Equation artifact. Placeholder: Communication volume depends on routed token count, D, K, and bytes per element. Label: `eq:ch12-expert-parallelism-and-all-to-all-communication`.

Detailed section file: `section_plans/ch12/04-expert-parallelism-and-all-to-all-communication.md`

### 12.5 Mapping the book model to production MoE families

**Objective:** Connect MiniDeepSeekMoE pieces to broader MoE designs while staying honest about omitted details.

**Mini-example:** Map top-k routing, shared experts, fine-grained experts, and router bias to the final reference model vocabulary.

**Development flow:**

1. Open with the local problem: Connect MiniDeepSeekMoE pieces to broader MoE designs while staying honest about omitted details.
2. Introduce the schematic: Concept map from book components to larger MoE system components.
3. Walk through mechanics and shapes using: Scaling identity: same layer contract, larger E, larger D, more devices.
4. Implement or pseudocode: Config comparison snippet showing smoke, default, and larger teaching configs.
5. Verify with: Reader checkpoint: identify which chapter implemented each production analogue.
6. Bridge: The book closes by summarizing the reusable mental model.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch12/fig-mapping-the-book-model-to-production-moe-families.tex` - TikZ figure. Caption placeholder: Concept map from book components to larger MoE system components. Label: `fig:ch12-mapping-the-book-model-to-production-moe-families`.
- `latex_book_skeleton/tables/ch12/tab-mapping-the-book-model-to-production-moe-families.tex` - Table. Caption placeholder: Book implementation feature, production analogue, and what remains out of scope. Label: `tab:ch12-mapping-the-book-model-to-production-moe-families`.
- `latex_book_skeleton/listings/ch12/lst-mapping-the-book-model-to-production-moe-families.tex` - Python listing. Caption placeholder: Config comparison snippet showing smoke, default, and larger teaching configs. Label: `lst:ch12-mapping-the-book-model-to-production-moe-families`.
- `latex_book_skeleton/equations/ch12/eq-mapping-the-book-model-to-production-moe-families.tex` - Equation artifact. Placeholder: Scaling identity: same layer contract, larger E, larger D, more devices. Label: `eq:ch12-mapping-the-book-model-to-production-moe-families`.

Detailed section file: `section_plans/ch12/05-mapping-the-book-model-to-production-moe-families.md`

### 12.6 Book summary and next steps

**Objective:** End with a coherent picture of MoE as a route-execute-combine layer embedded in a decoder.

**Mini-example:** Trace one token through the final model using the vocabulary from every part of the book.

**Development flow:**

1. Open with the local problem: End with a coherent picture of MoE as a route-execute-combine layer embedded in a decoder.
2. Introduce the schematic: Complete route-execute-combine summary diagram with training and inference diagnostics around it.
3. Walk through mechanics and shapes using: Final MiniDeepSeekMoE layer equation repeated as the book endpoint.
4. Implement or pseudocode: Extension checklist: add RMSNorm, alternate attention, larger datasets, or distributed dispatch.
5. Verify with: Final self-test: build, train smoke, inspect routing, sample text, and explain limitations.
6. Bridge: No next chapter; point readers to appendices and experiments they can extend.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch12/fig-book-summary-and-next-steps.tex` - TikZ figure. Caption placeholder: Complete route-execute-combine summary diagram with training and inference diagnostics around it. Label: `fig:ch12-book-summary-and-next-steps`.
- `latex_book_skeleton/tables/ch12/tab-book-summary-and-next-steps.tex` - Table. Caption placeholder: Reader capabilities after finishing the book and possible extensions. Label: `tab:ch12-book-summary-and-next-steps`.
- `latex_book_skeleton/listings/ch12/lst-book-summary-and-next-steps.tex` - Python listing. Caption placeholder: Extension checklist: add RMSNorm, alternate attention, larger datasets, or distributed dispatch. Label: `lst:ch12-book-summary-and-next-steps`.
- `latex_book_skeleton/equations/ch12/eq-book-summary-and-next-steps.tex` - Equation artifact. Placeholder: Final MiniDeepSeekMoE layer equation repeated as the book endpoint. Label: `eq:ch12-book-summary-and-next-steps`.

Detailed section file: `section_plans/ch12/06-book-summary-and-next-steps.md`
