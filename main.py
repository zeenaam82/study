from fastapi import FastAPI, HTTPException
from src.api.train_api import train_router
from src.api.predict_api import predict_router
from src.data.load_data import load_dataset
from src.utils.logger import get_logger

logger = get_logger(__name__)
app = FastAPI()

# 라우터 등록
app.include_router(train_router)
app.include_router(predict_router)

@app.get("/load_data")
def load_data():
    """
    데이터셋을 로드하고 샘플 데이터를 반환하는 API
    """
    try:
        file_path = "data/OnlineRetail.csv"
        df = load_dataset(file_path)
        logger.info(f"df type: {type(df)}")

        if hasattr(df, "to_legacy_dataframe"):
            df = df.to_legacy_dataframe()

        df_sample = df.head(100)

        if hasattr(df_sample, "compute"):
            df_sample = df_sample.compute()
            
        return {"data": df_sample.to_dict(orient='records')}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))