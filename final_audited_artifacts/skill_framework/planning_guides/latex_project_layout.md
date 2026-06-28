# LaTeX project layout plan

The book development must be LaTeX-first. The Phase 4 skeleton already follows the intended layout.

```text
moe-models-from-scratch/
├── main.tex
├── styles/
│   ├── colors.tex
│   ├── macros.tex
│   └── tikzstyles.tex
├── chapters/
│   └── chNN/
│       ├── chapter.tex
│       └── sections/
│           └── SS-section-slug.tex
├── figures/chNN/fig-section-slug.tex
├── tables/chNN/tab-section-slug.tex
├── listings/chNN/lst-section-slug.tex
└── equations/chNN/eq-section-slug.tex
```

## Hard rules

- Chapter files input section files.
- Section files input artifacts.
- Artifact files contain their own environment, caption, and label.
- TikZ diagrams live in figure wrapper files.
- Generated plots or external PDFs must be included only through a wrapper file containing `\includegraphics`, caption, and label.
- The global semantic color map is defined once in `styles/colors.tex`.
