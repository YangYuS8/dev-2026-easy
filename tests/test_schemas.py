import pytest
from pydantic import ValidationError

from app.schemas import TaskRead, TaskStatusUpdate


def test_task_status_update_accepts_known_status() -> None:
    payload = TaskStatusUpdate(status="pending")

    assert payload.status == "pending"


def test_task_status_update_rejects_unknown_status() -> None:
    with pytest.raises(ValidationError):
        TaskStatusUpdate(status="blocked")


def test_task_read_rejects_unknown_status() -> None:
    with pytest.raises(ValidationError):
        TaskRead(
            id=1,
            title="Write tests",
            description=None,
            status="blocked",
            created_at="2026-01-01T00:00:00Z",
            updated_at="2026-01-01T00:00:00Z",
        )
