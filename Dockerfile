FROM python:3.9-slim

WORKDIR /app/api

RUN apt-get update && apt-get install -y \
	build-essential \
	tesseract-ocr-por \
	cmake \
	git 

COPY . ./

RUN pip install -r requirements.txt
# RUN prisma generate
# RUN prisma migrate dev --name "init"

CMD ["uvicorn", "main:app", "--host","0.0.0.0", "--port", "8000"]
