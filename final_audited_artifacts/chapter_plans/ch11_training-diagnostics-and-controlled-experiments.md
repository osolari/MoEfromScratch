# Chapter 11: Training, diagnostics, and controlled experiments

**Part:** Part IV - assembling and training the model

**Role in the book:** Use the model to answer concrete questions about routing, balance, and sparse capacity.

## This chapter covers

- How to run small, reproducible experiments without overclaiming performance.
- How to interpret routing diagnostics alongside language-model loss.
- How ablations reveal the contribution of top-k, shared experts, and balancing methods.

## Implementation milestone

Build experiment scripts, diagnostic plot generation, and ablation tables for dense versus MoE variants.

## Section-by-section plan

### 11.1 Experiment design for a from-scratch book

**Objective:** Set realistic expectations for small-data experiments and define what can and cannot be concluded.

**Mini-example:** Use three smoke-scale runs to compare mechanics, not state-of-the-art quality.

**Development flow:**

1. Open with the local problem: Set realistic expectations for small-data experiments and define what can and cannot be concluded.
2. Introduce the schematic: Experiment funnel from smoke tests to short training runs to optional longer ablations.
3. Walk through mechanics and shapes using: Report mean and range across seeds when multiple seeds are used.
4. Implement or pseudocode: Experiment manifest YAML with seeds, configs, and output directories.
5. Verify with: Check that every experiment saves config, seed, logs, and git/code snapshot note.
6. Bridge: The data pipeline needs a repeatable preparation script.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch11/fig-experiment-design-for-a-from-scratch-book.tex` - TikZ figure. Caption placeholder: Experiment funnel from smoke tests to short training runs to optional longer ablations. Label: `fig:ch11-experiment-design-for-a-from-scratch-book`.
- `latex_book_skeleton/tables/ch11/tab-experiment-design-for-a-from-scratch-book.tex` - Table. Caption placeholder: Claim types allowed by each experiment scale. Label: `tab:ch11-experiment-design-for-a-from-scratch-book`.
- `latex_book_skeleton/listings/ch11/lst-experiment-design-for-a-from-scratch-book.tex` - Python listing. Caption placeholder: Experiment manifest YAML with seeds, configs, and output directories. Label: `lst:ch11-experiment-design-for-a-from-scratch-book`.
- `latex_book_skeleton/equations/ch11/eq-experiment-design-for-a-from-scratch-book.tex` - Equation artifact. Placeholder: Report mean and range across seeds when multiple seeds are used. Label: `eq:ch11-experiment-design-for-a-from-scratch-book`.

Detailed section file: `section_plans/ch11/01-experiment-design-for-a-from-scratch-book.md`

### 11.2 Dataset preparation and reproducibility

**Objective:** Make dataset setup deterministic and lightweight enough for readers to rerun.

**Mini-example:** Prepare a small corpus split into train and validation binary or tensor files.

**Development flow:**

1. Open with the local problem: Make dataset setup deterministic and lightweight enough for readers to rerun.
2. Introduce the schematic: Raw text to tokenized train/validation artifacts.
3. Walk through mechanics and shapes using: Train/validation split ratio and token count definitions.
4. Implement or pseudocode: prepare.py script with deterministic split and saved metadata.
5. Verify with: Print token counts, split sizes, and a decoded sample from each split.
6. Bridge: Training logs must include both language and routing metrics.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch11/fig-dataset-preparation-and-reproducibility.tex` - TikZ figure. Caption placeholder: Raw text to tokenized train/validation artifacts. Label: `fig:ch11-dataset-preparation-and-reproducibility`.
- `latex_book_skeleton/tables/ch11/tab-dataset-preparation-and-reproducibility.tex` - Table. Caption placeholder: Dataset artifacts, paths, and regeneration commands. Label: `tab:ch11-dataset-preparation-and-reproducibility`.
- `latex_book_skeleton/listings/ch11/lst-dataset-preparation-and-reproducibility.tex` - Python listing. Caption placeholder: prepare.py script with deterministic split and saved metadata. Label: `lst:ch11-dataset-preparation-and-reproducibility`.
- `latex_book_skeleton/equations/ch11/eq-dataset-preparation-and-reproducibility.tex` - Equation artifact. Placeholder: Train/validation split ratio and token count definitions. Label: `eq:ch11-dataset-preparation-and-reproducibility`.

Detailed section file: `section_plans/ch11/02-dataset-preparation-and-reproducibility.md`

### 11.3 Loss curves and routing dashboards

**Objective:** Create consistent plots that make model behavior inspectable after every run.

**Mini-example:** Plot validation loss, load balance score, entropy, and drop rate from one JSONL log.

**Development flow:**

1. Open with the local problem: Create consistent plots that make model behavior inspectable after every run.
2. Introduce the schematic: Standard diagnostic dashboard layout for a chapter experiment.
3. Walk through mechanics and shapes using: Load-balance score based on coefficient of variation across expert loads.
4. Implement or pseudocode: plot_experiment_dashboard.py reading logs and saving PDF figures.
5. Verify with: Save dashboard figures through LaTeX wrappers, never raw includegraphics in prose.
6. Bridge: With dashboards ready, ablation experiments can compare design choices.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch11/fig-loss-curves-and-routing-dashboards.tex` - TikZ figure. Caption placeholder: Standard diagnostic dashboard layout for a chapter experiment. Label: `fig:ch11-loss-curves-and-routing-dashboards`.
- `latex_book_skeleton/tables/ch11/tab-loss-curves-and-routing-dashboards.tex` - Table. Caption placeholder: Plot names, source metrics, and interpretation cautions. Label: `tab:ch11-loss-curves-and-routing-dashboards`.
- `latex_book_skeleton/listings/ch11/lst-loss-curves-and-routing-dashboards.tex` - Python listing. Caption placeholder: plot_experiment_dashboard.py reading logs and saving PDF figures. Label: `lst:ch11-loss-curves-and-routing-dashboards`.
- `latex_book_skeleton/equations/ch11/eq-loss-curves-and-routing-dashboards.tex` - Equation artifact. Placeholder: Load-balance score based on coefficient of variation across expert loads. Label: `eq:ch11-loss-curves-and-routing-dashboards`.

Detailed section file: `section_plans/ch11/03-loss-curves-and-routing-dashboards.md`

### 11.4 Ablation matrix: dense, top-1, top-2, shared, and bias-balanced

**Objective:** Plan the central comparison table for the book without pretending small runs settle model quality.

**Mini-example:** Run five variants for the same token budget and record comparable metrics.

**Development flow:**

1. Open with the local problem: Plan the central comparison table for the book without pretending small runs settle model quality.
2. Introduce the schematic: Ablation matrix with one row per model variant and columns for routing features.
3. Walk through mechanics and shapes using: Active parameter ratio for each sparse variant.
4. Implement or pseudocode: run_ablation_matrix.py that launches or documents variant commands.
5. Verify with: Flag any run with unstable loss, high drop rate, or extreme expert collapse.
6. Bridge: Expert behavior should be interpreted with both numbers and examples.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch11/fig-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.tex` - TikZ figure. Caption placeholder: Ablation matrix with one row per model variant and columns for routing features. Label: `fig:ch11-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced`.
- `latex_book_skeleton/tables/ch11/tab-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.tex` - Table. Caption placeholder: Dense baseline versus MoE variants: parameters, active parameters, loss, load, entropy, drop rate. Label: `tab:ch11-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced`.
- `latex_book_skeleton/listings/ch11/lst-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.tex` - Python listing. Caption placeholder: run_ablation_matrix.py that launches or documents variant commands. Label: `lst:ch11-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced`.
- `latex_book_skeleton/equations/ch11/eq-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.tex` - Equation artifact. Placeholder: Active parameter ratio for each sparse variant. Label: `eq:ch11-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced`.

Detailed section file: `section_plans/ch11/04-ablation-matrix-dense-top-1-top-2-shared-and-bias-balanced.md`

### 11.5 Interpreting expert behavior carefully

**Objective:** Teach readers to inspect expert usage without overclaiming that tiny experts learned semantic roles.

**Mini-example:** Look at expert IDs selected for a short prompt and compare across positions or token types.

**Development flow:**

1. Open with the local problem: Teach readers to inspect expert usage without overclaiming that tiny experts learned semantic roles.
2. Introduce the schematic: Token-by-token routing trace over a prompt.
3. Walk through mechanics and shapes using: Conditional expert frequency for a chosen token group.
4. Implement or pseudocode: trace_prompt_routing.py that prints token, top-k experts, and gates.
5. Verify with: Generate a routing trace table and a usage heatmap.
6. Bridge: The final chapter steps back from experiments to discuss inference and scaling limits.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch11/fig-interpreting-expert-behavior-carefully.tex` - TikZ figure. Caption placeholder: Token-by-token routing trace over a prompt. Label: `fig:ch11-interpreting-expert-behavior-carefully`.
- `latex_book_skeleton/tables/ch11/tab-interpreting-expert-behavior-carefully.tex` - Table. Caption placeholder: Interpretation checklist: evidence, limitation, alternative explanation, next test. Label: `tab:ch11-interpreting-expert-behavior-carefully`.
- `latex_book_skeleton/listings/ch11/lst-interpreting-expert-behavior-carefully.tex` - Python listing. Caption placeholder: trace_prompt_routing.py that prints token, top-k experts, and gates. Label: `lst:ch11-interpreting-expert-behavior-carefully`.
- `latex_book_skeleton/equations/ch11/eq-interpreting-expert-behavior-carefully.tex` - Equation artifact. Placeholder: Conditional expert frequency for a chosen token group. Label: `eq:ch11-interpreting-expert-behavior-carefully`.

Detailed section file: `section_plans/ch11/05-interpreting-expert-behavior-carefully.md`

### 11.6 Chapter summary and handoff

**Objective:** Close the experimental part by identifying what the book has demonstrated mechanically.

**Mini-example:** Summarize one dense run and one final MoE run in the same report card.

**Development flow:**

1. Open with the local problem: Close the experimental part by identifying what the book has demonstrated mechanically.
2. Introduce the schematic: Experiment report card combining loss, active parameters, expert balance, and routing trace.
3. Walk through mechanics and shapes using: No new equation; reuse active-parameter and load-balance metrics.
4. Implement or pseudocode: generate_experiment_report.py producing Markdown and LaTeX table outputs.
5. Verify with: Reader checkpoint: identify whether a routing issue is code, loss, capacity, or data related.
6. Bridge: The last chapter explains how these same mechanisms change at inference and production scale.

**Planned artifacts:**

- `latex_book_skeleton/figures/ch11/fig-chapter-summary-and-handoff.tex` - TikZ figure. Caption placeholder: Experiment report card combining loss, active parameters, expert balance, and routing trace. Label: `fig:ch11-chapter-summary-and-handoff`.
- `latex_book_skeleton/tables/ch11/tab-chapter-summary-and-handoff.tex` - Table. Caption placeholder: What each ablation teaches and which chapter implemented the mechanism. Label: `tab:ch11-chapter-summary-and-handoff`.
- `latex_book_skeleton/listings/ch11/lst-chapter-summary-and-handoff.tex` - Python listing. Caption placeholder: generate_experiment_report.py producing Markdown and LaTeX table outputs. Label: `lst:ch11-chapter-summary-and-handoff`.
- `latex_book_skeleton/equations/ch11/eq-chapter-summary-and-handoff.tex` - Equation artifact. Placeholder: No new equation; reuse active-parameter and load-balance metrics. Label: `eq:ch11-chapter-summary-and-handoff`.

Detailed section file: `section_plans/ch11/06-chapter-summary-and-handoff.md`
