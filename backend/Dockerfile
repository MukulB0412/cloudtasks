# ✅ Correct Dockerfile format
FROM python:3.11-slim

WORKDIR /app

# Step 1: Copy requirements first
COPY requirements.txt .

# Step 2: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 3: Copy FastAPI app code
COPY ./app ./app

# Step 4: Run Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
