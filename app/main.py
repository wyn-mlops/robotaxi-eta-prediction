from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
    # 这里现在是假模型，直接返回 20.5 分钟
    # 等队友把真的 model.pkl 给你，你再换掉
    return {"predicted_eta_min": 20.5}