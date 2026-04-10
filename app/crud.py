import psycopg
from psycopg.rows import class_row

from app.models import Task


def list_tasks(connection: psycopg.Connection) -> list[Task]:
    with connection.cursor(row_factory=class_row(Task)) as cursor:
        cursor.execute(
            """
            SELECT id, title, description, status, created_at, updated_at
            FROM tasks
            ORDER BY id ASC
            """
        )
        return list(cursor.fetchall())


def create_task(
    connection: psycopg.Connection,
    *,
    title: str,
    description: str | None,
) -> Task:
    with connection.cursor(row_factory=class_row(Task)) as cursor:
        cursor.execute(
            """
            INSERT INTO tasks (title, description)
            VALUES (%s, %s)
            RETURNING id, title, description, status, created_at, updated_at
            """,
            (title, description),
        )
        task = cursor.fetchone()

    connection.commit()
    if task is None:
        raise RuntimeError("Failed to create task")
    return task


def update_task_status(
    connection: psycopg.Connection,
    *,
    task_id: int,
    status: str,
) -> Task | None:
    with connection.cursor(row_factory=class_row(Task)) as cursor:
        cursor.execute(
            """
            UPDATE tasks
            SET status = %s, updated_at = NOW()
            WHERE id = %s
            RETURNING id, title, description, status, created_at, updated_at
            """,
            (status, task_id),
        )
        task = cursor.fetchone()

    connection.commit()
    return task
