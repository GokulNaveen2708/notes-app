from datetime import datetime, timezone

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(1000))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=now_utc)