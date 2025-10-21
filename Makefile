init: 
	python main.py init-db --db ./insurance.db

run:
	uvicorn insurance.interfaces.api:app --host 0.0.0.0 --port 8000

test:
	pytest tests/ -v

docker:
	docker build -t insurance_app .
	docker run -p:8000:8000 insurance_api