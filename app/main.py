#Entry point of backend.
from fastapi import FastAPI, HTTPException
from app.config import books
from app.schemas import Book
from typing import List

app = FastAPI(title="Quillstack Bookstore")

@app.get("/")
def root():
    return {"message": "BookStore API is running!"}

@app.get("/books", response_model=List[Book])
def get_books():
    return books

#Add a book.
@app.post("/books")
def add_book(book: Book):
    books.append(book.model_dump()) #Use model_dump()) instead of dict()
    return {"message": "book added successfully", "book": book}

#Check by book ID.
@app.post("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

#Update a book.
@app.put("/book/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book:Book):
    for i, book in enumerate(books):
        if book ["id"] == book_id:
            books[i] = updated_book.model_dump() #replace old book.
            return books[i]
    raise HTTPException(status_code=404, detail="Book not found")