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
