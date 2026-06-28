# EPUB production extraction

## What the EPUB contains

The attached EPUB is a compiled EPUB package, not a LaTeX source archive. Its key paths are:

```text
mimetype
META-INF/container.xml
OEBPS/content.opf
OEBPS/toc.ncx
OEBPS/Styles/stylesheet.css
OEBPS/Text/titlepage.xhtml
OEBPS/Text/copyright.html
OEBPS/Text/welcome.html
OEBPS/Text/brief-table-of-contents.html
OEBPS/Text/chapter-1.html ... chapter-8.html
OEBPS/Images/*.png, *.jpg
OEBPS/Misc/JetBrains.woff2
```

No `.tex`, `.sty`, `.cls`, `.bib`, or Makefile source was found in the EPUB or code ZIP.

## Source style extracted from `stylesheet.css`

| Element | EPUB/CSS behavior | LaTeX analogue in derived template |
|---|---|---|
| Body font | Verdana-like sans-serif in EPUB | Neutral text with readable spacing; can be switched to sans if desired |
| Heading color | `#000055` and `#141464` | `BookNavy`, `BookDeepBlue` |
| Listing header | white text on `#020056` | `BookListingHeader` for listing title bars |
| Callout background | `#E6E6E6` | `definitionbox` and `notebox` tcolorboxes |
| Code background | `#F2F2F2` | `lstlisting` style `bookpython` |
| Figures | centered image plus caption | figure wrappers with `\caption` and `\label` |
| Tables | black borders in EPUB | LaTeX `booktabs` tables for print quality |

## Reusable book pattern extracted

Most technical chapters follow this flow:

1. `This chapter covers` checklist.
2. Motivation and bottleneck.
3. Intuition with diagrams.
4. Step-by-step tensor/matrix walkthrough.
5. Math or formula breakdown.
6. From-scratch implementation listing.
7. Verification or empirical comparison.
8. Summary and bridge to next topic.

## Figure/listing density by chapter

| Chapter | Figures | Code/listings | Tables | Callouts |
|---:|---:|---:|---:|---:|
| 1 | 9 | 0 | 0 | 0 |
| 2 | 25 | 5 | 0 | 3 |
| 3 | 37 | 7 | 2 | 1 |
| 4 | 30 | 6 | 1 | 1 |
| 5 | 31 | 6 | 0 | 1 |
| 6 | 12 | 30 | 0 | 0 |
| 7 | 15 | 5 | 4 | 0 |
| 8 | 31 | 4 | 2 | 8 |

## Image dimensions and figure theme

Most diagrams are approximately 1042 px wide, with chapter 7 and 8 frequently using a consistent 1042 x 581 format. The visual theme is schematic and pedagogical: large blocks, arrows, matrices, color-coded paths, and captions that explain the takeaway rather than merely naming the figure.

## Derived reusable palette

| Name | Hex | Use |
|---|---:|---|
| BookNavy | `#000055` | Main heading/callout title accent |
| BookDeepBlue | `#141464` | Secondary heading/link/arrow accent |
| BookListingHeader | `#020056` | Code listing title header |
| BookCalloutGray | `#E6E6E6` | Definition/note callouts |
| BookCodeBg | `#F2F2F2` | Code block background |
| BookInputBlue | `#A6D8FF` | Tensor/input blocks |
| BookQueryBlue | `#2F6FA3` | Projection/attention blocks |
| BookExpertPurple | `#9050FF` | Routed expert blocks |
| BookExpertGold | `#FFD080` | Weights/scores/highlights |
| BookSharedGreen | `#A8DDA8` | Shared expert/general path |
| BookRouterRed | `#E03030` | Router/bias/imbalance highlights |
| BookMutedGray | `#D0D0D0` | Dormant experts/background structure |
| BookSoftFill | `#F0F0FF` | Light fill for neutral blocks |
