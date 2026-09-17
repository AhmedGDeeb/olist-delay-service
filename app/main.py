"""FastAPI inference service (scaffold)."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

from src.models.predict_model import ModelPredictor

app = FastAPI(
    title="Olist Delivery Delay Predictor",
    version="v0.0.0",
    description="Scaffold API for Task 3 — real model wired in later.",
)

predictor = ModelPredictor()


class Order(BaseModel):
    """Minimal order payload — expand fields when real model is wired in."""

    order_id: str
    customer_id: str
    order_purchase_timestamp: str


class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    model_version: str = "v0.0.0"


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/model/info")
def model_info() -> dict:
    return {"model_name": "scaffold", "version": app.version}


@app.post("/predict", response_model=PredictionResponse)
def predict_single(order: Order) -> PredictionResponse:
    try:
        df = pd.DataFrame([order.model_dump()])
        result = predictor.predict(df)
        return PredictionResponse(
            prediction=result["predictions"][0],
            probability=result["probabilities"][0],
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
