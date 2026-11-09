from fastapi import FastAPI, Response, HTTPException
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

@app.get("/notes/{note_id}")
def get_note_by_id(note_id: int):
    for note in notes:
        if note['id'] == note_id:
            return note

    raise HTTPException(status_code=404, detail="Note not found")

@app.head("/notes/{note_id}")
def head_note(note_id: int, response: Response):
    try:
        get_note_by_id(note_id)
    except HTTPException:
        response.status_code = 404
        return
    else:
        response.status_code = 200
        response.headers['x-note-exists'] = "true"


from typing import Optional
class NotePatch(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

@app.patch("/notes/{note_id}")
def update_note(note_id: int, new_item: NotePatch):
    curr_note = get_note_by_id(note_id)
    updated_data = new_item.model_dump(exclude_unset=True)
    curr_note.update(updated_data)

    return curr_note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    note_to_delete = get_note_by_id(note_id)
    notes.remove(note_to_delete)
    return Response(status_code=204)