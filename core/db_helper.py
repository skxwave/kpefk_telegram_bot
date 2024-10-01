from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy import select

from .config import settings
from core.models import User, Schedule


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


async def set_group(telegram_id: int, group: int):
    async with db_helper.session_factory() as session:
        user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        user.group = group
        await session.commit()
    return user


async def add_lesson(**kwargs):
    """
    Add a lesson to the schedule.

    Args:
        day (str): The day of the week (e.g., "Monday").
        group (int): The group number (e.g., 101).
        lesson_number (int): The order number of the lesson (e.g., 1, 2, 3...).
        subject (str): The subject of the lesson (e.g., "Math").
        classroom (str): The room where the lesson takes place (e.g., "101").
        teacher (str): The teacher's name (e.g., "Smith").
        numerator_denominator (str): Indicates if it's numerator or denominator (e.g., "numerator").
    """
    async with db_helper.session_factory() as session:
        existing_lesson = await session.scalars(select(Schedule).filter_by(**kwargs))
        if existing_lesson.first():
            return "Lesson exists"
        else:
            lesson = Schedule(**kwargs)
            session.add(lesson)
            await session.commit()
    return lesson


async def find_lessons(group: int, day: str):
    async with db_helper.session_factory() as session:
        lessons = await session.scalars(
            select(Schedule).filter(Schedule.group == group, Schedule.day == day)
        )

    return lessons
