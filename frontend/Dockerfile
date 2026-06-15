# =====================================================================
# FLASK FRONTEND MICROSERVICE DOCKERFILE
# =====================================================================
FROM python:3.12-slim

# Prevent Python from writing .pyc caching files and buffer streams
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

# Cache layer optimization: Install pip dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy server scripts and user interface HTML views into the container filesystem
COPY ./app ./app
COPY ./templates ./templates

# Open the production web interface port
EXPOSE 5000

# Execute Gunicorn binding to all interfaces on port 5000, using 4 execution workers
CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:5000", "app.server:app"]