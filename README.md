# 고객 클러스터링 API (FastAPI + Dask + ML)

## 개요
실제 전자상거래 데이터를 기반으로 고객을 유사한 그룹(클러스터)으로 분류하고, 새로운 고객 데이터가 들어올 경우 해당 고객이 어떤 그룹에 속하는지 예측할 수 있는 API를 개발한 프로젝트입니다.  
FastAPI 기반으로 RESTful API를 구현하며, 머신러닝(K-Means)을 활용하여 고객 유형을 파악합니다.

## 설치
1. git clone your-repo
2. cd project-dir
3. python -m venv venv
4. source venv/bin/activate  # 윈도우: venv\Scripts\activate
5. pip install -r requirements.txt

## 실행
-도커 이미지 빌드:
docker build -t bigdata-clustering .

-컨테이너 실행:
docker run -p 8000:8000 bigdata-clustering

-서버 실행:
uvicorn main:app --reload

-데이터 샘플 확인:
curl -X GET http://127.0.0.1:8000/load_data

-모델 학습 요청:
curl -X POST http://127.0.0.1:8000/train

-예측 실행:
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"total_quantity\": 200, \"avg_unit_price\": 4.5, \"num_purchases\": 25}"

-Swagger:
http://127.0.0.1:8000/docs
