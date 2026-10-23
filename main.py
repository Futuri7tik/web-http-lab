from fastapi import FastAPI, Response
from fastapi.testclient import TestClient

app = FastAPI(title="Notes API", version="0.1.0")

@app.get("/health")
def get_health():
    return {"status": "ok"}

@app.get("/hello")
def get_hello():
    return {"message": "Hello from Notes API"}

