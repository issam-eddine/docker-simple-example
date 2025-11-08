# docker-simple-example

Based on current best practices, here is a complete short project to demonstrate Docker with a basic scikit-learn machine learning example:

## Project Structure

Create a new folder for your project and set up the following files:

```
docker-simple-example/
├── model.py
├── requirements.txt
└── Dockerfile
```

## Step 1: Create the Python ML Script

Create a file called `model.py` that trains a simple classifier and saves the model:

```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model():
    # Load dataset
    data = load_iris()
    X, y = data.data, data.target
    
    # Train model
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X, y)
    
    # Save the trained model
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("✓ Model trained and saved as model.pkl")
    
    # Make a prediction
    sample = [[5.1, 3.5, 1.4, 0.2]]
    prediction = model.predict(sample)
    print(f"✓ Prediction for {sample}: {prediction[0]}")

if __name__ == '__main__':
    train_model()
```

## Step 2: Create requirements.txt

Create a `requirements.txt` file with the necessary dependencies:

```
scikit-learn==1.3.2
numpy==1.24.3
```

## Step 3: Create the Dockerfile

Create a file named `Dockerfile` (no extension):

```dockerfile
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
```

## Step 4: Build the Docker Image

Open Terminal and navigate to your project directory, then run:

```bash
docker build -t simple-example .
```

This command builds an image named `simple-example` using the Dockerfile in the current directory.

## Step 5: Run the Docker Container

Execute the container with:

```bash
docker run simple-example
```

You should see output like:

```
✓ Model trained and saved as model.pkl
✓ Prediction for [[5.1, 3.5, 1.4, 0.2]]: 0
```

## Verify it Works

To confirm Docker is working correctly, run these additional commands:

```bash
# List all images
docker images

# List running containers
docker ps -a

# Get image details
docker inspect simple-example
```

## Remove Container(s) and Image

```bash
docker stop $(docker ps -a -q -f ancestor=simple-example)
docker rm $(docker ps -a -q -f ancestor=simple-example)
docker rmi simple-example
```

## Why This Demonstrates Docker

This project shows how Docker **packages your entire environment** (Python 3.11, scikit-learn, numpy) into a self-contained unit that runs consistently regardless of your system. When someone runs the same image on another Mac or Linux machine, they get identical results without dependency conflicts.

