from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_predict_eta_success():
    payload = {
        "distance_km": 5.0,
        "traffic_index": 5,
        "weather": 0,
        "is_peak": 1
    }
    response = client.post("/api/predict", json=payload)
    assert response.status_code == 200
    assert "predicted_eta_min" in response.json()

def test_predict_eta_invalid_data():
    # 测试非法数据：缺少字段
    payload = {"distance_km": 5.0}
    response = client.post("/api/predict", json=payload)
    assert response.status_code == 422