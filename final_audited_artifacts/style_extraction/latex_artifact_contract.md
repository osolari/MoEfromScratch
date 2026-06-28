# LaTeX artifact contract

This is the production rulebook for the future MoE book. The point is to make each chapter developable in a separate chat session without breaking global consistency.

## Required directory structure

```text
moe-models-from-scratch/
├── main.tex
├── styles/
│   ├── preamble.tex
│   ├── colors.tex
│   ├── macros.tex
│   └── tikzstyles.tex
├── chapters/
│   └── ch01/
│       ├── chapter.tex
│       └── sections/
│           ├── 01-opening.tex
│           ├── 02-intuition.tex
│           ├── 03-mechanics.tex
│           ├── 04-implementation.tex
│           └── 05-summary.tex
├── figures/
│   └── ch01/
│       ├── fig-roadmap.tex
│       ├── fig-router-schematic.tex
│       └── fig-external-comparison.tex
├── tables/
│   └── ch01/
│       └── tab-concept-map.tex
└── listings/
    └── ch01/
        └── lst-minimal-router.tex
```


> Phase 2 seed note: the preview template in `latex_theme_contract/` currently combines artifact macros and TikZ styles in `styles/theme_macros.tex`. The final production template can split this into `macros.tex` and `tikzstyles.tex` without changing the artifact contract.

## Inclusion rule

A chapter or section file may include artifacts only like this:

```latex
\input{figures/ch01/fig-router-schematic}
\input{tables/ch01/tab-routing-notation}
\input{listings/ch01/lst-router-forward}
```

Do not place `figure`, `table`, `lstlisting`, or large TikZ bodies directly inside chapter prose unless the artifact is a one-line inline equation or a tiny local example.

## TikZ figure wrapper

```latex
\begin{figure}[t]
\centering
\begin{tikzpicture}[node distance=8mm]
  % diagram body here
\end{tikzpicture}
\caption{Explain the takeaway, not only the drawing.}
\label{fig:ch01-router-schematic}
\end{figure}
```

## External PDF figure wrapper

```latex
\begin{figure}[t]
\centering
\includegraphics[width=\BookFigureWidth]{figures/ch01/assets/router-comparison.pdf}
\caption{Explain the source, transformation, or comparison shown by the external figure.}
\label{fig:ch01-router-comparison}
\end{figure}
```

## Table wrapper

```latex
\begin{table}[t]
\centering
\caption{A concise caption that states what the table compares.}
\label{tab:ch01-routing-notation}
\begin{tabular}{lll}
\toprule
Symbol & Shape & Meaning \\
\midrule
$x$ & $(B,T,d)$ & token embeddings \\
\bottomrule
\end{tabular}
\end{table}
```

## Listing wrapper

```latex
\begin{lstlisting}[style=bookpython,caption={A minimal top-k router.},label={lst:ch01-minimal-router}]
# code here
\end{lstlisting}
```

## Label conventions

| Artifact | Label prefix | Example |
|---|---|---|
| Figure | `fig:chNN-name` | `fig:ch03-top2-routing` |
| Table | `tab:chNN-name` | `tab:ch03-load-metrics` |
| Listing | `lst:chNN-name` | `lst:ch03-router-forward` |
| Equation | `eq:chNN-name` | `eq:ch03-aux-loss` |
| Section | `sec:chNN-name` | `sec:ch03-load-balancing` |

## Per-section artifact placeholder requirements

Each section plan created later should list planned artifacts in this exact format:

```markdown
### Planned artifacts

- `figures/ch03/fig-top2-routing.tex` - TikZ. Shows token dispatch from router logits to the two selected experts. Caption placeholder included.
- `tables/ch03/tab-routing-notation.tex` - Table. Defines symbols and tensor shapes used in the section.
- `listings/ch03/lst-top2-router.tex` - Python listing. Implements the forward pass for top-2 routing.
```

## Proofread checklist

Before a section is considered ready:

- Every referenced artifact path exists.
- Every artifact wrapper contains a caption and label.
- Every TikZ diagram uses only the global color names from `styles/colors.tex`.
- Every listing compiles under the chosen LaTeX listing system.
- No raw `\includegraphics` appears in chapter or section prose.
- Captions and prose use the same terminology and tensor shapes.
