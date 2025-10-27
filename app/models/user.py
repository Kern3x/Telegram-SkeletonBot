from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.db_manager import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(Integer, unique=True, index=True, nullable=False)
    name: Mapped[str | None] = mapped_column(String(128))
