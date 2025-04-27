import os
import pickle
from sklearn.cluster import KMeans
from src.data.load_data import load_dataset
from src.utils.logger import get_logger

logger = get_logger(__name__)

# 모델 저장 경로
MODEL_PATH = "save_models/kmeans_model.pkl"

def train_model(data_path, n_clusters=5):
    """
    K-Means 클러스터링 모델을 학습하고 저장하는 함수
    """
    # 데이터 로드
    data = load_dataset(data_path)

    if hasattr(data, "to_legacy_dataframe"):
        data = data.to_legacy_dataframe()

    if hasattr(data, "compute"):
        data = data.compute()

    # CustomerID 기준으로 집계된 피처 생성
    features = data.groupby("CustomerID").agg({
        "Quantity": "sum",
        "UnitPrice": "mean",
        "InvoiceNo": "count"
    }).rename(columns={
        "Quantity": "TotalQuantity",
        "UnitPrice": "AvgUnitPrice",
        "InvoiceNo": "NumPurchases"
    }).dropna()

    # K-Means 학습
    model = KMeans(n_clusters=n_clusters, random_state=42)
    model.fit(features)

    # 모델 저장
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)

    logger.info(f"!모델 학습 완료! 모델이 {MODEL_PATH}에 저장됨.")

if __name__ == "__main__":
    train_model("data/OnlineRetail.csv")