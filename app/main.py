"""
FastAPI application exposing RESTful endpoints for text inference.

Includes a `/predict` endpoint that accepts POST requests and returns sentiment predictions.
"""

from fastapi import FastAPI, HTTPException
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

@app.post(
    "/predict",
    response_model=InferenceResponse,
    summary="Run Sentiment Prediction",
    response_description="Predicted sentiment label and confidence score"
)
async def run_inference(request: InferenceRequest):
    """
    Perform sentiment analysis on input text using a pre-trained HuggingFace transformer model.

    ## Request Body
    - **text** (`str`): The input text to classify sentiment. Must be a non-empty English sentence.

    ## Responses
    - **200 OK**: Successfully returned sentiment prediction.
        - **result** (`list[dict]`): A list with one item, including:
            - **label** (`str`): Either `"POSITIVE"` or `"NEGATIVE"`
            - **score** (`float`): Confidence score between `0.0` and `1.0`
    - **400 Bad Request**: Returned if the input is invalid or empty.
    - **500 Internal Server Error**: Indicates model or inference failure.

    ## Example
    **Input**
    ```json
    {
        "text": "This product is excellent!"
    }
    ```

    **Output**
    ```json
    {
        "result": [
            {
                "label": "POSITIVE",
                "score": 0.9991
            }
        ]
    }
    ```

    ## Notes
    - This endpoint supports real-time inference and is optimized for low-latency responses.
    - It uses the `distilbert-base-uncased-finetuned-sst-2-english` model.
    """
    try:
        output = predict(request.text)
        return {"result": output}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except RuntimeError as re:
        raise HTTPException(status_code=500, detail=str(re))

