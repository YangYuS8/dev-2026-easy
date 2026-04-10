from datetime import datetime, timezone
from types import SimpleNamespace


def test_list_tasks_endpoint_returns_tasks(client, monkeypatch) -> None:
    now = datetime.now(timezone.utc)

    monkeypatch.setattr(
        "app.api.tasks.crud.list_tasks",
        lambda connection: [
            SimpleNamespace(
                id=1,
                title="Read docs",
                description="Start here",
                status="pending",
                created_at=now,
                updated_at=now,
            )
        ],
    )

    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json()["tasks"][0]["title"] == "Read docs"


def test_create_task_endpoint_returns_created_task(client, monkeypatch) -> None:
    now = datetime.now(timezone.utc)

    monkeypatch.setattr(
        "app.api.tasks.crud.create_task",
        lambda connection, *, title, description: SimpleNamespace(
            id=1,
            title=title,
            description=description,
            status="pending",
            created_at=now,
            updated_at=now,
        ),
    )

    response = client.post(
        "/tasks",
        json={"title": "Read docs", "description": "Start here"},
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Read docs"
    assert response.json()["status"] == "pending"


def test_update_task_status_endpoint_returns_updated_task(client, monkeypatch) -> None:
    now = datetime.now(timezone.utc)

    monkeypatch.setattr(
        "app.api.tasks.crud.update_task_status",
        lambda connection, *, task_id, status: SimpleNamespace(
            id=task_id,
            title="Read docs",
            description="Start here",
            status=status,
            created_at=now,
            updated_at=now,
        ),
    )

    response = client.patch("/tasks/1/status", json={"status": "done"})

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["status"] == "done"


def test_update_task_status_endpoint_returns_not_found(client, monkeypatch) -> None:
    monkeypatch.setattr(
        "app.api.tasks.crud.update_task_status",
        lambda connection, *, task_id, status: None,
    )

    response = client.patch("/tasks/999/status", json={"status": "done"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_update_task_status_endpoint_rejects_invalid_status(client) -> None:
    response = client.patch("/tasks/1/status", json={"status": "archived"})

    assert response.status_code == 422
