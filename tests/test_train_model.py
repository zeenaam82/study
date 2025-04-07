import os
from src.models.train import train_model, MODEL_PATH

def test_train_model_creates_file():
    data_path = "data/OnlineRetail.csv"
    train_model(data_path, n_clusters=3)
    assert os.path.exists(MODEL_PATH)