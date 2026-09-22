from flask import render_template

from {{ cookiecutter.package_name }}.web import bp


@bp.get("/")
def index():
    return render_template("index.html")
