# Skill audit

The installable skill was repackaged after the Phase 7 corrections. The official skill packager completed successfully and produced the top-level `skill.zip`.

The skill framework now repeats the final LaTeX artifact-placement rule:

- use standalone wrappers,
- include artifacts through `\input`,
- use `[H]` placement for planned teaching figures and tables,
- keep `float` and `placeins` active when compiling.

The package contains 72 standalone section skill files and 85 literal `SKILL.md` mirrors, including the overall and chapter-level frameworks.
