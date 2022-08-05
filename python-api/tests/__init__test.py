import pytest

from app import create_app


def test_app_creates(app):  # noqa
    assert app


def test_app_healthy(app, client):  # noqa
    with client:
        resp = client.get("/health")
        assert resp.status_code == 200
        assert resp.is_json
        assert resp.json == "healthy"


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()
