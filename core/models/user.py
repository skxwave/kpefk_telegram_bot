from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BOOLEAN

from . import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    telegram_id: Mapped[int] = mapped_column(nullable=False)
    group: Mapped[int] = mapped_column(nullable=True)
    is_admin: Mapped[bool] = mapped_column(default="False", server_default="False")
