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

############################
Problems solved.
Problem: Was trying to test WebApp running from local host but couldn't connect. Problem? main.py was within the /app dir not in the root folder hence the error.
Solution: just move main.py to root folder and then run --> uvicorn main:app --reload
