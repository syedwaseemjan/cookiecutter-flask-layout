import pytest

from {{ cookiecutter.package_name }} import create_app
from {{ cookiecutter.package_name }}.config import TestingConfig
from {{ cookiecutter.package_name }}.extensions import db


@pytest.fixture
def app():
    application = create_app(TestingConfig)
    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
