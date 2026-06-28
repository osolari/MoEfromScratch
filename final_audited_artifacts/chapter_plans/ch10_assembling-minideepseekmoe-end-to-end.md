# Chapter 10: Assembling MiniDeepSeekMoE end to end

**Part:** Part IV - assembling and training the model

**Role in the book:** Integrate the final MoE layer into a complete decoder-only language model.

## This chapter covers

- How configuration objects control dense, top-k, shared expert, and balancing options.
- How the decoder block returns logits, losses, and routing metrics cleanly.
- How smoke tests protect the full model from hidden routing regressions.

## Implementation milestone

Produce the final model.py, config.py, train.py, sample.py, and tests for the MiniDeepSeekMoE implementation.

## Section-by-section plan

### 10.1 Configuration objects and model variants

**Objective:** Move from chapter-specific modules to a unified configuration-driven model.

**Mini-example:** Define DenseBaselineConfig, MiniDeepSeekMoESmokeConfig, and MiniDeepSeekMoE16x2Config.

**Development flow:**

1. Open with the local problem: Move from chapter-specific modules to a unified configuration-driven model.
2. Introduce the schematic: Configuration tree controlling attention, FFN/MoE, routing, balancing, and diagnostics.
3. Walk through mechanics and shapes using: Variant identity as a tuple of depth, width, expert count, K, and balancing method.
4. Implement or pseudocode: Dataclass or simple config object for MiniDeepSeekMoE.
5. Verify with: Print model summary and assert required fields exist.
6. Bridge: The decoder block can now instantiate dense or MoE FFN paths from config.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch10/fig-configuration-objects-and-model-variants.tex` - TikZ figure. Caption placeholder: Configuration tree controlling attention, FFN/MoE, routing, balancing, and diagnostics. Label: `fig:ch10-configuration-objects-and-model-variants`.
- `latex_book_skeleton/tables/ch10/tab-configuration-objects-and-model-variants.tex` - Table. Caption placeholder: Final configuration fields and default values. Label: `tab:ch10-configuration-objects-and-model-variants`.
- `latex_book_skeleton/listings/ch10/lst-configuration-objects-and-model-variants.tex` - Python listing. Caption placeholder: Dataclass or simple config object for MiniDeepSeekMoE. Label: `lst:ch10-configuration-objects-and-model-variants`.
- `latex_book_skeleton/equations/ch10/eq-configuration-objects-and-model-variants.tex` - Equation artifact. Placeholder: Variant identity as a tuple of depth, width, expert count, K, and balancing method. Label: `eq:ch10-configuration-objects-and-model-variants`.

Detailed section file: `section_plans/ch10/01-configuration-objects-and-model-variants.md`

### 10.2 Decoder block with dense prefix and MoE layers

**Objective:** Assemble layers so early dense computation can precede sparse MoE layers if configured.

**Mini-example:** Use one dense prefix layer followed by MoE blocks in the default config.

**Development flow:**

1. Open with the local problem: Assemble layers so early dense computation can precede sparse MoE layers if configured.
2. Introduce the schematic: Stack of decoder blocks showing dense prefix and repeated MoE layers.
3. Walk through mechanics and shapes using: block(x) = x + attention(norm(x)); x = x + ffn_or_moe(norm(x)).
4. Implement or pseudocode: DecoderBlock factory that chooses DenseFFN or MiniDeepSeekMoELayer.
5. Verify with: List layer types during model initialization.
6. Bridge: The model forward pass must carry routing metrics out of each MoE layer.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch10/fig-decoder-block-with-dense-prefix-and-moe-layers.tex` - TikZ figure. Caption placeholder: Stack of decoder blocks showing dense prefix and repeated MoE layers. Label: `fig:ch10-decoder-block-with-dense-prefix-and-moe-layers`.
- `latex_book_skeleton/tables/ch10/tab-decoder-block-with-dense-prefix-and-moe-layers.tex` - Table. Caption placeholder: Layer type by index for smoke, default, and larger teaching configs. Label: `tab:ch10-decoder-block-with-dense-prefix-and-moe-layers`.
- `latex_book_skeleton/listings/ch10/lst-decoder-block-with-dense-prefix-and-moe-layers.tex` - Python listing. Caption placeholder: DecoderBlock factory that chooses DenseFFN or MiniDeepSeekMoELayer. Label: `lst:ch10-decoder-block-with-dense-prefix-and-moe-layers`.
- `latex_book_skeleton/equations/ch10/eq-decoder-block-with-dense-prefix-and-moe-layers.tex` - Equation artifact. Placeholder: block(x) = x + attention(norm(x)); x = x + ffn_or_moe(norm(x)). Label: `eq:ch10-decoder-block-with-dense-prefix-and-moe-layers`.

Detailed section file: `section_plans/ch10/02-decoder-block-with-dense-prefix-and-moe-layers.md`

### 10.3 Forward pass outputs and loss dictionary

**Objective:** Return logits and structured losses/metrics without making training code guess where values live.

**Mini-example:** Forward pass returns logits, lm_loss, total_loss, router_metrics, and optional aux_loss.

**Development flow:**

1. Open with the local problem: Return logits and structured losses/metrics without making training code guess where values live.
2. Introduce the schematic: Forward output dictionary with model outputs and nested per-layer router metrics.
3. Walk through mechanics and shapes using: total_loss depends on selected balancing mode.
4. Implement or pseudocode: MiniDeepSeekMoE.forward implementation with metric aggregation.
5. Verify with: Unit test for output keys under dense, auxiliary, and bias modes.
6. Bridge: Training and sampling scripts can now be shared across variants.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch10/fig-forward-pass-outputs-and-loss-dictionary.tex` - TikZ figure. Caption placeholder: Forward output dictionary with model outputs and nested per-layer router metrics. Label: `fig:ch10-forward-pass-outputs-and-loss-dictionary`.
- `latex_book_skeleton/tables/ch10/tab-forward-pass-outputs-and-loss-dictionary.tex` - Table. Caption placeholder: Output dictionary keys, shapes, and when they are present. Label: `tab:ch10-forward-pass-outputs-and-loss-dictionary`.
- `latex_book_skeleton/listings/ch10/lst-forward-pass-outputs-and-loss-dictionary.tex` - Python listing. Caption placeholder: MiniDeepSeekMoE.forward implementation with metric aggregation. Label: `lst:ch10-forward-pass-outputs-and-loss-dictionary`.
- `latex_book_skeleton/equations/ch10/eq-forward-pass-outputs-and-loss-dictionary.tex` - Equation artifact. Placeholder: total_loss depends on selected balancing mode. Label: `eq:ch10-forward-pass-outputs-and-loss-dictionary`.

Detailed section file: `section_plans/ch10/03-forward-pass-outputs-and-loss-dictionary.md`

### 10.4 Training and sampling scripts

**Objective:** Create runnable scripts that match the source codebase style: minimal, readable, and chapter-scoped.

**Mini-example:** Run train.py with a smoke config and sample.py from the saved checkpoint.

**Development flow:**

1. Open with the local problem: Create runnable scripts that match the source codebase style: minimal, readable, and chapter-scoped.
2. Introduce the schematic: Script workflow from config to training to checkpoint to sample text.
3. Walk through mechanics and shapes using: Checkpoint state includes model, optimizer, config, and router bias buffers.
4. Implement or pseudocode: train.py main function with config loading, training loop, checkpointing, and sampling hook.
5. Verify with: Verify checkpoint reload produces logits of the same shape.
6. Bridge: A full model needs full-model smoke tests before experiments are trusted.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch10/fig-training-and-sampling-scripts.tex` - TikZ figure. Caption placeholder: Script workflow from config to training to checkpoint to sample text. Label: `fig:ch10-training-and-sampling-scripts`.
- `latex_book_skeleton/tables/ch10/tab-training-and-sampling-scripts.tex` - Table. Caption placeholder: Command-line arguments and their defaults. Label: `tab:ch10-training-and-sampling-scripts`.
- `latex_book_skeleton/listings/ch10/lst-training-and-sampling-scripts.tex` - Python listing. Caption placeholder: train.py main function with config loading, training loop, checkpointing, and sampling hook. Label: `lst:ch10-training-and-sampling-scripts`.
- `latex_book_skeleton/equations/ch10/eq-training-and-sampling-scripts.tex` - Equation artifact. Placeholder: Checkpoint state includes model, optimizer, config, and router bias buffers. Label: `eq:ch10-training-and-sampling-scripts`.

Detailed section file: `section_plans/ch10/04-training-and-sampling-scripts.md`

### 10.5 Full-model smoke tests

**Objective:** Create a test suite that catches shape, routing, balancing, and serialization failures.

**Mini-example:** Run the smoke config on CPU for two forward/backward passes.

**Development flow:**

1. Open with the local problem: Create a test suite that catches shape, routing, balancing, and serialization failures.
2. Introduce the schematic: Smoke-test pipeline with pass/fail checkpoints after each stage.
3. Walk through mechanics and shapes using: No NaNs and finite loss invariant.
4. Implement or pseudocode: tests/test_minideepseekmoe_smoke.py with forward, backward, bias-update, and save-load tests.
5. Verify with: CI-style console summary for all smoke tests.
6. Bridge: With a complete tested implementation, the next chapter runs experiments and interprets diagnostics.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch10/fig-full-model-smoke-tests.tex` - TikZ figure. Caption placeholder: Smoke-test pipeline with pass/fail checkpoints after each stage. Label: `fig:ch10-full-model-smoke-tests`.
- `latex_book_skeleton/tables/ch10/tab-full-model-smoke-tests.tex` - Table. Caption placeholder: Test names, purpose, and expected runtime tier. Label: `tab:ch10-full-model-smoke-tests`.
- `latex_book_skeleton/listings/ch10/lst-full-model-smoke-tests.tex` - Python listing. Caption placeholder: tests/test_minideepseekmoe_smoke.py with forward, backward, bias-update, and save-load tests. Label: `lst:ch10-full-model-smoke-tests`.
- `latex_book_skeleton/equations/ch10/eq-full-model-smoke-tests.tex` - Equation artifact. Placeholder: No NaNs and finite loss invariant. Label: `eq:ch10-full-model-smoke-tests`.

Detailed section file: `section_plans/ch10/05-full-model-smoke-tests.md`

### 10.6 Chapter summary and handoff

**Objective:** Summarize the complete implementation and separate code correctness from model quality.

**Mini-example:** Compare dense baseline and MiniDeepSeekMoE smoke configs by parameter count and active parameters.

**Development flow:**

1. Open with the local problem: Summarize the complete implementation and separate code correctness from model quality.
2. Introduce the schematic: End-to-end model architecture diagram from tokens to logits.
3. Walk through mechanics and shapes using: Active expert parameters per token for the final config.
4. Implement or pseudocode: README quickstart commands for train and sample.
5. Verify with: Reader checkpoint: run the smoke model and inspect router metrics.
6. Bridge: The next chapter turns the implementation into a controlled experiment framework.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch10/fig-chapter-summary-and-handoff.tex` - TikZ figure. Caption placeholder: End-to-end model architecture diagram from tokens to logits. Label: `fig:ch10-chapter-summary-and-handoff`.
- `latex_book_skeleton/tables/ch10/tab-chapter-summary-and-handoff.tex` - Table. Caption placeholder: Final implementation files and their responsibilities. Label: `tab:ch10-chapter-summary-and-handoff`.
- `latex_book_skeleton/listings/ch10/lst-chapter-summary-and-handoff.tex` - Python listing. Caption placeholder: README quickstart commands for train and sample. Label: `lst:ch10-chapter-summary-and-handoff`.
- `latex_book_skeleton/equations/ch10/eq-chapter-summary-and-handoff.tex` - Equation artifact. Placeholder: Active expert parameters per token for the final config. Label: `eq:ch10-chapter-summary-and-handoff`.

Detailed section file: `section_plans/ch10/06-chapter-summary-and-handoff.md`
