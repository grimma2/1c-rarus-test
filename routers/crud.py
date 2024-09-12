from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.task import ToDoTask as TaskDBModel, PriorityEnum


async def get_task(db_session: AsyncSession, task_id: int) -> TaskDBModel:
    task = (await db_session.scalars(select(TaskDBModel).where(TaskDBModel.id == task_id))).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task


# Создание новой задачи
async def create_task(db_session: AsyncSession, title: str, priority: str, text: str) -> TaskDBModel:
    new_task = TaskDBModel(title=title, priority=priority, text=text)
    
    db_session.add(new_task)  # Добавляем новую задачу в сессию

    return new_task


# Обновление задачи по ID
async def update_task(db_session: AsyncSession, task_id: int, title: str, priority: PriorityEnum, text: str) -> TaskDBModel:
    task = await get_task(db_session, task_id)  # Получаем задачу по ID
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if title:
        print(title)
        task.title = title

    if priority:
        print(priority.value)
        task.priority = priority.value

    if text:
        print(type(text), dir(text))
        task.text = text
    
    return task


# Удаление задачи по ID
async def delete_task(db_session: AsyncSession, task_id: int) -> None:
    task = await get_task(db_session, task_id)  # Проверяем наличие задачи
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    await db_session.delete(task)  # Удаляем задачу


# Получение списка всех задач
async def get_task_list(db_session: AsyncSession, priority: str = None) -> list[TaskDBModel]:
    query = select(TaskDBModel)
    
    if priority:
        query = query.where(TaskDBModel.priority == priority)
    
    tasks = (await db_session.scalars(query)).all()
    
    print(tasks)
    return tasks