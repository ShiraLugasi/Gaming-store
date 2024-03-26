FROM python:3.10-slim

WORKDIR /app

COPY versions.txt /app/

RUN pip install --no-cache-dir -r versions.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


