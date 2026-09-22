# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Setup

[uv](https://docs.astral.sh/uv/) installs Python, locks dependencies, and runs the app.

```bash
cp .env.example .env
uv sync --all-groups
uv run flask db upgrade
uv run pre-commit install
uv run flask run --debug
```

Open http://127.0.0.1:5000. `/` renders this project's name. `GET /api/health` returns JSON.

## Database

Development uses a SQLite file under `instance/` when `DATABASE_URL` is unset. Tests use an in-memory SQLite database. Production uses Postgres. `APP_ENV=production` refuses to boot until `SECRET_KEY` is set and `DATABASE_URL` is a `postgresql+psycopg://` URL, and it marks the session cookie Secure.

## Where code goes

Code is split by technical layer. One resource uses these files:

```text
src/{{ cookiecutter.package_name }}/
  api/<resource>.py              REST routes, imported from api/__init__.py
  web/views/<resource>.py        HTML routes, imported from web/views/__init__.py
  web/templates/<resource>.html
  models/<resource>.py           imported from models/__init__.py
  services/<resource>.py
```

Web views and API modules call services. Services use models and `db.session`. Services do not import Flask's request, response, or template helpers. Models do not import Flask.

A module is registered only when the package `__init__.py` next to it imports it. `api/health.py` and `web/views/index.py` show the route shape. Copy one of those when you add a module. `services/` starts empty. After adding a model, create a migration with `uv run flask db migrate`.

## Checks

```bash
uv run ruff check .
uv run ruff format .
uv run pytest
```
