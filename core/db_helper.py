from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy import select

from .config import settings
from core.models import User


class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
    ):
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


db_helper = DatabaseHelper(url=settings.db.url)


async def create_user(
    username: str,
    telegram_id: int,
):
    async with db_helper.session_factory() as session:
        user = User(
            username=username,
            telegram_id=telegram_id,
        )
        session.add(user)
        await session.commit()

    return user


async def find_user(telegram_id: int):
    async with db_helper.session_factory() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
    return user
