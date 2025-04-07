# 고객 클러스터링 API (FastAPI + Dask + ML)

## 설치

git clone <your-repo>
cd <project-dir>
python -m venv venv
source venv/bin/activate  # 윈도우: venv\Scripts\activate
pip install -r requirements.txt

도커 이미지 빌드
docker build -t bigdata-clustering .

컨테이너 실행
docker run -p 8000:8000 bigdata-clustering

서버 실행
uvicorn main:app --reload

Swagger
http://127.0.0.1:8000/docs

데이터 샘플 확인
curl -X GET http://127.0.0.1:8000/load_data

모델 학습 요청
curl -X POST http://127.0.0.1:8000/train

예측 실행
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"total_quantity\": 200, \"avg_unit_price\": 4.5, \"num_purchases\": 25}"
