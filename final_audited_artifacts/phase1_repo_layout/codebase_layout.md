# Codebase layout and setup extraction

## Repository intent

The repository is organized as chapter-by-chapter companion code for the attached DeepSeek book. It favors readable teaching implementations over a package-style library. There is no `pyproject.toml`, no top-level requirements file, and no installable package; code is meant to be run from each chapter folder.

## Top-level structure

```text
DeepSeek-From-Scratch-main/
├── README.md
├── ch01/README.md
├── ch02/01_main-chapter-code/Chapter_2.ipynb
├── ch03/01_main-chapter-code/Chapter_3.ipynb
├── ch03/02-bonus-code/MHA_vs_MQA_vs_GQA_vs_MLA..ipynb
├── ch04/01_main-chapter-code/Chapter_4.ipynb
├── ch04/02-bonus-code/deepseek_moe_comparison.ipynb
├── ch05/01_main-chapter-code/Chapter_5.ipynb
├── ch06/01_main-chapter-code/{requirements.txt,prepare.py,model.py,train.py,sample.py}
├── ch07/01_main-chapter-code/{requirements.txt,README.md,grpo_rlvr_minimal.py}
└── ch08/01_main-chapter-code/Chapter_8.ipynb
```

## Chapter code pattern

- Chapters 2-5 and 8 use Jupyter notebooks for main chapter code.
- Chapter 6 uses standalone scripts to form a complete model/data/train/sample pipeline.
- Chapter 7 uses one compact standalone Python file for minimal GRPO + RLVR mechanics.
- Bonus notebooks live beside the main code rather than inside a shared utilities package.

## Dependencies observed

### Chapter 6 runnable pipeline

```text
torch
numpy
datasets
tiktoken
tqdm
```

### Chapter 7 runnable demo

```text
torch
```

### Notebook-only dependencies observed

The notebooks additionally use packages such as `transformers`, `matplotlib`, `pandas`, `seaborn`, `torchvision`, and `IPython.display` depending on chapter. A future MoE book codebase should either provide a top-level `environment.yml` / `requirements.txt` or keep the chapter-local style and make each chapter self-contained.

## Validation performed

- All `.py` files in `ch06` and `ch07` parsed successfully with `python -m compileall`.
- All notebooks parsed as valid JSON.

## Setup style to reuse for the MoE book

Use this shape for the new repository:

```text
moe-from-scratch/
├── README.md
├── environment.yml or requirements.txt
├── ch01/README.md
├── ch01/01_main-chapter-code/Chapter_1.ipynb
├── ch02/README.md
├── ch02/01_main-chapter-code/Chapter_2.ipynb
├── ...
├── chNN/01_main-chapter-code/{prepare.py,model.py,train.py,sample.py}
└── shared/                 # optional, only if repeated code becomes distracting
```

Recommendation: keep notebooks for conceptual chapters and switch to scripts once the book reaches a complete trainable MiniMoE model.
