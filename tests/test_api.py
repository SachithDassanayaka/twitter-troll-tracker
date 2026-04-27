from fastapi.testclient import TestClient
from api.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("src.predict.predict")
def test_predict(mock_predict):
    mock_predict.return_value = 1
    response = client.post("/predict", json={"text": "this is a troll"})
    assert response.status_code == 200
    assert response.json() == {"troll": True}