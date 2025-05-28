FROM python:3.10-slim

# Avoid Python buffering and add system dependencies
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies for pip
RUN apt-get update && apt-get install -y build-essential

# Copy source code
COPY . /services

# Install Python dependencies
RUN pip install --upgrade pip \
 && pip install fastapi uvicorn

# Expose port
EXPOSE 8001

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
