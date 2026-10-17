from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Lobo Projection API")

# 加载刚才训练好的真实模型
model = joblib.load('model.pkl')

class PredictionInput(BaseModel):
    distance_km: float
    traffic_index: int
    weather: int
    is_peak: int

@app.get("/")
def read_root():
    return {"message": "Welcome to Lobo Projection API"}

@app.post("/api/predict")
def predict_eta(data: PredictionInput):
    # 把用户传来的数据变成 Pandas 表格
    input_df = pd.DataFrame([data.model_dump()])
    
    # 让真实模型进行预测
    prediction = model.predict(input_df)[0]
    
    return {"predicted_eta_min": round(float(prediction), 1)}