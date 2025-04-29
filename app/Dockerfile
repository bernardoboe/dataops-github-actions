FROM python:3.11-slim

WORKDIR /app

COPY conecta_postgres.py .

RUN pip install psycopg2-binary flask flask-restx gunicorn

CMD ["gunicorn","--bind", "0.0.0:5000","connecta_postgres:app"]

