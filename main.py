from fastapi import FastAPI, Response, status
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI(title="Notes API", version="0.1.0")

@app.get("/health")
def get_health():
    return {"status": "ok"}

@app.get("/hello")
def get_hello():
    return {"message": "Hello from Notes API"}

class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=80)
    content: str = Field(..., min_length=1, max_length=500)

notes = []
next_id = 1
@app.get('/notes')
def get_notes():
    return notes

@app.post("/notes", status_code=201)
def post_note(note: NoteCreate):
    note_to_add = note.model_dump()

    global next_id
    note_to_add['id'] = next_id
    next_id += 1
    notes.append(note_to_add)
    return note_to_add