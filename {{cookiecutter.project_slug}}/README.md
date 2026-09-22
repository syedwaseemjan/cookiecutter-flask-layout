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

Open http://127.0.0.1:5000. `APP_ENV=production` refuses to boot until `SECRET_KEY` is set, and it marks the session cookie Secure.

`/` renders this project's name. `GET /api/health` returns JSON.

## Where code goes

```text
src/{{ cookiecutter.package_name }}/
  api/            one module per REST resource, imported from api/__init__.py
  web/views/      one module per page, imported from web/views/__init__.py
  models/         SQLAlchemy models, imported from models/__init__.py
  services/       called by views and API modules
```

`api/health.py` and `web/views/index.py` show the shape. Copy one of those when you add a module, and import the new module from the package `__init__.py` next to it. After adding a model, create a migration with `uv run flask db migrate`.

## Checks

```bash
uv run ruff check .
uv run ruff format .
uv run pytest
```
