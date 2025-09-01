1. Create git Repos and then link it.

2. Create venv (virtual environment).
why? 
Isolated dependencies - prevents conflicts with other python projects or system packages.
Reproducibility - Makes it easier to share your project with others/deploy it.
Clean start - ensures your libraries you install are only for this project.

How to do it?
cd path/to/3tierDevOps

--> python -m venv venv

--> .\venv\Scripts\Activate

is a success if you see "(venv) PS C:\Users\squid\Downloads\VSCselfprojects2025\3TierDevOps>"

venv/ --> paste into .gitignore so we dont push virtual environment.

note: venv is common name for environment folder, can call it anything.

#Starting project
3. Starting the BackEnd skeleton.
Pros:

Modern and fast: Uses async by default → better for APIs that handle many requests.

Type hints: Pydantic models let you validate data automatically.

Auto docs: Swagger UI and Redoc are generated automatically.

Popular for microservices: Many startups, cloud services, and newer teams use it.

Lightweight: Less “magic” than Django—good for learning how things work.

Cons:

Not as “full-featured” for big monolith apps.

Less built-in admin/dashboard (you’d use external tools).

3TierDevOps/
│
├─ venv/                  # your virtual environment (already done)
├─ app/                   # main application folder
│   ├─ __init__.py
│   ├─ main.py             # entry point of backend
│   ├─ config.py           # config settings like DB connection strings, environment variables
│   ├─ models.py           # data models (empty for now, will use DB later)
│   ├─ schemas.py          # request/response structures (for APIs)
│   └─ routes/             # folder for route definitions
│       ├─ __init__.py
│       └─ books.py        # endpoints for books
│
├─ tests/                  # later for unit tests
├─ requirements.txt        # track dependencies
└─ .gitignore              # exclude venv, __pycache__, etc.

3.1 Install FastAPI and Uvicorn.
--> pip install fastapi uvicorn
Why? FastAPI provides backend framework & Uvicorn provides server for running FastAPI.

Then freeze versions in requirements.txt
--> pip freeze > requirements.txt

Why? Makes project reproducible for other team members or deployment.

3.2 Create app/main.py.

Line 1: from fastapi import FastAPi
--> Imports mainFastAPI class
What it does: Imports the main FastAPI class.
Why we do it: FastAPI is the framework that handles routing, requests, responses, and documentation.
Thinking behind it: Every modern web API has a “central orchestrator” object—FastAPI is that for Python. We need it to initialize our app.

Line 2: app = FastAPI(title="3TierDevOps Bookstore")
What it does: Creates an instance of the FastAPI application.
Why we do it: This object represents your API. All routes, middleware, and configs attach to it.
Why we add title=: This gives your API a clear name for documentation. When you open http://127.0.0.1:8000/docs, you’ll see this title in the auto-generated Swagger UI.
Developer mindset: Always make your APIs self-documenting and clear from the start—real projects do this.

Line 3-6: Define a root route. 
--> @app.get("/") → decorator
What it does: Maps HTTP GET requests to the root URL /.
Why we do it: Every API should have a simple health check endpoint to confirm the server is running.
Thinking: Devs often add a “heartbeat” or “status” route early so other devs or deployment scripts can verify the API is live.

--> def root(): → function
What it does: The function that executes when someone hits /.
Why we do it: FastAPI routes always need a function handler. Think of it as the action that happens when the user calls the API.

--> return {"message": "Bookstore API is running!"} → response
What it does: Sends a JSON response back to the client.
Why we do it: APIs communicate with structured data (JSON is standard).
Mindset: Even for dummy data, it’s good to return meaningful JSON so frontend or other services can integrate easily later.

3.2 Test --> Test it works on localhost webapp & it does (problem solved).

3.3 Define book endpoint
API just confirms its running but a bookstore API needs functionality e.g returning books. Keeping data in-memory first, so i dont worry aboput database now.
Teaches me how to define multiple endpoints (/ vs books)
Using in-memory list like a minidatabase.
Adding type hints / response mopdels to simulate proper API contracts.
Testing fucntionality via url localhost link in browser.

--> from fastapi import FastAPI
--> from typing import List
What it does: Brings in FastAPI and type hints for lists.
Why we do it: Needed to create endpoints and document response types.
Mindset: Always import what you know you’ll need upfront; sets the 

--> app = FastAPI(title="QuillStack Bookstore")
What it does: Creates the FastAPI app object.
Why we do it: All endpoints attach to this app; title appears in Swagger docs.
Mindset: Initialize core objects before adding logic.

--> books = [
    {"id": 1, "title": "The Arcane Codex", "author": "A. Mage"},
    {"id": 2, "title": "DevOps Alchemy", "author": "B. Builder"}
]
What it does: Stores a list of book dictionaries.
Why we do it: Allows testing endpoints without a real database.
Mindset: Keep it simple first; focus on functionality before persistence.

--> @app.get("/")
def root():
    return {"message": "BookStore API is running!"}

What it does: Responds to / requests with a simple message.
Why we do it: Confirms the app is running; useful for debugging and health checks.
Mindset: Verify basics work before adding complexity.

--> @app.get("/books", response_model=List[dict])
def get_books():
    return books
What it does: Returns the list of books.
Why we do it: Provides the first “real” API resource to test retrieval.
Mindset: Build one feature at a time; start with reading data before writing or updating.

3.3 Test --> uvicorn app.main:app --reload
then go to http://127.0.0.1:8000/books 
Go to link and it should show the books list. because of our @app.get("/books") & the function get_books 

3.4 Make API interactive with structured data --> Create a Pydantic model & POST endpoint to add books dynamically.
Why? So far we only have a get /books which returns a static list. We need to add better functionality such as add, update and remove because REAL APIs let users interact with data and handle user input safely.

--> from pydantic import BaseModel
What it does: Lets us define data structures with type validation.
Why we do it: To ensure incoming data (like new books) has the correct shape.
Mindset: “Never trust raw input—validate it!”

--> class Book(BaseModel):
    id: int
    title: str
    author: str

What it does: Defines the structure of a book object.
Why we do it: Makes both input (POST) and output (GET) consistent.
Mindset: Think of it as the blueprint for every book in your app.

then back in main.py
--> from app.models import Book
Allows fastAPI to validate incoming data using Book model.

--> @app.post("/books")
def add_book(book: Book):
    books.append(book.model_dump()) #Use model_dump()) instead of dict()
    return {"message": "book added successfully", "book": book}

What it does: Defines a POST endpoint /books that takes a Book object from the request body, converts it to a dictionary using model_dump(), and appends it to the books list. Returns a success message along with the added book.
Why we do it: This allows the API to accept and store new books dynamically. Using model_dump() ensures the Pydantic Book object is converted to a plain dictionary that can be added to the in-memory list.
Mindset: Think in terms of CRUD operations. This is the Create step: validating input, adding it to storage, and providing feedback to the user in a structured, predictable way.

--> added resonse_model=List[Book]
What it does: List from typing defines the response type as a list of Book objects, so response_model=List[Book] tells FastAPI to validate and serialize each item against the Book schema.
Why we do it: Enforces type safety, ensures consistent response formatting, and auto-generates precise OpenAPI documentation.
Mindset: Always define response types explicitly to maintain strict data contracts between your API and its consumers.

3.4 Test --> run uvicorn app.main:app --reload
 and then check Swagger UI http://127.0.0.1:8000/docs then test post/books and see if you can enter date (works!!)
 
 3.5 Adjustment - Moved models.py content into schema.py for futuure database scalability and changed main.py to import from schema.py instead of models.py

 3.6 Get a Single Book by ID.
 --> @app.get("/books/{book_id}", response_model=Book)
What it does: Adds an endpoint /books/{book_id} that takes an ID from the URL, searches the books list for a match, and returns that book. If none is found, it raises an HTTPException with a 404 status.

Why we do it: This lets clients fetch a single resource instead of the whole collection. Using HTTPException ensures the API follows HTTP standards for missing resources, improving clarity and error handling.

Mindset: Think of it like a database lookup — every request should either return exactly what was asked for or give a clear, standard error so the client knows what went wrong.

3.6 Test --> run uvicorn app.main:app --reload
 and then check Swagger UI http://127.0.0.1:8000/docs then test post/books/{book_id} and see if you can enter id (works!!)

 3.7 Update a Book 
--> @app.put("/books/{book_id}", response_model=Book)

What it does: Replaces an existing book with new data.
Why we do it: Lets users modify book info safely by ID.
Mindset: Always validate existence before updating; maintain data consistency.

3.8 Delete a book.
--> @app.delete("/books/{book_id}")
What it does: Removes a book by its ID.
Why we do it: Enables safe deletion with feedback and error handling.
Mindset: Avoid silently failing operations; always confirm the action.

3.7& 3.8 test
--> uvicorn app.main:app --reload
--> http://127.0.0.1:8000/docs


3.9 - Refactorin/making more modular so moving all /book endpoints into routers/book.py
What it does: keeps main.py from getting messy and keeps it clean.
Why we do it: Better scalability.
Mindset: Organize early. Makes it ready for a database without rewriting endpoints.


3.10 Trying to test yet issue arose 
--> AttributeError: 'list' object has no attribute 'router'
This is because my book is currently a list, not a router object. FastAPI routers must be created using APIrouter().
Solution: from app.routers import books  # to include the router in main.py and remove the pre-existing libraries (except from fastapi import FastAPI) as they now lived in routers/books.py

3.11 Created DockerFile for app.
--> Installed Postgres dependency for integration later and saves us a headache.

3.12 - Created .dockerignore to avoid bloating when i make container.

Phase 2: DB integration.

4. Creating new files/folder structure for better modularity and created a docker-compose.yml file to run postgres + app together later. Created New SQLAlchemy book model, new Pydantic schema for book, and new crud function for book.

4.1 Install DB dependencies of SQLAlchemy with
pip install sqlalchemy psycopg2-binary
then pip freeze > requirements.txt
used pip freeze | findstr "sqlalchemy psycopg2-binary"
pip freeze > requirements.txt


4.2 Selfnote Had to recreate Venv midproejct as i had to get it off github again as PC wiped due to technical issues.



 #########################
Problems solved.
Problem: Was trying to test WebApp running from local host but couldn't connect. Problem? main.py was within the /app dir not in the root folder hence the error.
Solution: just move main.py to root folder and then run --> uvicorn main:app --reload

Problem: was using dict() when tryting to make a model but had to use newer version which is model_dump() to convert book model isntance into plaint dict to append into book list. FastAPI and pydantic v2 use model_dump() to avoid confusion with internal Pydantic methods.

Problem: Wanted to make it more robust on get_books in main.py
Added response_model=List[Book]
ensures GET return books in the correct format. 

Problem: Had to move models.py content to schemas.py (the pydantic model) as models.py is for future database scalability. 

Problem: in step 3.10 after moving functions into routers/book.py--> uvicorn app.main:app --reload wont work.
--> AttributeError: 'list' object has no attribute 'router'
This is because my book is currently a list, not a router object. FastAPI routers must be created using APIrouter().
Solution: from app.routers import books  # to include the router in main.py and remove the pre-existing libraries (except from fastapi import FastAPI) as they now lived in routers/books.py

Architectural decision problem: SO i initially stored data in a list with a dict? for testing purposes (but issue is data gets wiped for each run so we need a DB), so i was thinking SQLite for local testing and far faster as it runs as a file with no need for installation/configuration nor concerns about DB connection issues. However, I opt'd for PostgreSQL as its more production like and closer to real working environments and I can spend more time troubleshooting on this than changing from SQLite to PostgreSQL. This meant I had to make a docker for my app to run it later with postgreSQL in containers with a single docker-compose up.
Made dockerfile have postgres install dependency beforehand to avoid issues on adjusting it later. 


Architectural decision. Phase 2: DB integration.
Rationale for using ORMs like SQLAlchemy before PostGre

Why we don’t just “use PostgreSQL directly” with raw SQL

ORMs like SQLAlchemy provide a layer of abstraction

You define models in Python (Book class) instead of writing raw SQL queries for every operation.

Makes code cleaner, safer, and easier to maintain.

Junior+ engineers are expected to know ORMs in jobs; it’s a production best practice.

Consistency with your app structure

Right now, your FastAPI app works with Pydantic schemas.

SQLAlchemy models map nicely to schemas, so your endpoints can stay almost the same.

Portability & testing

You can switch DBs (SQLite, Postgres, MySQL) with minimal code changes.

Easier to test locally with SQLite before moving to Postgres container.

Handles migrations & relationships

Once you go multi-table or more complex logic, ORMs make it manageable.

Raw SQL can become messy and error-prone.

Phase 2 DB integration problems:
problem: Need to move CRUD logic with in-memory list to own crud file for DB integration later. 
This will help us integrate postgreSQL later so we dont have to refactor everything again.