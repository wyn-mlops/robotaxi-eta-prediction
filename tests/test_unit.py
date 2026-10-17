import pytest
from pydantic import ValidationError
from app.main import PredictionInput

def test_input_valid():
    # 测试正常输入，数据格式没问题
    data = PredictionInput(distance_km=5.0, traffic_index=5, weather=1, is_peak=0)
    assert data.distance_km == 5.0

def test_negative_distance():
    # 测试边界情况：距离不能为负数，必须报错
    with pytest.raises(ValidationError):
        PredictionInput(distance_km=-1.0, traffic_index=5, weather=1, is_peak=0)