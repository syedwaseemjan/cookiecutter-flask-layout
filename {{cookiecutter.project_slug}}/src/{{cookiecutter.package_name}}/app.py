import os
from pathlib import Path

from flask import Flask, jsonify, render_template, request

from {{ cookiecutter.package_name }}.config import CONFIGS, Config
from {{ cookiecutter.package_name }}.extensions import db, migrate


def create_app(config_class: type[Config] | None = None) -> Flask:
    if config_class is None:
        name = os.environ.get("APP_ENV", "development")
        try:
            config_class = CONFIGS[name]
        except KeyError as exc:
            raise RuntimeError(f"Unknown APP_ENV {name!r}") from exc

    app = Flask(__name__, instance_relative_config=True, static_folder=None)
    app.config.from_object(config_class)
    if not app.config.get("SECRET_KEY"):
        raise RuntimeError("Set SECRET_KEY before starting the app")

    _configure_database(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from {{ cookiecutter.package_name }} import models  # noqa: F401
    from {{ cookiecutter.package_name }}.api import bp as api_bp
    from {{ cookiecutter.package_name }}.web import bp as web_bp

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    _register_error_handlers(app)

    @app.shell_context_processor
    def shell_context():
        return {"db": db}

    return app


def _configure_database(app: Flask) -> None:
    if app.config.get("SQLALCHEMY_DATABASE_URI"):
        return
    configured = os.environ.get("DATABASE_URL")
    if configured:
        app.config["SQLALCHEMY_DATABASE_URI"] = configured
        return
    if app.config.get("DATABASE_REQUIRED"):
        raise RuntimeError("Set DATABASE_URL before starting the app")
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    db_path = Path(app.instance_path) / "{{ cookiecutter.project_slug }}.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"


def _register_error_handlers(app: Flask) -> None:
    @app.errorhandler(404)
    def not_found(_error):
        if request.path.startswith("/api"):
            return jsonify(error="Not found"), 404
        return render_template("errors/404.html"), 404
