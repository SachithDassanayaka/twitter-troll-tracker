import pickle
from features import load_vectorizer

def predict(text, model_path="models/model.pkl"):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    vec = load_vectorizer()
    X = vec.transform([text])
    return model.predict(X)[0]
    
if __name__ == "__main__":
    sample_text = "This is a troll message"
    result = predict(sample_text)
    print("Prediction:", result)
       
