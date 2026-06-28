# Phase 1 report: template and codebase extraction

## Scope completed

Phase 1 inspected the two attached files:

- `Build_a_DeepSeek_Model_(From_Scratch)_v3_MEAP.epub`
- `DeepSeek-From-Scratch-main.zip`

The goal was to extract the production template, repository layout, and setup conventions that should guide the future **MoE Models from Scratch** book.

## Key finding: no original LaTeX source was attached

The EPUB is a compiled EPUB package. It contains XHTML chapters, CSS, images, a font file, and EPUB metadata, but no original LaTeX source files. The code ZIP likewise contains companion code, not book source.

Files searched for and not found: `.tex`, `.sty`, `.cls`, `.bib`, `.latex`, and source `Makefile`.

Therefore, the included `latex_template/` directory is a **derived LaTeX analogue** of the attached EPUB style and structure, not a recovered original LaTeX template.

## EPUB production structure extracted

```text
OEBPS/
├── Text/
│   ├── titlepage.xhtml
│   ├── copyright.html
│   ├── welcome.html
│   ├── brief-table-of-contents.html
│   └── chapter-1.html ... chapter-8.html
├── Styles/stylesheet.css
├── Images/*.png, *.jpg
├── Misc/JetBrains.woff2
├── content.opf
└── toc.ncx
```

The book is structured as XHTML with repeated containers for readable text, figures, code/listings, callouts, and tables.

## Derived LaTeX template created

The folder `latex_template/` contains a modular book template with these conventions:

```text
latex_template/
├── main.tex
├── Makefile
├── README.md
├── styles/
│   ├── preamble.tex
│   ├── colors.tex
│   └── macros.tex
├── frontmatter/
│   ├── titlepage.tex
│   └── closing-note.tex
├── chapters/01-template/
│   ├── chapter.tex
│   └── sections/*.tex
├── figures/
│   ├── figure-tikz-placeholder.tex
│   └── figure-pdf-placeholder.tex
├── tables/table-placeholder.tex
└── listings/listing-placeholder.tex
```

Every content artifact is loaded via `\input`. Figures, tables, and listings are each wrapped in their own `.tex` file so captions and labels are local to the artifact. TikZ is used for authored schematics. External PDF figures are intended to be wrapped in a `.tex` file containing `\includegraphics`, `\caption`, and `\label`.

## Style and theme extracted

The EPUB CSS gave the following core visual rules:

| Element | Extracted style | LaTeX analogue |
|---|---|---|
| Headings | dark navy/blue | `BookNavy`, `BookDeepBlue` |
| Callouts | light gray panels | `definitionbox`, `notebox` |
| Code | light gray background | `lstlisting` style `bookpython` |
| Listing titles | dark blue label area | `BookListingHeader` |
| Figures | centered schematic with explanatory caption | `figure` wrappers + TikZ/PDF |
| Tables | simple bordered EPUB tables | print-style `booktabs` tables |

The extracted color map is included in `latex_template/styles/colors.tex` and documented in `source_extracts/epub_production_extraction.md`.

## Book layout pattern extracted

The attached book generally develops each technical idea in this order:

1. Start with why the idea matters.
2. Introduce a concrete bottleneck.
3. Build intuition with diagrams.
4. Walk through a tiny tensor/matrix example.
5. Derive or explain the math.
6. Translate the mechanism into PyTorch.
7. Verify with a small test, benchmark, or comparison.
8. End with a summary and bridge to the next chapter.

This pattern should be reused for the MoE book, especially because MoE benefits from routing diagrams, matrix walkthroughs, dispatch/combine schematics, and load-balancing visualizations.

## Codebase layout extracted

The attached codebase is chapter-first rather than package-first:

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

The setup is intentionally lightweight:

- Early and conceptual chapters use notebooks.
- The complete training pipeline is a script folder with `prepare.py`, `model.py`, `train.py`, and `sample.py`.
- Minimal RL code is a single standalone file.
- Requirements are chapter-local in runnable script chapters.

## Code and template validation performed

- Chapter 6 and chapter 7 `.py` files compile successfully with `python -m compileall`.
- All notebooks parse as valid JSON.
- The derived LaTeX template compiles successfully with `pdflatex` into `latex_template/moe_template.pdf`.
- No repository packaging metadata was present, so no package installation test was applicable.

## Phase 1 deliverable inventory

```text
PHASE_1_REPORT.md
latex_template/
repo_layout/
  codebase_layout.md
  codebase_manifest.txt
source_extracts/
  epub_production_extraction.md
  chapter_structure_outline.md
```

## Recommended decision before Phase 2

Confirm whether the future **MoE Models from Scratch** project should use the derived LaTeX template exactly as drafted, or whether you want a different production target such as Markdown-to-LaTeX, Quarto, or a notebook-first book build.

My default recommendation is to keep the current LaTeX plan because it matches your requirement that every artifact be a `.tex` file included via `\input`, while still allowing generated PDF plots and TikZ schematics.
