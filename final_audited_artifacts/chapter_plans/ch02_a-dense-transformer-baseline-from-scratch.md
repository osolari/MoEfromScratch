# Chapter 2: A dense Transformer baseline from scratch

**Part:** Part I - foundations and baseline

**Role in the book:** Build a minimal decoder-only language model before replacing the FFN with MoE.

## This chapter covers

- The tensor path through embeddings, causal attention, dense FFN, residuals, and logits.
- A compact PyTorch baseline that trains and samples on a small dataset.
- The baseline diagnostics needed to compare dense and sparse variants later.

## Implementation milestone

Produce a dense decoder implementation, train loop, sample script, and validation-loss baseline.

## Section-by-section plan

### 2.1 Dataset and token batches

**Objective:** Create the small next-token prediction pipeline used for every model variant.

**Mini-example:** Load a short text corpus, tokenize it, and create B=2, T=8 training examples.

**Development flow:**

1. Open with the local problem: Create the small next-token prediction pipeline used for every model variant.
2. Introduce the schematic: Text to token IDs to input-target shifted batches.
3. Walk through mechanics and shapes using: Next-token objective index relation target[t] = input[t+1].
4. Implement or pseudocode: Minimal get_batch function with input and target shifts.
5. Verify with: Print the first input-target pair and decode it to verify shifting.
6. Bridge: Token IDs become vectors through embeddings and positions.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch02/fig-dataset-and-token-batches.tex` - TikZ figure. Caption placeholder: Text to token IDs to input-target shifted batches. Label: `fig:ch02-dataset-and-token-batches`.
- `latex_book_skeleton/tables/ch02/tab-dataset-and-token-batches.tex` - Table. Caption placeholder: Batch tensor shapes and dataloader responsibilities. Label: `tab:ch02-dataset-and-token-batches`.
- `latex_book_skeleton/listings/ch02/lst-dataset-and-token-batches.tex` - Python listing. Caption placeholder: Minimal get_batch function with input and target shifts. Label: `lst:ch02-dataset-and-token-batches`.
- `latex_book_skeleton/equations/ch02/eq-dataset-and-token-batches.tex` - Equation artifact. Placeholder: Next-token objective index relation target[t] = input[t+1]. Label: `eq:ch02-dataset-and-token-batches`.

Detailed section file: `section_plans/ch02/01-dataset-and-token-batches.md`

### 2.2 Token and position embeddings

**Objective:** Implement the entry point that maps integer token IDs to dense vectors.

**Mini-example:** Use vocab_size=32, block_size=8, and d_model=16 to inspect embedding shapes.

**Development flow:**

1. Open with the local problem: Implement the entry point that maps integer token IDs to dense vectors.
2. Introduce the schematic: Token IDs and position IDs summed into the model input tensor.
3. Walk through mechanics and shapes using: x = token_embedding(idx) + position_embedding(pos).
4. Implement or pseudocode: Embedding module forward pass returning x with shape (B,T,D).
5. Verify with: Assert output shape and confirm gradients flow to both embedding tables.
6. Bridge: The embedded sequence now enters causal self-attention.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch02/fig-token-and-position-embeddings.tex` - TikZ figure. Caption placeholder: Token IDs and position IDs summed into the model input tensor. Label: `fig:ch02-token-and-position-embeddings`.
- `latex_book_skeleton/tables/ch02/tab-token-and-position-embeddings.tex` - Table. Caption placeholder: Embedding parameter counts and output shapes. Label: `tab:ch02-token-and-position-embeddings`.
- `latex_book_skeleton/listings/ch02/lst-token-and-position-embeddings.tex` - Python listing. Caption placeholder: Embedding module forward pass returning x with shape (B,T,D). Label: `lst:ch02-token-and-position-embeddings`.
- `latex_book_skeleton/equations/ch02/eq-token-and-position-embeddings.tex` - Equation artifact. Placeholder: x = token_embedding(idx) + position_embedding(pos). Label: `eq:ch02-token-and-position-embeddings`.

Detailed section file: `section_plans/ch02/02-token-and-position-embeddings.md`

### 2.3 Causal self-attention as the context path

**Objective:** Build enough attention to make the baseline a real decoder while keeping MoE focus on the FFN.

**Mini-example:** Trace a single attention head with B=1, T=4, D=8.

**Development flow:**

1. Open with the local problem: Build enough attention to make the baseline a real decoder while keeping MoE focus on the FFN.
2. Introduce the schematic: Causal mask applied to attention scores before softmax.
3. Walk through mechanics and shapes using: Masked attention softmax(QK^T / sqrt(d_head))V.
4. Implement or pseudocode: Compact multi-head causal attention module.
5. Verify with: Check that a token cannot attend to future positions.
6. Bridge: After attention mixes context, the dense FFN transforms each token independently.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch02/fig-causal-self-attention-as-the-context-path.tex` - TikZ figure. Caption placeholder: Causal mask applied to attention scores before softmax. Label: `fig:ch02-causal-self-attention-as-the-context-path`.
- `latex_book_skeleton/tables/ch02/tab-causal-self-attention-as-the-context-path.tex` - Table. Caption placeholder: Q, K, V, score, probability, and output shapes. Label: `tab:ch02-causal-self-attention-as-the-context-path`.
- `latex_book_skeleton/listings/ch02/lst-causal-self-attention-as-the-context-path.tex` - Python listing. Caption placeholder: Compact multi-head causal attention module. Label: `lst:ch02-causal-self-attention-as-the-context-path`.
- `latex_book_skeleton/equations/ch02/eq-causal-self-attention-as-the-context-path.tex` - Equation artifact. Placeholder: Masked attention softmax(QK^T / sqrt(d_head))V. Label: `eq:ch02-causal-self-attention-as-the-context-path`.

Detailed section file: `section_plans/ch02/03-causal-self-attention-as-the-context-path.md`

### 2.4 Dense feed-forward block as the replacement target

**Objective:** Implement the dense FFN in a way that makes the later expert replacement obvious.

**Mini-example:** Apply the same MLP to every token in a B*T flattened view.

**Development flow:**

1. Open with the local problem: Implement the dense FFN in a way that makes the later expert replacement obvious.
2. Introduce the schematic: Dense FFN applied independently to each token row.
3. Walk through mechanics and shapes using: FFN(x) = W_2 activation(W_1 x + b_1) + b_2.
4. Implement or pseudocode: FeedForward module with Linear, activation, Linear.
5. Verify with: Confirm FFN preserves the final D dimension.
6. Bridge: Attention and FFN combine inside a residual decoder block.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch02/fig-dense-feed-forward-block-as-the-replacement-target.tex` - TikZ figure. Caption placeholder: Dense FFN applied independently to each token row. Label: `fig:ch02-dense-feed-forward-block-as-the-replacement-target`.
- `latex_book_skeleton/tables/ch02/tab-dense-feed-forward-block-as-the-replacement-target.tex` - Table. Caption placeholder: Dense FFN parameters compared with one future expert MLP. Label: `tab:ch02-dense-feed-forward-block-as-the-replacement-target`.
- `latex_book_skeleton/listings/ch02/lst-dense-feed-forward-block-as-the-replacement-target.tex` - Python listing. Caption placeholder: FeedForward module with Linear, activation, Linear. Label: `lst:ch02-dense-feed-forward-block-as-the-replacement-target`.
- `latex_book_skeleton/equations/ch02/eq-dense-feed-forward-block-as-the-replacement-target.tex` - Equation artifact. Placeholder: FFN(x) = W_2 activation(W_1 x + b_1) + b_2. Label: `eq:ch02-dense-feed-forward-block-as-the-replacement-target`.

Detailed section file: `section_plans/ch02/04-dense-feed-forward-block-as-the-replacement-target.md`

### 2.5 Training loop and sampling baseline

**Objective:** Train the dense model long enough to create a trustworthy comparison anchor.

**Mini-example:** Run a smoke train for a few iterations and sample a short continuation.

**Development flow:**

1. Open with the local problem: Train the dense model long enough to create a trustworthy comparison anchor.
2. Introduce the schematic: Training loop pipeline: batch, forward, loss, backward, optimizer, sample.
3. Walk through mechanics and shapes using: Cross-entropy over shifted logits and targets.
4. Implement or pseudocode: Train step with loss, backward pass, clipping, optimizer step, and logging.
5. Verify with: Track train and validation loss plus samples at fixed intervals.
6. Bridge: Now that the dense baseline works, the next chapter isolates the expert and router pieces.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch02/fig-training-loop-and-sampling-baseline.tex` - TikZ figure. Caption placeholder: Training loop pipeline: batch, forward, loss, backward, optimizer, sample. Label: `fig:ch02-training-loop-and-sampling-baseline`.
- `latex_book_skeleton/tables/ch02/tab-training-loop-and-sampling-baseline.tex` - Table. Caption placeholder: Baseline configuration fields and default smoke-test values. Label: `tab:ch02-training-loop-and-sampling-baseline`.
- `latex_book_skeleton/listings/ch02/lst-training-loop-and-sampling-baseline.tex` - Python listing. Caption placeholder: Train step with loss, backward pass, clipping, optimizer step, and logging. Label: `lst:ch02-training-loop-and-sampling-baseline`.
- `latex_book_skeleton/equations/ch02/eq-training-loop-and-sampling-baseline.tex` - Equation artifact. Placeholder: Cross-entropy over shifted logits and targets. Label: `eq:ch02-training-loop-and-sampling-baseline`.

Detailed section file: `section_plans/ch02/05-training-loop-and-sampling-baseline.md`

### 2.6 Baseline diagnostics and comparison slots

**Objective:** Prepare diagnostic hooks that will later compare dense and sparse models fairly.

**Mini-example:** Create a metrics dictionary with loss, tokens/sec, parameter count, and activation estimate.

**Development flow:**

1. Open with the local problem: Prepare diagnostic hooks that will later compare dense and sparse models fairly.
2. Introduce the schematic: Dashboard placeholder for loss curves, parameter counts, and future routing metrics.
3. Walk through mechanics and shapes using: Perplexity = exp(validation cross-entropy).
4. Implement or pseudocode: count_parameters and estimate_active_parameters helper functions.
5. Verify with: Write the first baseline row in the experiment comparison table.
6. Bridge: The next chapter replaces the dense FFN with a small expert bank and a router.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch02/fig-baseline-diagnostics-and-comparison-slots.tex` - TikZ figure. Caption placeholder: Dashboard placeholder for loss curves, parameter counts, and future routing metrics. Label: `fig:ch02-baseline-diagnostics-and-comparison-slots`.
- `latex_book_skeleton/tables/ch02/tab-baseline-diagnostics-and-comparison-slots.tex` - Table. Caption placeholder: Metrics available now versus metrics added by MoE layers. Label: `tab:ch02-baseline-diagnostics-and-comparison-slots`.
- `latex_book_skeleton/listings/ch02/lst-baseline-diagnostics-and-comparison-slots.tex` - Python listing. Caption placeholder: count_parameters and estimate_active_parameters helper functions. Label: `lst:ch02-baseline-diagnostics-and-comparison-slots`.
- `latex_book_skeleton/equations/ch02/eq-baseline-diagnostics-and-comparison-slots.tex` - Equation artifact. Placeholder: Perplexity = exp(validation cross-entropy). Label: `eq:ch02-baseline-diagnostics-and-comparison-slots`.

Detailed section file: `section_plans/ch02/06-baseline-diagnostics-and-comparison-slots.md`
