import pytest

from {{ cookiecutter.package_name }} import create_app
from {{ cookiecutter.package_name }}.config import DevelopmentConfig, ProductionConfig


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"{{ cookiecutter.project_name }}" in response.data


def test_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_unknown_api_route(client):
    response = client.get("/api/missing")
    assert response.status_code == 404
    assert response.get_json()["error"] == "Not found"


def test_stylesheet(client):
    response = client.get("/static/css/app.css")
    assert response.status_code == 200


def test_production_requires_database_url(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)

    class Production(ProductionConfig):
        SECRET_KEY = "production-secret"

    with pytest.raises(RuntimeError, match="DATABASE_URL"):
        create_app(Production)


def test_production_accepts_postgres_url(monkeypatch):
    database_url = "postgresql+psycopg://localhost/app"
    monkeypatch.setenv("DATABASE_URL", database_url)

    class Production(ProductionConfig):
        SECRET_KEY = "production-secret"

    application = create_app(Production)
    assert application.config["SQLALCHEMY_DATABASE_URI"] == database_url


def test_production_rejects_sqlite(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:////tmp/app.db")

    class Production(ProductionConfig):
        SECRET_KEY = "production-secret"

    with pytest.raises(RuntimeError, match="PostgreSQL"):
        create_app(Production)


def test_upgrade(tmp_path):
    class MigrateConfig(DevelopmentConfig):
        DEBUG = False
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{tmp_path / 'app.db'}"

    application = create_app(MigrateConfig)
    result = application.test_cli_runner().invoke(args=["db", "upgrade"])
    assert result.exit_code == 0, result.output
