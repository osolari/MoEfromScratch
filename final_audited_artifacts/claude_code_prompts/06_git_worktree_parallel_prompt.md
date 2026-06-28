# Prompt 06 — Safe chapter worktree workflow

Use this file as an operating note for parallel chapter development.

## Shell setup

```bash
git worktree add ../moe-ch03 ch03-draft
cd ../moe-ch03
claude
```

## Claude Code prompt

```text
/moe-models-from-scratch-developer

This worktree is for Chapter <CHAPTER_NUMBER> only.

Before editing, inspect:

- chapter_packets/chXX.md
- section_development_briefs/chXX/
- latex_book_skeleton/chapters/chXX/
- latex_book_skeleton/figures/chXX/
- latex_book_skeleton/tables/chXX/
- latex_book_skeleton/listings/chXX/
- latex_book_skeleton/equations/chXX/

Do not edit other chapters, shared style files, main.tex, or global planning files unless I explicitly ask.

Report the planned section order and wait for my approval before editing.
```
