from typing import Optional

from pydantic import BaseModel, ConfigDict

from models.task import PriorityEnum


class ToDoTask(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    priority: PriorityEnum
    title: str
    text: str


class ToDoTaskOutput(ToDoTask):
    id: int


class ToDoTaskUpdate(BaseModel):
    priority: Optional[PriorityEnum] = None
    title: Optional[str] = None
    text: Optional[str] = None
