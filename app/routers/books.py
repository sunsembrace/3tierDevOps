# app/routers/books.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.schemas import Book
from app.config import books

router = APIRouter()

@router.get("/", response_model=List[Book])
def get_books():
    return books

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.post("/", response_model=Book)
def add_book(book: Book):
    books.append(book.model_dump())
    return book

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books[i] = updated_book.model_dump()
            return books[i]
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(i)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
