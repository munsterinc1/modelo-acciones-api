import numpy as np
from app.schemas import StockData

def predict_price(model, data: StockData) -> float:
    X = np.array([[data.Open, data.High, data.Low, data.Close, data.Volume]])
    return float(model.predict(X)[0])
