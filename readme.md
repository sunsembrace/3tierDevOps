1. Create git Repos and then link it.

2. Create venv (virtual environment).
why? 
Isolated dependencies - prevents conflicts with other python projects or system packages.
Reproducibility - Makes it easier to share your project with others/deploy it.
Clean start - ensures your libraries you install are only for this project.

How to do it?
cd path/to/3tierDevOps

python -m venv venv

.\venv\Scripts\Activate

is a success if you see "(venv) PS C:\Users\squid\Downloads\VSCselfprojects2025\3TierDevOps>"

venv/ --> paste into .gitignore so we dont push virtual environment.

note: venv is common name for environment folder, can call it anything.

#Starting project
3. Starting the BackEnd skeleton.
Chose FastAPI as my Python Framework as its more modern, job-friendly and easy to expand into APIs.

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
