from app.config import get_settings


def test_settings_default_port(monkeypatch) -> None:
    monkeypatch.delenv("APP_PORT", raising=False)
    get_settings.cache_clear()
    settings = get_settings()
    assert settings.app_port == 8000
    get_settings.cache_clear()


def test_health_endpoint_returns_ok_status(client) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
