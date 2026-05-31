# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Run the app** (must run from the `src/` directory so Flask can resolve templates/static):
```
cd src && python app.py
```
Visit `http://127.0.0.1:5000`.

**Install dependencies:**
```
uv pip install -r requirements.txt
```

**Run all tests:**
```
python -m unittest discover -s tests
```

**Run a single test:**
```
python -m unittest tests.test_app.AppTestCase.test_index
```

## Architecture

This is a minimal Flask app with no database — course data lives in an in-memory list in `src/models.py`.

**Request flow:**
1. `src/app.py` — creates the Flask app and registers two URL rules: `/` → `index`, `/course/<course_id>` → `course`
2. `src/views.py` — view functions that render templates
3. `src/models.py` — `Course` class and a hardcoded `courses` list

**Template inheritance is inconsistent in the starter:**
- `course.html` correctly uses `{% extends 'layout.html' %}` with `{% block content %}`
- `index.html` incorrectly uses `{% include 'layout.html' %}` instead — this should be `{% extends %}` to match the pattern

**Known gap:** `views.py` does not import from `models.py`. The `course` view passes only `course_id` to the template, not an actual `Course` object. To wire them together, the view needs to look up the course from the `courses` list and pass it as `course=courses[int(course_id)-1]`.

**Static assets:** A single CSS file at `src/static/css/styles.css`. Referenced via `url_for('static', filename='css/styles.css')` in templates.

**Add unit tests:**  Whenever you do changes or add new functionality, add unit tests for it.