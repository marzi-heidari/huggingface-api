from transformers import pipeline, Pipeline
from typing import List
import logging

# Setup logging
logger = logging.getLogger("uvicorn.error")

try:
    classifier: Pipeline = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )
except Exception as e:
    logger.exception("Failed to load model pipeline")
    raise RuntimeError("Model failed to load") from e


def predict(text: str) -> List[dict]:
    """
    Run sentiment prediction on input text with error handling.

    Args:
        text (str): Input text for inference.

    Returns:
        List[dict]: List of predictions with label and score.

    Raises:
        ValueError: If input is invalid.
        RuntimeError: If inference fails.
    """
    if not isinstance(text, str) or text.strip() == "":
        raise ValueError("Input must be a non-empty string.")

    try:
        return classifier(text)
    except Exception as e:
        logger.exception("Inference failed.")
        raise RuntimeError("Inference pipeline failed.") from e
