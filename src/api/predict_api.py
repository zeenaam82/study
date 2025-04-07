from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator
from src.models.predict import predict_cluster

predict_router = APIRouter()

class CustomerData(BaseModel):
    total_quantity: float = Field(..., ge=0, description="총 구매 수량")
    avg_unit_price: float = Field(..., ge=0, description="평균 단가")
    num_purchases: int = Field(..., ge=1, description="구매 횟수")

    @field_validator("avg_unit_price")
    def check_price(cls, v):
        if v > 10000:
            raise ValueError("avg_unit_price 값이 너무 큽니다.")
        return v

@predict_router.post("/predict")
def predict(data: CustomerData):
    """
    고객 데이터를 입력받아 클러스터를 예측하는 API
    """
    try:
        cluster = predict_cluster(
            data.total_quantity,
            data.avg_unit_price,
            data.num_purchases
        )
        return {"cluster": cluster}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"예측 중 오류 발생: {str(e)}")