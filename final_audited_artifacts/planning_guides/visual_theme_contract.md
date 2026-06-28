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
