from pydantic import BaseModel

class StockData(BaseModel):
    Open: float
    High: float
    Low: float
    Close: float
    Volume: float

class Prediction(BaseModel):
    prediccion_precio_de_cierre_mañana: float
