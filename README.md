# Insurance API Demo

A minimal example GET API for a technical demonstration at TokioMarine. The service exposes a small insurance policy API intended for demonstration and discussion.

## Highlights
- FastAPI-based ASGI app
- Pydantic domain model: InsurancePolicy
- Simple GET endpoints for demo purposes
- Small SQLite-based demo datastore + CLI to initialize it

## Project setup (editable / development)
This project is configured for editable installs using setuptools via pyproject.toml. Run the following from the project root (where this README and pyproject.toml live):

Install tooling and the package in editable mode (recommended):
```bash
cd /Users/alexanderwong/TokioMarine/insurance_app
python -m pip install -U pip setuptools wheel
pip install -e .
pip install -r requirements.txt   # if you use requirements.txt
```

Notes:
- The editable install puts the package named `insurance` on your PYTHONPATH so imports like `from insurance.domain.policy import ...` work in tests and the app.
- If you prefer not to install, you can run tests or the app with the repo root on PYTHONPATH:
  ```bash
  PYTHONPATH=. pytest -q
  PYTHONPATH=. uvicorn insurance.interfaces.api:app --reload
  ```
- If pip complains about editable mode, ensure setuptools is up-to-date (see the first command above). As an alternative you can add a minimal setup.cfg (legacy) — see project maintainers for that option.


## Quickstart (local / development)

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies (editable install recommended):
   ```bash
   python -m pip install -U pip setuptools wheel
   pip install -e .
   pip install -r requirements.txt
   ```
3. Initialize the database:
   ```bash
   # from project root
   PYTHONPATH=. python -m insurance.interfaces.cli init-db --db ./insurance.db

   # or with recreate (drops and recreates table)
   PYTHONPATH=. python -m insurance.interfaces.cli init-db --db ./insurance.db --recreate

   # or via Makefile
   PYTHONPATH=. make init
   ```

   You can verify the database contents with:
   ```bash
   sqlite3 ./insurance.db ".tables"
   sqlite3 ./insurance.db "SELECT COUNT(*) FROM insurance_policies;"
   ```

4. Run the FastAPI app:
   ```bash
   uvicorn insurance.interfaces.api:app --reload --host 0.0.0.0 --port 8000

   # or via Makefile
   make run
   ```

5. Example request:
   ```bash
   curl http://localhost:8000/policies

   ```

## Quickstart (Docker)
Build and run the container:
```bash
docker build -t insurance-api .
docker run -p 8000:8000 insurance-api
```

## Run tests
Run the test suite with pytest:
```bash
pytest -q
```

## Run The Frontend (optional)
A minimal frontend is provided for demonstration purposes. To run the frontend:
1. Navigate to the `client` directory:
   ```bash
   cd client
   python -m http.server 3000  # or use any static file server

   ```

2. Open your browser and go to `http://localhost:3000/insurance_viewer.html` to view the frontend.


## Project layout
- insurance/ — application package
  - domain/ — domain models (e.g. InsurancePolicy)
  - interfaces/ — FastAPI endpoints and CLI
  - infrastructure/ — persistence and SQL helpers
  - application/ — use cases and services
- tests/ — unit and integration tests
- .env — local environment values (INSURANCE_DB_PATH)
- Makefile — convenience shortcuts (init, run, test)

## Dependencies
- FastAPI
- Uvicorn
- Pydantic
- SQLite3
- pytest

## Testing
The project includes unit and integration tests using pytest. To run the tests, execute:
```bash
pytest -q
```
## API details & JSON output
Endpoints:
GET /api/policies/ — list policies
GET /api/policies/{uuid} — single policy
To ensure responses are valid JSON:
The API normalizes DB rows / Pydantic models into JSON-serializable dicts.
You can enable FastAPI response_model to validate outputs. 

## CORS
If accessing the API from a different origin (e.g., frontend running on a different port),
CORS middleware has been added to allow cross-origin requests.
Add the following to insurance/interfaces/api.py:
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)     


## Usefule Commands Summary
# project root
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip setuptools wheel
pip install -e .
pip install -r requirements.txt   # optional

# init DB
PYTHONPATH=. python -m insurance.interfaces.cli init-db --db ./insurance.db
# run
PYTHONPATH=. uvicorn insurance.interfaces.api:app --reload
# tests
PYTHONPATH=. pytest -q
# make targets
PYTHONPATH=. make init
PYTHONPATH=. make run
PYTHONPATH=. make test