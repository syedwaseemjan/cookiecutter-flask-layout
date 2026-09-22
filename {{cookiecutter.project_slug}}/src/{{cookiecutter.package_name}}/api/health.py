from flask import jsonify

from {{ cookiecutter.package_name }}.api import bp


@bp.get("/health")
def health():
    return jsonify(status="ok")
