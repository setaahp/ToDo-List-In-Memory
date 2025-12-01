# Dockerfile
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy project dependency files
COPY pyproject.toml poetry.lock* /app/

# Install Poetry
RUN pip install --no-cache-dir poetry

# Disable virtualenv creation and install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy all project files
COPY . /app/

# Default command (can be overridden by docker-compose)
CMD ["python", "main.py", "interactive"]
