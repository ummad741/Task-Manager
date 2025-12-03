from sqlalchemy import create_engine, text, String
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase, Mapped
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
# local files
from database.environments import SYNC_DSN, ASYNC_DSN
from database.fields import (str_30, str_50, intpk, created_at, updated_at)


engine_sync = create_engine(
    url=SYNC_DSN,
    echo=True,  # Sqlalchemy qilgan zaproslarni log qilib beradi
    pool_size=5,  # bazaga qanca ulanish mumkunligini belgilidi
    max_overflow=10  # yana qoshima zaproslar uchun connection bazaga

)

engine_async = create_async_engine(
    url=ASYNC_DSN,
    echo=True,  # bazaga bo'gan hamma zaproslarni log qilib beradi
)


class Base(DeclarativeBase):
    __abstract__ = True
    # python type hint sqlalchemy columnga automate map qilish
    # anotated strlarni
    type_anotation_map = {
        str_30: str_30,
        str_50: str_50
    }
    id: Mapped[intpk]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


session_factory = sessionmaker(engine_sync)
async_session_factory = async_sessionmaker(engine_async)
