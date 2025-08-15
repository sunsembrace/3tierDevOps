#Entry point of backend.
from fastapi import FastAPI
from app.routers import books  # to include the router

app = FastAPI(title="Quillstack Bookstore")

app.include_router(books.router,prefix="/books",tags=["Books"])

@app.get("/")
def root():
    return {"message": "BookStore API is running!"}
