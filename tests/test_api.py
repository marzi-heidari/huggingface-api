"""
Unit tests for HuggingFace Inference API.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_healthcheck_predict_valid_input():
    """
    Test /predict endpoint with valid input.
    """
    payload = {"text": "The service was outstanding and fast!"}
    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "result" in response.json()
    assert isinstance(response.json()["result"], list)
    assert "label" in response.json()["result"][0]
    assert "score" in response.json()["result"][0]


def test_predict_missing_text_field():
    """
    Test /predict endpoint with missing 'text' key.
    """
    payload = {}  # missing 'text'
    response = client.post("/predict", json=payload)

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"][-1] == "text"


def test_predict_empty_text_string():
    """
    Test /predict endpoint with empty input string.
    """
    payload = {"text": ""}
    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    result = response.json()["result"][0]
    assert result["label"] in ["POSITIVE", "NEGATIVE"]
    assert 0.0 <= result["score"] <= 1.0


@pytest.mark.parametrize("text", [
    "I love it.",
    "I hate this.",
    "It was okay.",
    "This product is garbage.",
    "Absolutely wonderful!"
])
def test_predict_multiple_inputs(text):
    """
    Parameterized test for different input sentiments.
    """
    response = client.post("/predict", json={"text": text})

    assert response.status_code == 200
    result = response.json()["result"][0]
    assert result["label"] in ["POSITIVE", "NEGATIVE"]
    assert 0.0 <= result["score"] <= 1.0
