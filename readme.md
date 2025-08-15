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

