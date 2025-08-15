#Entry point of backend.
from fastapi import FastAPI

app =FastAPI(title="Quillstack Bookstore")

@app.get("/")
def root():
    return {"message": "BookStore API is running!"}