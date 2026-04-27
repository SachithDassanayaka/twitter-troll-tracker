import pickle
from src.features import load_vectorizer
import os

MODEL_PATH = os.getenv("MODEL_PATH", "models/model.pkl")

def predict(text):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    vec = load_vectorizer()
    X = vec.transform([text])
    return model.predict(X)[0]
    
if __name__ == "__main__":
    sample_text = "We provide live news updates about BLM violations"
    result = predict(sample_text)
    print("Prediction:", result)
       
