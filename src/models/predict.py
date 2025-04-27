import pickle
import numpy as np
import os
from src.utils.logger import get_logger

logger = get_logger(__name__)

# 모델 경로
MODEL_PATH = "save_models/kmeans_model.pkl"

def load_model():
    """
    저장된 K-Means 모델을 로드하는 함수
    """
    if not os.path.exists(MODEL_PATH):
        logger.error(f"!모델 파일 '{MODEL_PATH}'이(가) 존재하지 않습니다. 먼저 학습을 실행하세요.")
        raise FileNotFoundError(f"모델 파일을 찾을 수 없습니다: {MODEL_PATH}")

    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

    return model

def predict_cluster(total_quantity, avg_unit_price, num_purchases):
    """
    새로운 고객 데이터에 대한 클러스터 예측 수행
    """
    model = load_model()
    features = np.array([[total_quantity, avg_unit_price, num_purchases]])
    cluster = model.predict(features)[0]

    logger.info(f"!예측 결과: 고객은 {cluster}번 클러스터에 속함")
    return cluster

if __name__ == "__main__":
    cluster = predict_cluster(total_quantity=30, avg_unit_price=3.5, num_purchases=5)
    print(f"!예측된 클러스터: {cluster}")