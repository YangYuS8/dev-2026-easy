import sqlite3
from datetime import datetime, timezone

from app.models import Task


def _to_task(row: sqlite3.Row) -> Task:
    return Task(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        status=row["status"],
        created_at=datetime.fromisoformat(row["created_at"]),
        updated_at=datetime.fromisoformat(row["updated_at"]),
    )


def list_tasks(connection: sqlite3.Connection) -> list[Task]:
    rows = connection.execute(
        "SELECT id, title, description, status, created_at, updated_at FROM tasks ORDER BY id ASC"
    ).fetchall()
    return [_to_task(row) for row in rows]


def create_task(connection: sqlite3.Connection, *, title: str, description: str | None) -> Task:
    now = datetime.now(timezone.utc).isoformat()
    cursor = connection.execute(
        "INSERT INTO tasks (title, description, status, created_at, updated_at) VALUES (?, ?, 'pending', ?, ?)",
        (title, description, now, now),
    )
    connection.commit()
    row = connection.execute(
        "SELECT id, title, description, status, created_at, updated_at FROM tasks WHERE id = ?",
        (cursor.lastrowid,),
    ).fetchone()
    return _to_task(row)


def update_task_status(connection: sqlite3.Connection, *, task_id: int, status: str) -> Task | None:
    now = datetime.now(timezone.utc).isoformat()
    connection.execute(
        "UPDATE tasks SET status = ?, updated_at = ? WHERE id = ?",
        (status, now, task_id),
    )
    connection.commit()
    row = connection.execute(
        "SELECT id, title, description, status, created_at, updated_at FROM tasks WHERE id = ?",
        (task_id,),
    ).fetchone()
    return _to_task(row) if row else None
