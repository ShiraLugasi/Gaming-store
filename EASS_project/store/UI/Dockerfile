FROM python:3.9-slim

WORKDIR /UI

COPY . /UI

COPY . /store

COPY versions.txt .

RUN pip install -r versions.txt

CMD ["streamlit", "run", "ST.py"]