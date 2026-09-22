from flask import Blueprint

bp = Blueprint(
    "web",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static",
)

from {{ cookiecutter.package_name }}.web import views  # noqa: E402, F401
