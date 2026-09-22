# cookiecutter-flask-layout

Cookiecutter for a Flask application. It stamps out an empty project: app factory, config, SQLAlchemy, and migrations. There is no sample domain.

Rename this repository to **cookiecutter-flask-layout**. `cookiecutter-flask` is already the Bootstrap and login template.

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
- Packages for REST modules (`api/`), page modules (`web/views/`), models, and services
- uv, Ruff, pytest, and pre-commit
- A lockfile, written by `uv lock` at generation time when uv is installed

## Check the template

```bash
uvx cookiecutter . --no-input --output-dir /tmp/generated
cd /tmp/generated/flask-app
uv sync --all-groups
uv run ruff check .
uv run ruff format --check .
uv run pytest
```
