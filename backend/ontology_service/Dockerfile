FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app
COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt
COPY backend /app/backend
WORKDIR /app/backend/ontology_service

CMD ["sh", "-c", "alembic upgrade head && python -m backend.ontology_service.app.seed && uvicorn backend.ontology_service.app.main:app --host 0.0.0.0 --port 8000"]
