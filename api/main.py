from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/predict")
def troll_prediction(data: InputData):
    result = predict(data.text)
    return {"troll": bool(result)}