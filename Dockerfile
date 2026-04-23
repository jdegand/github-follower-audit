FROM python:3.11-slim

# Create app directory
WORKDIR /app

# Copy dependency list first (cache-friendly)
COPY requirements.txt .
# COPY requirements-dev.txt .

# Install Python dependencies - Add -r requirements-dev.txt for tests
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command
CMD ["python", "run.py"]
