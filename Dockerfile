# Use a slim Python 3.11 image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ML script into the container
COPY model.py model.py

# Run the model training script
CMD ["python", "model.py"]
