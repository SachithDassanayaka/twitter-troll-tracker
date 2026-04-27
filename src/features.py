from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def fit_vectorizer(texts, save_path="models/vectorizer.pkl"):
    vec = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
    X = vec.fit_transform(texts)
    with open(save_path, "wb") as f:
        pickle.dump(vec, f)
    return X, vec

def load_vectorizer(path="models/vectorizer.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)