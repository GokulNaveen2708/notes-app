from database import engine, SessionLocal, Base
from models import Note
from schemas import NoteCreate
import repository

Base.metadata.create_all(bind=engine)
db = SessionLocal()

repository.create_note(db, NoteCreate(content='first note'))
repository.create_note(db, NoteCreate(content='second note'))

for n in repository.list_notes(db):
    print('  id=', n.id, ' content=', n.content)

db.close()