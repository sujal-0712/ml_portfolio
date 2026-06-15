# =====================================================================
# FASTAPI BACKEND MICROSERVICE DOCKERFILE (RUST-INSULATED NETWORK)
# =====================================================================
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

# Install system dependencies required for gradient boosting compilation
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements manifest
COPY requirements.txt .

# Swapping standard pip for the Rust-backed 'uv' engine.
# This prevents 'IncompleteRead' failures on large 300MB wheels.
RUN pip install --no-cache-dir uv && \
    uv pip install --system --no-cache -r requirements.txt

# Copy application layers and model binaries
COPY ./app ./app
COPY ./artifacts ./artifacts

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]