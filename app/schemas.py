from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


# What the user is ALLOWED to send in.
class NoteCreate(BaseModel):
    content: str = Field(min_length=1, max_length=1000)


# What we send back OUT to the user.
class NoteRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    content: str
    created_at: datetime