# LaTeX artifact contract

All book development must stay LaTeX-first.

## Section rule

Every artifact is a separate `.tex` wrapper and is included from section prose with `\input`.

```latex
\input{figures/chXX/fig-section-slug}
\input{tables/chXX/tab-section-slug}
\input{equations/chXX/eq-section-slug}
\input{listings/chXX/lst-section-slug}
```

## Wrapper rules

- TikZ figure wrappers contain a complete `figure` environment, `tikzpicture`, `\caption`, and `\label`.
- PDF figure wrappers contain a complete `figure` environment, `\includegraphics[width=\BookFigureWidth]{...}`, `\caption`, and `\label`.
- Table wrappers contain a complete table environment, caption, label, and `booktabs`/`tabularx` styling.
- Listing wrappers use `lstlisting` with `style=bookpython`, caption, and label.
- Equation wrappers contain an equation environment and a stable `eq:` label.

## Float placement rule added in Phase 7

Keep `\usepackage{float}` and `\usepackage[section]{placeins}` active in `latex_book_skeleton/main.tex`. Planned teaching figures and tables should default to `[H]` placement inside their standalone wrappers so artifacts stay with the section that introduces them. If a developed section contains unusual float pressure, add an explicit `\FloatBarrier` at the end of that section after the final artifact discussion.