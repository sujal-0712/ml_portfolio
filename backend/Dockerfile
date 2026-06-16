# Use the standard slim python image directly to bypass registry namespace bugs
FROM python:3.12-slim AS builder

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1

# Install curl cleanly so we can pull the official installer binary directly from Astral's servers
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Download and run the standalone uv installation script securely
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && cp /root/.local/bin/uv /bin/uv

COPY requirements.txt .

# Use our bootstrapped uv binary to sync packages into the system space
RUN --mount=type=cache,target=/root/.cache/uv \
    /bin/uv pip install --system -r requirements.txt

# Minimal production execution stage
FROM python:3.12-slim

WORKDIR /app

# Copy the completely built packages from the builder stage over
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]