from fastapi import APIRouter, HTTPException
from src.models.train import train_model

train_router = APIRouter()

@train_router.post("/train")
def train():
    """
    K-Means 모델을 학습시키는 API
    """
    try:
        data_path = "data/OnlineRetail.csv"
        train_model(data_path)
        return {"message": "모델 학습 완료!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"모델 학습 중 오류 발생: {str(e)}")