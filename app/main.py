#Entry point of backend.
from fastapi import FastAPI
from app.config import books
from app.models import Book
from typing import List

app = FastAPI(title="Quillstack Bookstore")

@app.get("/")
def root():
    return {"message": "BookStore API is running!"}

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.post("/books")
def add_book(book: Book):
    books.append(book.model_dump()) #Use model_dump()) instead of dict()
    return {"message": "book added successfully", "book": book}