"""
FastAPI application exposing RESTful endpoints for text inference.

Includes a `/predict` endpoint that accepts POST requests and returns sentiment predictions.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.model import predict

app = FastAPI(
    title="HuggingFace Sentiment Analysis API",
    description="A scalable inference service for HuggingFace transformer models.",
    version="1.0.0"
)

class InferenceRequest(BaseModel):
    text: str = Field(..., example="The product was excellent and exceeded expectations.")

class InferenceResponse(BaseModel):
    result: list

@app.post("/predict", response_model=InferenceResponse)
async def run_inference(request: InferenceRequest):
    """
    POST endpoint for model inference.

    Args:
        request (InferenceRequest): JSON body containing the input text.

    Returns:
        InferenceResponse: JSON containing model predictions.
    """
    output = predict(request.text)
    return {"result": output}
