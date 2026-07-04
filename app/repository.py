from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models import Note
from app.schemas import NoteCreate


# Save a new note and return it.
def create_note(db: Session, note_in: NoteCreate) -> Note:
    note = Note(content=note_in.content)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


# Get all notes, newest first.
def list_notes(db: Session) -> list[Note]:
    stmt = select(Note).order_by(Note.created_at.desc())
    return list(db.execute(stmt).scalars().all())