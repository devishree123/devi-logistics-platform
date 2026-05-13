FROM python:3.12-slim

WORKDIR /app

# Copy dependency file first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy full project
COPY . .

EXPOSE 8080

CMD ["uvicorn", "ai_api:app", "--host", "0.0.0.0", "--port", "8080"]