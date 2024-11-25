FROM python:3.10-slim

WORKDIR /app/api

COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential gcc libpq-dev \
	&& pip install -r requirements.txt \
	&& apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
