from collections.abc import Generator

import psycopg

from app.config import get_settings
from app.models import TASK_STATUSES


ALLOWED_TASK_STATUSES = tuple(sorted(TASK_STATUSES))
TASK_STATUS_CHECK = ", ".join(f"'{status}'" for status in ALLOWED_TASK_STATUSES)


CREATE_TASKS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(32) NOT NULL DEFAULT 'pending' CHECK (status IN ({task_status_check})),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
)
""".format(task_status_check=TASK_STATUS_CHECK)


ENSURE_TASK_STATUS_CONSTRAINT_SQL = """
ALTER TABLE tasks DROP CONSTRAINT IF EXISTS tasks_status_check;
ALTER TABLE tasks
ADD CONSTRAINT tasks_status_check
CHECK (status IN ({task_status_check}))
""".format(task_status_check=TASK_STATUS_CHECK)


def get_connection() -> Generator[psycopg.Connection, None, None]:
    settings = get_settings()
    with psycopg.connect(settings.database_url) as connection:
        yield connection


def init_db() -> None:
    settings = get_settings()
    with psycopg.connect(settings.database_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_TASKS_TABLE_SQL)
            cursor.execute(ENSURE_TASK_STATUS_CONSTRAINT_SQL)
        connection.commit()
