#Entry point of backend.
from fastapi import FastAPI
from app.config import books

app = FastAPI(title="Quillstack Bookstore")

@app.get("/")
def root():
    return {"message": "BookStore API is running!"}

@app.get("/books")
def get_books():
    return books