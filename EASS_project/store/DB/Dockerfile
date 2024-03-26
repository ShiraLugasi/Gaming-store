FROM python:3.10-slim AS builder

WORKDIR /shira

COPY versions.txt .
RUN pip install -r versions.txt



FROM postgres:latest

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=postgres

COPY --from=builder /shira /shira

EXPOSE 5432





