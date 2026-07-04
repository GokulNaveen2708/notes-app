from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import NoteCreate, NoteRead
from app import messaging, repository

router = APIRouter()


# Save a note:  POST /notes
@router.post("/notes", response_model=NoteRead, status_code=201)
def create_note(payload: NoteCreate, db: Session = Depends(get_db)):
    note = repository.create_note(db, payload)
    messaging.publish_note_created(note.id, note.content)
    return note

# List notes:  GET /notes
@router.get("/notes", response_model=list[NoteRead])
def list_notes(db: Session = Depends(get_db)):
    return repository.list_notes(db)