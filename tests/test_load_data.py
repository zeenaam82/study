import os
from src.data.load_data import load_dataset

def test_load_dataset():
    file_path = "data/OnlineRetail.csv"
    df = load_dataset(file_path)

    assert df is not None
    assert hasattr(df, "columns")