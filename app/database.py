from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

# 1. The engine: the actual connection to the database.
engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False},  # needed for SQLite only
)

# 2. A factory that hands out a fresh "session" whenever we ask.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# 3. A base blueprint that our table will build on (used in Piece 4).
Base = declarative_base()


# 4. Hand out a session, then always close it when the work is done.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()