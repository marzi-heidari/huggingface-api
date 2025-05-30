"""
Model management and inference module.

This module loads the HuggingFace sentiment analysis pipeline and exposes a callable
function to perform inference on input strings.
"""

from transformers import pipeline
from typing import List

# Initialize pipeline once during startup
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def predict(text: str) -> List[dict]:
    """
    Run sentiment analysis on the provided input text.

    Args:
        text (str): The input text to analyze.

    Returns:
        List[dict]: A list containing the prediction label and confidence score.
    """
    return classifier(text)
