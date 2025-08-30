# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install UV package manager
RUN pip install uv

# Copy dependencies
COPY pyproject.toml .

# Install project dependencies
RUN uv sync

# Copy application code
COPY app/ app/

# Expose port 8000
EXPOSE 8000

# Run app with uvicorn
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]