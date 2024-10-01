from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BOOLEAN

from . import Base


class Schedule(Base):
    __tablename__ = "schedule"

    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[str]
    group: Mapped[int]
    lesson_number: Mapped[int]
    subject: Mapped[str]
    classroom: Mapped[str]
    teacher: Mapped[str]
    numerator_denominator: Mapped[str] = mapped_column(nullable=True)
