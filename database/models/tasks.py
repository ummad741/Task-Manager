import enum
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
# localfiles
from database.config import Base
from database.fields import (
    str_30, str_50, full_text
)


class TasksTable(Base):
    class Level(enum.Enum):
        hard = "Hard"
        medium = "Medium"
        easy = "Easy"

    class Point(enum.Enum):
        five = 5
        three = 3
        one = 1

    __tablename__ =  "tasks"
    title: Mapped[str_30]
    description: Mapped[full_text]
    level: Mapped[Level]
    point: Mapped[Point]
    workers_id: Mapped[int] = mapped_column(
        ForeignKey("workers.id", ondelete="CASCADE"))
    worker: Mapped[int] = relationship(back_populates='tasks')
