from typing import Optional

from fastapi import APIRouter, Query

from core import DBSessionDep
from schemas.task import ToDoTask as ToDoTaskInput, ToDoTaskOutput, ToDoTaskUpdate
from .crud import get_task, create_task, update_task, delete_task, get_task_list


router = APIRouter(
    prefix="/api/tasks",
    tags=["todo_tasks"],
    responses={404: {"description": "Not found"}},
)


# Получение задачи по ID
@router.get("/{task_id}", response_model=ToDoTaskOutput)
async def task_details(
    task_id: int,
    db_session: DBSessionDep
):
    task = await get_task(db_session, task_id)
    return task


# Создание новой задачи
@router.post("/create", response_model=ToDoTaskOutput)
async def create_new_task(
    task_data: ToDoTaskInput,  # схема данных для создания задачи
    db_session: DBSessionDep,
):
    new_task = await create_task(db_session, **task_data.model_dump())  # Используем crud для создания задачи
    await db_session.commit()  # Коммитим транзакцию в роутере
    return new_task


# Обновление задачи по ID
@router.put("/{task_id}", response_model=ToDoTaskOutput)
async def update_task_details(
    task_id: int,
    task_data: ToDoTaskUpdate,  # схема данных для обновления задачи
    db_session: DBSessionDep,
):  
    # Обновляем задачу через crud функцию
    updated_task = await update_task(db_session, task_id, **task_data.model_dump())
    await db_session.commit()  # Коммитим транзакцию в роутере
    return updated_task


# Удаление задачи по ID
@router.delete("/{task_id}")
async def delete_task_details(
    task_id: int,
    db_session: DBSessionDep,
):
    await delete_task(db_session, task_id)  # Удаляем через crud функцию
    await db_session.commit()  # Коммитим транзакцию в роутере
    return {"message": "Task deleted successfully"}


# Получение списка всех задач
@router.get("/", response_model=list[ToDoTaskOutput])
async def get_all_tasks(
    db_session: DBSessionDep,
    priority: Optional[str] = Query(None, min_length=3, max_length=6)
):
    tasks = await get_task_list(db_session, priority=priority)  # Получаем список задач через crud функцию
    return tasks
