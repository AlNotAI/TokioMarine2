FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "insurance.interfaces.api:app", "--host", "localhost", "--port", "8000"]
