# Corrections applied in Phase 7

- `final_audited_artifacts/latex_book_skeleton/main.tex`: added \usepackage[section]{placeins} (prevents figure/table floats from drifting into later sections in the compiled book skeleton).
- `final_audited_artifacts/planning_guides/latex_artifact_contract.md`: added float placement rule (the rendered Phase 5 skeleton showed deferred floats crossing section boundaries before this correction).
- `final_audited_artifacts/planning_guides/proofread_checklist.md`: added float placement rule (the rendered Phase 5 skeleton showed deferred floats crossing section boundaries before this correction).
- `final_audited_artifacts/planning_guides/separate_session_workflow.md`: added float placement rule (the rendered Phase 5 skeleton showed deferred floats crossing section boundaries before this correction).
- `final_audited_artifacts/section_development_briefs`: patched 72 section briefs with float-placement acceptance check (section briefs are intended to be self-contained handoffs; the float rule must travel with each brief).
- `final_audited_artifacts/session_starters`: patched 72 session starters with float-placement note (isolated section-development chats need the same artifact-placement guard).
- `final_audited_artifacts/skill_framework`: patched skill markdown and skill references with float-placement rule (the installable skill and standalone skill files must enforce the corrected LaTeX contract).
- `final_audited_artifacts/skill_framework/installable_skill_source/moe-models-from-scratch-developer/SKILL.md`: added non-negotiable float-placement rule (installable skill must preserve the corrected artifact contract).
- `final_audited_artifacts/skill_framework/installable_skill_source/moe-models-from-scratch-developer/references/theme-and-artifact-contract.md`: added float placement rule (skill references must mirror final LaTeX artifact contract).
- `final_audited_artifacts/skill_framework/installable_skill_source/moe-models-from-scratch-developer/references/proofread-checklist.md`: added float placement rule (skill references must mirror final LaTeX artifact contract).
- `final_audited_artifacts/skill_framework/installable_skill_source/moe-models-from-scratch-developer/references/separate-session-workflow.md`: added float placement rule (skill references must mirror final LaTeX artifact contract).

## Additional final proofread corrections

- Corrected acronym capitalization in seven LaTeX listing captions: FFN, MLPs, FFNs, MoE, and MiniDeepSeekMoE now render with the intended technical capitalization while labels and Python function names remain stable.
- Corrected the installable skill UI metadata from `Latex-first` to `LaTeX-first`; YAML frontmatter descriptions remain lowercase to satisfy skill validation conventions.
- Removed a duplicate float-placement bullet from the installable skill entrypoint while preserving the corrected `placeins`/`\FloatBarrier` rule.

## Float pinning correction

- `final_audited_artifacts/latex_book_skeleton/main.tex`: ensured \usepackage{float} and \usepackage[section]{placeins} (supports [H] figure/table placement and section barriers).
- `final_audited_artifacts/latex_book_skeleton/figures`: confirmed 72/72 figure wrappers use [H] (keeps teaching figures with their owning section).
- `final_audited_artifacts/latex_book_skeleton/tables`: confirmed 72/72 table wrappers use [H] (keeps teaching tables with their owning section).
- `final_audited_artifacts/planning_guides/latex_artifact_contract.md`: strengthened float-placement rule to [H] plus placeins (section barriers alone may place prior-section floats at the top of a later-section page).
- `final_audited_artifacts/planning_guides/separate_session_workflow.md`: strengthened float-placement rule to [H] plus placeins (section barriers alone may place prior-section floats at the top of a later-section page).
- `final_audited_artifacts/planning_guides/proofread_checklist.md`: strengthened float-placement rule to [H] plus placeins (section barriers alone may place prior-section floats at the top of a later-section page).
- `final_audited_artifacts/skill_framework/installable_skill_source/moe-models-from-scratch-developer/references/theme-and-artifact-contract.md`: strengthened float-placement rule to [H] plus placeins (section barriers alone may place prior-section floats at the top of a later-section page).
- `final_audited_artifacts/skill_framework/installable_skill_source/moe-models-from-scratch-developer/references/proofread-checklist.md`: strengthened float-placement rule to [H] plus placeins (section barriers alone may place prior-section floats at the top of a later-section page).
- `final_audited_artifacts/skill_framework/installable_skill_source/moe-models-from-scratch-developer/references/separate-session-workflow.md`: strengthened float-placement rule to [H] plus placeins (section barriers alone may place prior-section floats at the top of a later-section page).
- `final_audited_artifacts/section_development_briefs`: updated 72 markdown files with [H] float placement wording (keeps all handoffs aligned with final artifact placement contract).
- `final_audited_artifacts/session_starters`: updated 72 markdown files with [H] float placement wording (keeps all handoffs aligned with final artifact placement contract).
- `final_audited_artifacts/skill_framework`: updated 328 markdown files with [H] float placement wording (keeps all handoffs aligned with final artifact placement contract).
- `final_audited_artifacts/section_development_briefs`: confirmed 72 section briefs contain final float rule (each section can be developed in a separate chat without losing the placement rule).
