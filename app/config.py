from fastapi import FastAPI #import fastAPI framework
from typing import List

app = FastAPI(title="Quillstack Bookstore")

books = [
    {"id": 1, "title": "The arcane Codex", "author": "A. Mage"},
    {"id": 2, "title": "DevOps Alchemy", "author": "B.Builder"},
]

@app.get("/")
def root():
    return {"message": "Bookstore API is running"}

@app.get("/books", response_model=List[dict])
def get_books():
    return books