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
