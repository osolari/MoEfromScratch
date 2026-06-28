# Theme and artifact contract

# Visual theme contract

Use this file as the reproducible figure and table theme for *MoE Models from Scratch*.

## Color map

| Role | LaTeX color | Hex | Use |
|---|---|---:|---|
| Main navy | `BookNavy` | `#000055` | chapter titles, structural headings |
| Deep blue | `BookDeepBlue` | `#141464` | neutral diagram text and arrows |
| Listing header | `BookListingHeader` | `#020056` | code listing title bars |
| Callout gray | `BookCalloutGray` | `#E6E6E6` | note, checkpoint, and chapter-cover boxes |
| Code background | `BookCodeBg` | `#F2F2F2` | listing background |
| Token purple | `MoETokenPurple` | `#C060E0` | tokens and token-flow dots |
| Router cyan | `MoERouterCyan` | `#00A7C1` | routers, score matrices, dispatch arrows |
| Expert purple | `MoEExpertPurple` | `#9050FF` | generic routed experts |
| Active expert green | `MoEActiveGreen` | `#70D050` | selected experts and active routes |
| Output red | `MoEOutputRed` | `#F05050` | outputs, overflow, imbalance warnings |
| Capacity gold | `MoECapacityGold` | `#FFD080` | capacity, top-k slots, quotas, bias state |
| Shared expert green | `MoESharedGreen` | `#A8DDA8` | shared experts and always-on paths |
| Muted gray | `MoEMutedGray` | `#D0D0D0` | inactive routes and background structures |
| Soft fill | `MoESoftFill` | `#F0F0FF` | grouping regions |

## Diagram rules

- Use TikZ for mechanism schematics.
- Use generated PDF assets for plots, dashboards, and diagnostics.
- Never insert raw `\includegraphics` directly in section prose; put it in the figure wrapper and include that wrapper with `\input`.
- Preserve left-to-right flow when possible: tokens -> router -> selected experts -> combine -> output.
- Use red only for outputs, dropped tokens, overload, or imbalance.


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


## Visual theme summary

Use semantic LaTeX color names only.

| Role | LaTeX color | Hex | Use |
|---|---|---:|---|
| Main navy | `BookNavy` | `#000055` | chapter titles and structural headings |
| Deep blue | `BookDeepBlue` | `#141464` | neutral diagram text and arrows |
| Listing header | `BookListingHeader` | `#020056` | code listing title bars |
| Callout gray | `BookCalloutGray` | `#E6E6E6` | notes, checkpoints, and chapter-cover boxes |
| Code background | `BookCodeBg` | `#F2F2F2` | listing background |
| Token purple | `MoETokenPurple` | `#C060E0` | tokens and token-flow dots |
| Router cyan | `MoERouterCyan` | `#00A7C1` | routers, score matrices, dispatch arrows |
| Expert purple | `MoEExpertPurple` | `#9050FF` | generic routed experts |
| Active expert green | `MoEActiveGreen` | `#70D050` | selected experts and active routes |
| Output red | `MoEOutputRed` | `#F05050` | outputs, overflow, imbalance warnings |
| Capacity gold | `MoECapacityGold` | `#FFD080` | capacity, top-k slots, quotas, and bias state |
| Shared expert green | `MoESharedGreen` | `#A8DDA8` | shared experts and always-on paths |
| Muted gray | `MoEMutedGray` | `#D0D0D0` | inactive routes and background structures |
| Soft fill | `MoESoftFill` | `#F0F0FF` | grouping regions |

Use semantic TikZ styles from `styles/tikzstyles.tex`. Do not scatter raw hex colors through figure bodies.

## Float placement rule added in Phase 7

Keep `\usepackage{float}` and `\usepackage[section]{placeins}` active in `latex_book_skeleton/main.tex`. Planned teaching figures and tables should default to `[H]` placement inside their standalone wrappers so artifacts stay with the section that introduces them. If a developed section contains unusual float pressure, add an explicit `\FloatBarrier` at the end of that section after the final artifact discussion.