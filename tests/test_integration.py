from app.main import predict_eta, PredictionInput

def test_model_prediction_reasonable():
    # 测试真模型：输入 5 公里，算出来的时间必须大于 0
    data = PredictionInput(distance_km=5.0, traffic_index=5, weather=1, is_peak=0)
    result = predict_eta(data)
    
    # 断言预测时间大于 0 分钟
    assert result["predicted_eta_min"] > 0