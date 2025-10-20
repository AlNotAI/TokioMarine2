# Insurance API Demo

A minimal example GET API for a technical demonstration at TokioMarine. The service exposes a small insurance policy API intended for demonstration and discussion.

## Highlights
- FastAPI-based ASGI app
- Example domain model: InsurancePolicy
- Simple GET endpoints for demo purposes

## Project setup (editable / development)
This project is configured for editable installs using setuptools via pyproject.toml. Run the following from the project root (where this README and pyproject.toml live):

```bash
cd /Users/alexanderwong/TokioMarine/insurance_app
python -m pip install -U pip setuptools wheel
pip install -e .
```

Notes:
- The editable install puts the package named `insurance` on your PYTHONPATH so imports like `from insurance.domain.policy import ...` work in tests and the app.
- If you prefer not to install, you can run tests or the app with the repo root on PYTHONPATH:
  ```bash
  PYTHONPATH=. pytest -q
  PYTHONPATH=. uvicorn insurance.interfaces.api:app --reload
  ```
- If pip complains about editable mode, ensure setuptools is up-to-date (see the first command above). As an alternative you can add a minimal setup.cfg (legacy) — see project maintainers for that option.

## Quickstart (local)
1. Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies (editable install recommended):
   ```sh
   python -m pip install -U pip setuptools wheel
   pip install -e .
   pip install -r requirements.txt
   ```
3. Run the FastAPI app:
   ```sh
   uvicorn insurance.interfaces.api:app --reload --host 0.0.0.0 --port 8000
   ```
4. Example request:
   ```sh
   curl http://localhost:8000/policies
   ```

## Quickstart (Docker)
Build and run the container:
```sh
docker build -t insurance-api .
docker run -p 8000:8000 insurance-api
```

## Run tests
Run the test suite with pytest:
```sh
pytest -q
```

## Project layout
- insurance/ — application package
  - domain/ — domain models (e.g. InsurancePolicy)
  - interfaces/ — FastAPI endpoints and ASGI app
  - infrastructure/ — persistence and infra adapters
  - application/ — use cases and services
- tests/ — unit and integration tests

## Notes for the demo
- Focus discussion on the domain model validation, API design, and testing strategy.
- Bring up trade-offs for error handling, validation, and deployment.