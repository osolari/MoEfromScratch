# LaTeX audit

The final LaTeX skeleton compiles successfully to `validation/phase7_latex_skeleton_preview.pdf`.

Phase 7 corrected float behavior after visual inspection showed that normal top-floating figures/tables could drift away from their owning section. The corrected skeleton now uses:

```latex
\usepackage{float}
\usepackage[section]{placeins}
```

All 72 figure wrappers use `\begin{figure}[H]`, and all 72 table wrappers use `\begin{table}[H]`.

The section prose files continue to include artifacts only through `\input{...}` and do not inline raw `figure`, `table`, `lstlisting`, or `equation` environments.
