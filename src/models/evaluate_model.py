"""Placeholder — evaluation logic will go here later."""

import pandas as pd

from src.models.predict_model import ModelPredictor


def evaluate(X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    """Return a simple metrics dictionary. Placeholder implementation."""
    predictor = ModelPredictor()
    result = predictor.predict(X_test)
    n = len(result["predictions"])
    return {
        "n_samples": n,
        "note": "placeholder evaluation — replace with real metrics",
    }
