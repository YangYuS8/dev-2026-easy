import pytest
from fastapi.testclient import TestClient

from app.db import get_connection
from app.main import app


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> TestClient:
    monkeypatch.setattr("app.main.init_db", lambda: None)

    def fake_get_connection():
        yield object()

    app.dependency_overrides[get_connection] = fake_get_connection
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
