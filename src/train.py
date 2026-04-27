import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from preprocess import load_and_preprocess
from src.features import fit_vectorizer

df = load_and_preprocess("data/tweets.csv")
X, vec = fit_vectorizer(df["clean_text"])
y = df.get("categories")  # add manually for training (1=troll, 0=normal)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)