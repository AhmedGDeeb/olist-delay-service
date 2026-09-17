"""Tests for the inference pipeline (scaffold)."""

import pandas as pd

from src.models.predict_model import ModelPredictor


def test_predictor_initializes():
    predictor = ModelPredictor()
    assert predictor is not None


def test_predict_returns_correct_shape():
    predictor = ModelPredictor()
    df = pd.DataFrame(
        {
            "order_id": ["a", "b", "c"],
            "customer_id": ["x", "y", "z"],
            "order_purchase_timestamp": ["2024-01-01"] * 3,
        }
    )
    result = predictor.predict(df)
    assert len(result["predictions"]) == 3
    assert len(result["probabilities"]) == 3


def test_predictions_are_binary():
    predictor = ModelPredictor()
    df = pd.DataFrame(
        {
            "order_id": ["a"],
            "customer_id": ["x"],
            "order_purchase_timestamp": ["2024-01-01"],
        }
    )
    result = predictor.predict(df)
    assert result["predictions"][0] in (0, 1)
    assert 0.0 <= result["probabilities"][0] <= 1.0
