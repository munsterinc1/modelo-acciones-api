from fastapi import FastAPI
from joblib import load
import numpy as np
from app.schemas import StockData, Prediction
from app.utils import predict_price

app = FastAPI()
model = load("app/model.joblib")

@app.get("/")
def root():
    return {"Mensaje": "API para predecir precio de cierre de acciones"}

@app.post("/predict", response_model=Prediction)
def predict(data: StockData):
    prediction = predict_price(model, data)
    return {"prediccion_precio_de_cierre_mañana": prediction}
