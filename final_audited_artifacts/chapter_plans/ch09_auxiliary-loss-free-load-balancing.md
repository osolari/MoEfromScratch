# Chapter 9: Auxiliary-loss-free load balancing

**Part:** Part III - training routers and experts

**Role in the book:** Replace auxiliary balancing with a router-bias mechanism that affects selection but not combine weights.

## This chapter covers

- Why it is useful to separate load-balancing control from the language-model objective.
- How dynamic router bias changes expert selection without becoming a trainable parameter.
- How to compare auxiliary-loss and bias-balancing behavior with identical diagnostics.

## Implementation milestone

Implement router_bias state, biased top-k selection, unbiased gate computation, and no-gradient bias updates from observed load.

## Section-by-section plan

### 9.1 The limitation of auxiliary balancing

**Objective:** Explain why a separate balancing mechanism is attractive after readers have implemented auxiliary losses.

**Mini-example:** Show total_loss changes when aux_coef changes even with the same LM loss.

**Development flow:**

1. Open with the local problem: Explain why a separate balancing mechanism is attractive after readers have implemented auxiliary losses.
2. Introduce the schematic: Auxiliary loss path entering the optimization objective beside LM loss.
3. Walk through mechanics and shapes using: total_loss includes auxiliary term in the baseline approach.
4. Implement or pseudocode: Experiment config that toggles aux_loss on and off for the same model.
5. Verify with: Compare LM loss and load balance separately, not only total loss.
6. Bridge: Router bias moves balance control into the selection rule rather than the loss.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch09/fig-the-limitation-of-auxiliary-balancing.tex` - TikZ figure. Caption placeholder: Auxiliary loss path entering the optimization objective beside LM loss. Label: `fig:ch09-the-limitation-of-auxiliary-balancing`.
- `latex_book_skeleton/tables/ch09/tab-the-limitation-of-auxiliary-balancing.tex` - Table. Caption placeholder: Auxiliary balancing benefits and trade-offs. Label: `tab:ch09-the-limitation-of-auxiliary-balancing`.
- `latex_book_skeleton/listings/ch09/lst-the-limitation-of-auxiliary-balancing.tex` - Python listing. Caption placeholder: Experiment config that toggles aux_loss on and off for the same model. Label: `lst:ch09-the-limitation-of-auxiliary-balancing`.
- `latex_book_skeleton/equations/ch09/eq-the-limitation-of-auxiliary-balancing.tex` - Equation artifact. Placeholder: total_loss includes auxiliary term in the baseline approach. Label: `eq:ch09-the-limitation-of-auxiliary-balancing`.

Detailed section file: `section_plans/ch09/01-the-limitation-of-auxiliary-balancing.md`

### 9.2 Router bias as non-trainable state

**Objective:** Define router bias as a per-expert control signal updated outside backpropagation.

**Mini-example:** Use four experts with bias values that rise for underused experts and fall for overused experts.

**Development flow:**

1. Open with the local problem: Define router bias as a per-expert control signal updated outside backpropagation.
2. Introduce the schematic: Bias vector nudging the score table before top-k selection.
3. Walk through mechanics and shapes using: selection_score = score + router_bias.
4. Implement or pseudocode: Register router_bias as a buffer and exclude it from optimizer gradients.
5. Verify with: Assert router_bias.requires_grad is false and optimizer does not update it.
6. Bridge: The key implementation detail is that bias changes selection but not final gates.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch09/fig-router-bias-as-non-trainable-state.tex` - TikZ figure. Caption placeholder: Bias vector nudging the score table before top-k selection. Label: `fig:ch09-router-bias-as-non-trainable-state`.
- `latex_book_skeleton/tables/ch09/tab-router-bias-as-non-trainable-state.tex` - Table. Caption placeholder: Router bias properties: shape, initialization, update timing, gradient status, checkpoint behavior. Label: `tab:ch09-router-bias-as-non-trainable-state`.
- `latex_book_skeleton/listings/ch09/lst-router-bias-as-non-trainable-state.tex` - Python listing. Caption placeholder: Register router_bias as a buffer and exclude it from optimizer gradients. Label: `lst:ch09-router-bias-as-non-trainable-state`.
- `latex_book_skeleton/equations/ch09/eq-router-bias-as-non-trainable-state.tex` - Equation artifact. Placeholder: selection_score = score + router_bias. Label: `eq:ch09-router-bias-as-non-trainable-state`.

Detailed section file: `section_plans/ch09/02-router-bias-as-non-trainable-state.md`

### 9.3 Biased selection and unbiased combine

**Objective:** Implement the central invariant of the final reference model.

**Mini-example:** A token selects experts using score+bias, then gates are computed from the original selected scores.

**Development flow:**

1. Open with the local problem: Implement the central invariant of the final reference model.
2. Introduce the schematic: Two score streams: biased scores for top-k, unbiased scores for gate normalization.
3. Walk through mechanics and shapes using: idx = topk(score + b); gate = normalize(score[idx]).
4. Implement or pseudocode: Router forward pass returning topk_idx from biased scores and gates from unbiased selected scores.
5. Verify with: Unit test that changing bias can change expert IDs while gate values still come from raw scores.
6. Bridge: The bias vector needs an update rule based on observed expert load.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch09/fig-biased-selection-and-unbiased-combine.tex` - TikZ figure. Caption placeholder: Two score streams: biased scores for top-k, unbiased scores for gate normalization. Label: `fig:ch09-biased-selection-and-unbiased-combine`.
- `latex_book_skeleton/tables/ch09/tab-biased-selection-and-unbiased-combine.tex` - Table. Caption placeholder: Selection tensor versus combine tensor and where each is used. Label: `tab:ch09-biased-selection-and-unbiased-combine`.
- `latex_book_skeleton/listings/ch09/lst-biased-selection-and-unbiased-combine.tex` - Python listing. Caption placeholder: Router forward pass returning topk_idx from biased scores and gates from unbiased selected scores. Label: `lst:ch09-biased-selection-and-unbiased-combine`.
- `latex_book_skeleton/equations/ch09/eq-biased-selection-and-unbiased-combine.tex` - Equation artifact. Placeholder: idx = topk(score + b); gate = normalize(score[idx]). Label: `eq:ch09-biased-selection-and-unbiased-combine`.

Detailed section file: `section_plans/ch09/03-biased-selection-and-unbiased-combine.md`

### 9.4 Dynamic bias update from expert load

**Objective:** Add a simple no-gradient update that nudges underused experts up and overused experts down.

**Mini-example:** Compare observed loads [8,2,1,1] to target load 3 and update each bias.

**Development flow:**

1. Open with the local problem: Add a simple no-gradient update that nudges underused experts up and overused experts down.
2. Introduce the schematic: Feedback loop from observed expert histogram to router bias update.
3. Walk through mechanics and shapes using: b_i <- b_i + gamma if load_i < target, otherwise b_i <- b_i - gamma.
4. Implement or pseudocode: update_router_bias(load, target, gamma) implemented under torch.no_grad().
5. Verify with: Track bias values over training beside expert loads.
6. Bridge: Now we can compare auxiliary balancing and bias balancing using the same model and metrics.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch09/fig-dynamic-bias-update-from-expert-load.tex` - TikZ figure. Caption placeholder: Feedback loop from observed expert histogram to router bias update. Label: `fig:ch09-dynamic-bias-update-from-expert-load`.
- `latex_book_skeleton/tables/ch09/tab-dynamic-bias-update-from-expert-load.tex` - Table. Caption placeholder: Bias update hyperparameters: gamma, target load, update interval, clamp range. Label: `tab:ch09-dynamic-bias-update-from-expert-load`.
- `latex_book_skeleton/listings/ch09/lst-dynamic-bias-update-from-expert-load.tex` - Python listing. Caption placeholder: update_router_bias(load, target, gamma) implemented under torch.no_grad(). Label: `lst:ch09-dynamic-bias-update-from-expert-load`.
- `latex_book_skeleton/equations/ch09/eq-dynamic-bias-update-from-expert-load.tex` - Equation artifact. Placeholder: b_i <- b_i + gamma if load_i < target, otherwise b_i <- b_i - gamma. Label: `eq:ch09-dynamic-bias-update-from-expert-load`.

Detailed section file: `section_plans/ch09/04-dynamic-bias-update-from-expert-load.md`

### 9.5 Comparing balancing methods

**Objective:** Design a fair chapter experiment comparing no balance, auxiliary loss, and router-bias balancing.

**Mini-example:** Run three short smoke experiments with identical seeds and report the same diagnostics.

**Development flow:**

1. Open with the local problem: Design a fair chapter experiment comparing no balance, auxiliary loss, and router-bias balancing.
2. Introduce the schematic: Three-panel comparison of expert load histograms and validation loss curves.
3. Walk through mechanics and shapes using: Balance score based on max_load/mean_load or coefficient of variation.
4. Implement or pseudocode: run_balancing_ablation.py command presets.
5. Verify with: Produce a table with LM loss, aux loss if used, load balance score, entropy, and drop rate.
6. Bridge: The next chapter assembles the full MiniDeepSeekMoE model around this final layer.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch09/fig-comparing-balancing-methods.tex` - TikZ figure. Caption placeholder: Three-panel comparison of expert load histograms and validation loss curves. Label: `fig:ch09-comparing-balancing-methods`.
- `latex_book_skeleton/tables/ch09/tab-comparing-balancing-methods.tex` - Table. Caption placeholder: Experiment matrix with balancing method, objective terms, update rule, and expected diagnostics. Label: `tab:ch09-comparing-balancing-methods`.
- `latex_book_skeleton/listings/ch09/lst-comparing-balancing-methods.tex` - Python listing. Caption placeholder: run_balancing_ablation.py command presets. Label: `lst:ch09-comparing-balancing-methods`.
- `latex_book_skeleton/equations/ch09/eq-comparing-balancing-methods.tex` - Equation artifact. Placeholder: Balance score based on max_load/mean_load or coefficient of variation. Label: `eq:ch09-comparing-balancing-methods`.

Detailed section file: `section_plans/ch09/05-comparing-balancing-methods.md`

### 9.6 Chapter summary and handoff

**Objective:** Lock the final router behavior and document the invariants required by the complete model.

**Mini-example:** Trace one token through score, bias, selected experts, unbiased gates, expert outputs, and metrics.

**Development flow:**

1. Open with the local problem: Lock the final router behavior and document the invariants required by the complete model.
2. Introduce the schematic: Final router contract diagram with selection and combine paths separated.
3. Walk through mechanics and shapes using: Final routing formula for MiniDeepSeekMoE.
4. Implement or pseudocode: RouterBiasBalancer smoke test covering update and no-gradient behavior.
5. Verify with: Reader checkpoint: explain why bias should not be included in combine weights.
6. Bridge: We can now build the full model with this routing block as the FFN replacement.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch09/fig-chapter-summary-and-handoff.tex` - TikZ figure. Caption placeholder: Final router contract diagram with selection and combine paths separated. Label: `fig:ch09-chapter-summary-and-handoff`.
- `latex_book_skeleton/tables/ch09/tab-chapter-summary-and-handoff.tex` - Table. Caption placeholder: Final router invariants and tests. Label: `tab:ch09-chapter-summary-and-handoff`.
- `latex_book_skeleton/listings/ch09/lst-chapter-summary-and-handoff.tex` - Python listing. Caption placeholder: RouterBiasBalancer smoke test covering update and no-gradient behavior. Label: `lst:ch09-chapter-summary-and-handoff`.
- `latex_book_skeleton/equations/ch09/eq-chapter-summary-and-handoff.tex` - Equation artifact. Placeholder: Final routing formula for MiniDeepSeekMoE. Label: `eq:ch09-chapter-summary-and-handoff`.

Detailed section file: `section_plans/ch09/06-chapter-summary-and-handoff.md`
