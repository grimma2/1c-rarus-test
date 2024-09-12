from enum import Enum as PyEnum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SqlEnum

from . import Base


class PriorityEnum(str, PyEnum):
    low = "low"
    medium = "medium"
    high = "high"


class ToDoTask(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    priority: Mapped[PriorityEnum] = mapped_column(SqlEnum(PriorityEnum), nullable=False)
    title: Mapped[str]
    text: Mapped[str]
