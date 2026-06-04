Custom command /implement_ui_user_story

Description: Orchestrates the complete UI feature workflow: Design -> Implement -> Verify.

You are implementing a UI feature from a user story. Follow these two phases in order — do not skip or merge them.

## User Story

$ARGUMENTS

---

## Phase 1 — UX Design

Invoke the `ux-design-planner` agent with the user story above. Pass the full story text as-is so the agent has complete context. Wait for the agent to return a design spec before proceeding.

The design spec must include at minimum:
- Page layout / component structure
- Key interaction flows (happy path + edge cases)
- Data displayed and its source
- Any new routes or URL changes
- Wait for "Ready to coding signal"

Do not begin coding until Phase 1 is complete and you have a written design spec in hand.

---

## Phase 2 — Implementation

Using the design spec from Phase 1, implement the feature in this Flask project.

Project conventions (from CLAUDE.md):
- Templates live in `src/templates/`. Use `{% extends 'layout.html' %}` with `{% block content %}` — never `{% include %}`.
- Views live in `src/views.py`; routes are registered in `src/app.py`.
- Course data is the in-memory `courses` list in `src/models.py`.
- Static CSS is at `src/static/css/styles.css`.
- For every code change, add or update unit tests in `tests/`.

Steps:
1. Identify which files need to change based on the design spec.
2. Make the changes file by file.
3. Add or update unit tests covering the new behavior.
4. Run the test suite (`python -m unittest discover -s tests`) and confirm all tests pass before reporting done.
