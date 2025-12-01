import enum
# relationshipda kop object saqlanishi
from typing import List
# Optionalning manosi bu None bolishi mumkun
from datetime import date
from typing import Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
# local files
from database.config import Base
from models.tasks import TasksTable
from database.fields import (
    str_30, str_50,full_text
)

class WorkersTable(Base):
    class Role(enum.Enum):
        profesional = "Profesional"
        middle = 'Middle'
        intern = "Intern"

    __tablename__ = 'workers'
    name: str_30
    last_name: str_30
    birht_date: Mapped[date] = mapped_column(date)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    role: Mapped[Role]
    tasks: Mapped[List["Tasks"]] = relationship(
        back_populates="workers", cascade='all, delete-orphan'
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}"

# class User(Base):
#     __tablename__ = "user_account"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     fullname: Mapped[Optional[str]]
#     addresses: Mapped[List["Address"]] = relationship(
#         back_populates="user", cascade="all, delete-orphan"
#     )
#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

# class Address(Base):
# # ✅ 2. List["Address"] nima?

# # Bu — relationshipning ko‘plik (one-to-many) ekanini bildiradi.

# # Ya’ni:

# # Bitta User ko‘p Addresslarga ega bo‘lishi mumkin.

# # SQL darajasida:

# # user → one

# # address → many
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

#     user: Mapped["User"] = relationship(back_populates="addresses")
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"
