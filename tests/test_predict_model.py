from src.models.predict import predict_cluster

def test_predict_cluster():
    # 예시 입력값
    total_quantity = 20.0
    avg_unit_price = 3.5
    num_purchases = 5

    result = predict_cluster(total_quantity, avg_unit_price, num_purchases)
    assert isinstance(result, int)
    assert 0 <= result < 5  # 클러스터 수가 5인 경우