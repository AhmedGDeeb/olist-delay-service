"""Tests for feature engineering (scaffold)."""

import pandas as pd

from src.features.build_features import create_features, create_label


def test_create_label_returns_dataframe():
    df = pd.DataFrame({"a": [1, 2, 3]})
    result = create_label(df)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 3


def test_create_features_returns_dataframe():
    df = pd.DataFrame({"a": [1, 2, 3]})
    result = create_features(df)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 3
