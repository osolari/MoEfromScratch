# Chapter 7: Router training and load-balancing losses

**Part:** Part III - training routers and experts

**Role in the book:** Teach the router to avoid expert collapse before moving to auxiliary-loss-free balancing.

## This chapter covers

- Why next-token loss alone may not balance expert use.
- How auxiliary load-balancing losses and router regularizers are implemented.
- How routing diagnostics become part of the training loop.

## Implementation milestone

Implement auxiliary load-balancing loss, optional router z-loss, entropy diagnostics, and trainer integration.

## Section-by-section plan

### 7.1 Expert imbalance as a training problem

**Objective:** Show that a technically correct router can still collapse onto a small number of experts.

**Mini-example:** Construct a score table where one expert receives most top-k selections.

**Development flow:**

1. Open with the local problem: Show that a technically correct router can still collapse onto a small number of experts.
2. Introduce the schematic: Collapsed routing histogram compared with balanced routing histogram.
3. Walk through mechanics and shapes using: Target average load per expert is N*K/E routes.
4. Implement or pseudocode: Synthetic imbalance generator for router-score diagnostics.
5. Verify with: Report max_load/mean_load and number of empty experts.
6. Bridge: An auxiliary loss can reward agreement between probability mass and actual expert load.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch07/fig-expert-imbalance-as-a-training-problem.tex` - TikZ figure. Caption placeholder: Collapsed routing histogram compared with balanced routing histogram. Label: `fig:ch07-expert-imbalance-as-a-training-problem`.
- `latex_book_skeleton/tables/ch07/tab-expert-imbalance-as-a-training-problem.tex` - Table. Caption placeholder: Symptoms of imbalance and the training behavior they affect. Label: `tab:ch07-expert-imbalance-as-a-training-problem`.
- `latex_book_skeleton/listings/ch07/lst-expert-imbalance-as-a-training-problem.tex` - Python listing. Caption placeholder: Synthetic imbalance generator for router-score diagnostics. Label: `lst:ch07-expert-imbalance-as-a-training-problem`.
- `latex_book_skeleton/equations/ch07/eq-expert-imbalance-as-a-training-problem.tex` - Equation artifact. Placeholder: Target average load per expert is N*K/E routes. Label: `eq:ch07-expert-imbalance-as-a-training-problem`.

Detailed section file: `section_plans/ch07/01-expert-imbalance-as-a-training-problem.md`

### 7.2 Auxiliary load-balancing loss

**Objective:** Implement the classic balancing baseline as a transparent, measurable loss term.

**Mini-example:** Compute expert load fractions and probability fractions for E=4 experts.

**Development flow:**

1. Open with the local problem: Implement the classic balancing baseline as a transparent, measurable loss term.
2. Introduce the schematic: Two bars per expert: selected load and router probability mass.
3. Walk through mechanics and shapes using: Auxiliary loss proportional to E * sum_i load_i * prob_i.
4. Implement or pseudocode: load_balancing_loss function returning scalar aux_loss and metrics.
5. Verify with: Check loss is lower for balanced synthetic routing than collapsed routing.
6. Bridge: Auxiliary loss enters the total training objective with a coefficient.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch07/fig-auxiliary-load-balancing-loss.tex` - TikZ figure. Caption placeholder: Two bars per expert: selected load and router probability mass. Label: `fig:ch07-auxiliary-load-balancing-loss`.
- `latex_book_skeleton/tables/ch07/tab-auxiliary-load-balancing-loss.tex` - Table. Caption placeholder: Inputs and outputs of the auxiliary loss function. Label: `tab:ch07-auxiliary-load-balancing-loss`.
- `latex_book_skeleton/listings/ch07/lst-auxiliary-load-balancing-loss.tex` - Python listing. Caption placeholder: load_balancing_loss function returning scalar aux_loss and metrics. Label: `lst:ch07-auxiliary-load-balancing-loss`.
- `latex_book_skeleton/equations/ch07/eq-auxiliary-load-balancing-loss.tex` - Equation artifact. Placeholder: Auxiliary loss proportional to E * sum_i load_i * prob_i. Label: `eq:ch07-auxiliary-load-balancing-loss`.

Detailed section file: `section_plans/ch07/02-auxiliary-load-balancing-loss.md`

### 7.3 Integrating auxiliary loss into training

**Objective:** Add routing losses to the model output dictionary without hiding the main language-model loss.

**Mini-example:** Return lm_loss, aux_loss, total_loss, and router_metrics from one forward pass.

**Development flow:**

1. Open with the local problem: Add routing losses to the model output dictionary without hiding the main language-model loss.
2. Introduce the schematic: Loss composition diagram from logits and router statistics to total loss.
3. Walk through mechanics and shapes using: total_loss = lm_loss + lambda_aux * aux_loss.
4. Implement or pseudocode: Training step that combines lm_loss + aux_coef * aux_loss.
5. Verify with: Log individual losses separately so balancing cannot hide LM degradation.
6. Bridge: Load balancing is one router signal; score scale can also create instability.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch07/fig-integrating-auxiliary-loss-into-training.tex` - TikZ figure. Caption placeholder: Loss composition diagram from logits and router statistics to total loss. Label: `fig:ch07-integrating-auxiliary-loss-into-training`.
- `latex_book_skeleton/tables/ch07/tab-integrating-auxiliary-loss-into-training.tex` - Table. Caption placeholder: Loss terms, coefficients, default values, and logging names. Label: `tab:ch07-integrating-auxiliary-loss-into-training`.
- `latex_book_skeleton/listings/ch07/lst-integrating-auxiliary-loss-into-training.tex` - Python listing. Caption placeholder: Training step that combines lm_loss + aux_coef * aux_loss. Label: `lst:ch07-integrating-auxiliary-loss-into-training`.
- `latex_book_skeleton/equations/ch07/eq-integrating-auxiliary-loss-into-training.tex` - Equation artifact. Placeholder: total_loss = lm_loss + lambda_aux * aux_loss. Label: `eq:ch07-integrating-auxiliary-loss-into-training`.

Detailed section file: `section_plans/ch07/03-integrating-auxiliary-loss-into-training.md`

### 7.4 Router score scale and z-loss

**Objective:** Introduce a simple regularizer for overly large router logits or scores.

**Mini-example:** Compare a modest logit row with a very large logit row that creates near-hard routing.

**Development flow:**

1. Open with the local problem: Introduce a simple regularizer for overly large router logits or scores.
2. Introduce the schematic: Router logit scale affects probability sharpness before top-k selection.
3. Walk through mechanics and shapes using: z_loss based on squared logsumexp of router logits.
4. Implement or pseudocode: router_z_loss function and optional coefficient in the training config.
5. Verify with: Track router score max, entropy, and z-loss over training.
6. Bridge: The regularizers become useful only if the diagnostics are visible during training.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch07/fig-router-score-scale-and-z-loss.tex` - TikZ figure. Caption placeholder: Router logit scale affects probability sharpness before top-k selection. Label: `fig:ch07-router-score-scale-and-z-loss`.
- `latex_book_skeleton/tables/ch07/tab-router-score-scale-and-z-loss.tex` - Table. Caption placeholder: Router regularization options: z-loss, entropy, noise, and clipping. Label: `tab:ch07-router-score-scale-and-z-loss`.
- `latex_book_skeleton/listings/ch07/lst-router-score-scale-and-z-loss.tex` - Python listing. Caption placeholder: router_z_loss function and optional coefficient in the training config. Label: `lst:ch07-router-score-scale-and-z-loss`.
- `latex_book_skeleton/equations/ch07/eq-router-score-scale-and-z-loss.tex` - Equation artifact. Placeholder: z_loss based on squared logsumexp of router logits. Label: `eq:ch07-router-score-scale-and-z-loss`.

Detailed section file: `section_plans/ch07/04-router-score-scale-and-z-loss.md`

### 7.5 Routing dashboards and training logs

**Objective:** Create the standard diagnostic views used for every later MoE experiment.

**Mini-example:** Log one training batch with load histogram, gate entropy, drop count, and loss terms.

**Development flow:**

1. Open with the local problem: Create the standard diagnostic views used for every later MoE experiment.
2. Introduce the schematic: Dashboard layout with loss curve, expert load histogram, gate entropy, and drop rate.
3. Walk through mechanics and shapes using: Routing entropy over normalized selected gates.
4. Implement or pseudocode: collect_router_metrics and plot_router_dashboard helpers.
5. Verify with: Generate a dashboard PDF or image after a short smoke run.
6. Bridge: The next chapter changes the expert architecture itself by adding shared and fine-grained routed experts.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch07/fig-routing-dashboards-and-training-logs.tex` - TikZ figure. Caption placeholder: Dashboard layout with loss curve, expert load histogram, gate entropy, and drop rate. Label: `fig:ch07-routing-dashboards-and-training-logs`.
- `latex_book_skeleton/tables/ch07/tab-routing-dashboards-and-training-logs.tex` - Table. Caption placeholder: Metric names, tensor source, frequency, and expected range. Label: `tab:ch07-routing-dashboards-and-training-logs`.
- `latex_book_skeleton/listings/ch07/lst-routing-dashboards-and-training-logs.tex` - Python listing. Caption placeholder: collect_router_metrics and plot_router_dashboard helpers. Label: `lst:ch07-routing-dashboards-and-training-logs`.
- `latex_book_skeleton/equations/ch07/eq-routing-dashboards-and-training-logs.tex` - Equation artifact. Placeholder: Routing entropy over normalized selected gates. Label: `eq:ch07-routing-dashboards-and-training-logs`.

Detailed section file: `section_plans/ch07/05-routing-dashboards-and-training-logs.md`

### 7.6 Chapter summary and handoff

**Objective:** Frame auxiliary balancing as the baseline that auxiliary-loss-free balancing will later improve on.

**Mini-example:** Compare training metrics with aux_coef=0 and aux_coef>0 in a smoke run.

**Development flow:**

1. Open with the local problem: Frame auxiliary balancing as the baseline that auxiliary-loss-free balancing will later improve on.
2. Introduce the schematic: Before-and-after load histograms for auxiliary balancing.
3. Walk through mechanics and shapes using: Model objective includes both LM and routing terms in this chapter.
4. Implement or pseudocode: Config presets for no-balancing and auxiliary-balancing runs.
5. Verify with: Reader checkpoint: explain why aux_loss must be logged separately from LM loss.
6. Bridge: MiniDeepSeekMoE keeps the routing lessons but changes expert structure before changing the balancing method.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch07/fig-chapter-summary-and-handoff.tex` - TikZ figure. Caption placeholder: Before-and-after load histograms for auxiliary balancing. Label: `fig:ch07-chapter-summary-and-handoff`.
- `latex_book_skeleton/tables/ch07/tab-chapter-summary-and-handoff.tex` - Table. Caption placeholder: What auxiliary loss fixes and what trade-offs remain. Label: `tab:ch07-chapter-summary-and-handoff`.
- `latex_book_skeleton/listings/ch07/lst-chapter-summary-and-handoff.tex` - Python listing. Caption placeholder: Config presets for no-balancing and auxiliary-balancing runs. Label: `lst:ch07-chapter-summary-and-handoff`.
- `latex_book_skeleton/equations/ch07/eq-chapter-summary-and-handoff.tex` - Equation artifact. Placeholder: Model objective includes both LM and routing terms in this chapter. Label: `eq:ch07-chapter-summary-and-handoff`.

Detailed section file: `section_plans/ch07/06-chapter-summary-and-handoff.md`
