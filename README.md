# cookiecutter-flask-layout

Cookiecutter for a Flask application laid out in technical layers. A resource is split across `api/`, `web/views/`, `web/templates/`, `models/`, and `services/`.

Web views and API modules call services. Services use models and the database session. Services do not import Flask request, response, or template helpers. Models do not import Flask. A module is part of the app only after its package `__init__.py` imports it.

## Generate a project

Install [uv](https://docs.astral.sh/uv/).

```bash
uvx cookiecutter gh:syedwaseemjan/cookiecutter-flask-layout
```

From a local checkout:

```bash
uvx cookiecutter /path/to/cookiecutter-flask-layout
```

The defaults create `flask-app/` with the Python package `flaskapp`. Change the project name when prompted.

## What you get

- Python 3.12 or 3.13, Flask 3, SQLAlchemy 2, and Alembic through Flask-Migrate
- Layer packages for REST modules (`api/`), pages (`web/views/`), models, and services
- uv, Ruff, pytest, and pre-commit
- A lockfile, written by `uv lock` at generation time when uv is installed

## Layout

```text
src/<package>/
  api/<resource>.py
  web/views/<resource>.py
  web/templates/<resource>.html
  models/<resource>.py
  services/<resource>.py
```

Import each new module from the `__init__.py` beside it. `api/health.py` and `web/views/index.py` show the route shape. `services/` starts empty; put query and transaction code there when a feature needs it.

Development and tests use SQLite. `APP_ENV=production` uses Postgres and refuses to start until `SECRET_KEY` is set and `DATABASE_URL` is a `postgresql+psycopg://` URL.

## Check the template

```bash
uvx cookiecutter . --no-input --output-dir /tmp/generated
cd /tmp/generated/flask-app
uv sync --all-groups
uv run ruff check .
uv run ruff format --check .
uv run pytest
```
