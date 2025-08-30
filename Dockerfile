# Use official Python base image
FROM python:3.12-slim AS development

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

# Create logs directory
RUN mkdir -p logs

# Expose port 8000
EXPOSE 8000

# Set default environment
ENV ENVIRONMENT=develpment

# Set the log level
ENV LOG_LEVEL=DEBUG

# Run app with uvicorn
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]