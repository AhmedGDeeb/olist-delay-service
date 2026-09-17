"""Inference pipeline — loads fitted objects and predicts.

Placeholder implementation: uses a dummy model and identity preprocessor
so the FastAPI service and tests can run before real artifacts exist.
"""

import pandas as pd

from src.features.build_features import create_features


class ModelPredictor:
    """Loads saved model + preprocessor and predicts on raw input."""

    def __init__(self, config: dict | None = None):
        # In the real version, load from config['model'][...] paths.
        # For the scaffold, we use a trivial in-memory "model".
        self._is_scaffold = True

    def predict(self, raw_df: pd.DataFrame) -> dict:
        """Return a dict with predictions and probabilities (placeholder)."""
        df = create_features(raw_df)
        n = len(df)

        # Dummy output: everything predicted "on time" with 0.1 probability.
        return {
            "predictions": [0] * n,
            "probabilities": [0.1] * n,
        }
