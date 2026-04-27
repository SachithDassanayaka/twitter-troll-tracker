import pandas as pd
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text.strip()

def load_and_preprocess(path):
    df = pd.read_csv(path)
    df["clean_text"] = df["user_profile_description"].apply(clean_text)
    return df