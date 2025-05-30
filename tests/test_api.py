"""
Unit tests for HuggingFace Sentiment Analysis API with error handling.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_predict_valid_input():
    """
    Test /predict with a valid sentence.
    Should return 200 and correct structure.
    """
    payload = {"text": "This product exceeded expectations!"}
    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.json()["result"][0]
    assert "label" in data and data["label"] in ["POSITIVE", "NEGATIVE"]
    assert "score" in data and 0.0 <= data["score"] <= 1.0


def test_predict_missing_text_field():
    """
    Test /predict with no 'text' key in payload.
    Should return 422 from FastAPI input validation.
    """
    payload = {}
    response = client.post("/predict", json=payload)

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"][-1] == "text"


def test_predict_empty_text():
    """
    Test /predict with empty string.
    Should return 400 with proper error message.
    """
    payload = {"text": ""}
    response = client.post("/predict", json=payload)

    assert response.status_code == 400
    assert "Input must be a non-empty string" in response.text


@pytest.mark.parametrize("bad_input", [None, 123, {}, [], True])
def test_predict_invalid_input_types(bad_input):
    """
    Test /predict with various non-string payloads.
    Should return 422 from FastAPI input validation (before reaching model).
    """
    response = client.post("/predict", json={"text": bad_input})
    assert response.status_code == 422



