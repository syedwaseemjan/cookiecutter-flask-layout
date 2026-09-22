from {{ cookiecutter.package_name }} import create_app
from {{ cookiecutter.package_name }}.config import DevelopmentConfig


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


def test_upgrade(tmp_path):
    class MigrateConfig(DevelopmentConfig):
        DEBUG = False
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{tmp_path / 'app.db'}"

    application = create_app(MigrateConfig)
    result = application.test_cli_runner().invoke(args=["db", "upgrade"])
    assert result.exit_code == 0, result.output
