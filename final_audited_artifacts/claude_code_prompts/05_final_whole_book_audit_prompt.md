# Prompt 05 — Final whole-book production audit

Use after all chapters are drafted and merged.

```text
/moe-models-from-scratch-developer

Perform the final whole-book production audit.

Scope:
latex_book_skeleton/

Tasks:

1. Compile the full book.
2. Check all section files for raw figure/table/listing/equation environments.
3. Check that all planned artifact wrappers exist.
4. Check that every wrapper has a caption and label where appropriate.
5. Check that TikZ figures follow the visual theme.
6. Check that all MiniDeepSeekMoE invariants are preserved.
7. Check that Chapter 9 never uses router bias to compute final combine weights.
8. Check notation consistency across chapters.
9. Check code listing consistency with the codebase.
10. Produce a final punch list before making edits.

Do not make broad rewrites unless they address a concrete issue.
```
