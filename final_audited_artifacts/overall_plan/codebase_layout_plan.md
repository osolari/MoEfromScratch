# Codebase layout plan

The codebase should preserve the attached repository's chapter-first style while adding a reusable shared package for later chapters.

```text
MoE-Models-From-Scratch-main/
├── README.md
├── pyproject.toml                 # optional; requirements.txt per late chapter remains acceptable
├── common/
│   ├── __init__.py
│   ├── config.py                  # shared dataclasses/config dictionaries
│   ├── data.py                    # tokenization and batch helpers
│   ├── dense_model.py             # baseline Transformer components
│   ├── experts.py                 # ExpertMLP, expert banks, shared experts
│   ├── routing.py                 # top-k, gates, router bias, load metrics
│   ├── dispatch.py                # naive and vectorized dispatch utilities
│   ├── diagnostics.py             # load histograms, entropy, active params
│   └── plotting.py                # reusable plot helpers
├── ch01/README.md
├── ch02/01_main-chapter-code/Chapter_2_dense_baseline.ipynb
├── ch03/01_main-chapter-code/Chapter_3_first_moe_layer.ipynb
├── ch04/01_main-chapter-code/Chapter_4_top1_routing.ipynb
├── ch05/01_main-chapter-code/Chapter_5_top2_routing.ipynb
├── ch06/01_main-chapter-code/Chapter_6_vectorized_dispatch.ipynb
├── ch07/01_main-chapter-code/Chapter_7_load_balancing.ipynb
├── ch08/01_main-chapter-code/Chapter_8_shared_fine_grained_experts.ipynb
├── ch09/01_main-chapter-code/Chapter_9_aux_loss_free_balancing.ipynb
├── ch10/01_main-chapter-code/
│   ├── requirements.txt
│   ├── config.py
│   ├── model.py
│   ├── train.py
│   ├── sample.py
│   └── tests/test_smoke.py
├── ch11/01_main-chapter-code/
│   ├── prepare.py
│   ├── run_ablation_matrix.py
│   ├── plot_experiment_dashboard.py
│   ├── trace_prompt_routing.py
│   └── generate_experiment_report.py
└── ch12/01_main-chapter-code/
    ├── estimate_moe_compute.py
    ├── profile_inference_routes.py
    └── conceptual_distributed_dispatch.py
```

## Code style rules

- Earlier chapters can use notebooks for visual step-by-step development.
- Later chapters should provide scripts because training, sampling, and experiments need repeatability.
- Every chapter must be runnable in a smoke-test configuration before optional larger experiments are attempted.
- The final `model.py` should not depend on notebook-only code.
- Diagnostics should be implemented as reusable functions, not hidden inside plotting cells.
