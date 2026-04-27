# Twitter Troll Tracker

## Project Overview
This project detects trolls and malicious accounts on Twitter/X using Natural Language Processing (NLP) and machine learning models. The pipeline covers data collection, preprocessing, feature engineering, model training, prediction, and deployment using FastAPI.

##Features
- Collect tweets from Twitter/X using Tweepy API
- Preprocess text data (cleaning, tokenization)
- Feature extraction using TF-IDF
- Train a RandomForest classifier to detect trolls
- Expose predictions via FastAPI REST API
- Unit tests with mocked model for CI
- GitHub Actions CI workflow for automated testing

## Setup
1. Create virtual env: `python -m venv venv`
2. Activate: `source venv/bin/activate`
3. Install: `pip install -r requirements.txt`

##Folder Structure
```text
twitter-troll-tracker/
│
├── api/
│   ├── main.py
│   └── schemas.py
│
├── src/
│   ├── predict.py
│   ├── features.py
│   └── train.py
│
├── models/
│   └── model.pkl (NOT committed to git in production)
│
├── tests/
│   └── test_api.py
│
├── requirements.txt
├── .gitignore
├── README.md
├── Dockerfile
└── .github/
    └── workflows/
        └── ci.yml
```

## Run API
```bash
uvicorn api.main:app --reload