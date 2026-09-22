"""REST modules. Add one module per resource and import it below."""

from flask import Blueprint

bp = Blueprint("api", __name__)

from {{ cookiecutter.package_name }}.api import health  # noqa: E402, F401
