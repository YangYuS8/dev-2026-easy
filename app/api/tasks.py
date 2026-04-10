import psycopg
from fastapi import APIRouter, Depends, HTTPException, status

from app import crud
from app.db import get_connection
from app.schemas import TaskCreate, TaskListResponse, TaskRead, TaskStatusUpdate


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=TaskListResponse)
def get_tasks(
    connection: psycopg.Connection = Depends(get_connection),
) -> TaskListResponse:
    tasks = crud.list_tasks(connection)
    return TaskListResponse(
        tasks=[TaskRead.model_validate(task.__dict__) for task in tasks]
    )


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreate,
    connection: psycopg.Connection = Depends(get_connection),
) -> TaskRead:
    task = crud.create_task(
        connection,
        title=payload.title,
        description=payload.description,
    )
    return TaskRead.model_validate(task.__dict__)


@router.patch("/{task_id}/status", response_model=TaskRead)
def update_task_status(
    task_id: int,
    payload: TaskStatusUpdate,
    connection: psycopg.Connection = Depends(get_connection),
) -> TaskRead:
    task = crud.update_task_status(connection, task_id=task_id, status=payload.status)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )

    return TaskRead.model_validate(task.__dict__)
