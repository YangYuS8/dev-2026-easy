from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class TaskStatus(StrEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"


TASK_STATUSES = tuple(status.value for status in TaskStatus)


@dataclass
class Task:
    id: int
    title: str
    description: str | None
    status: str
    created_at: datetime
    updated_at: datetime
