import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os

os.makedirs("app", exist_ok=True)

df = yf.download("AAPL", start="2022-01-01", end="2024-12-31")
df = df.dropna()
df["Close_next"] = df["Close"].shift(-1)
df = df.dropna()

X = df[["Open", "High", "Low", "Close", "Volume"]]
y = df["Close_next"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")

joblib.dump(model, "app/model.joblib")
print("✅ Modelo guardado en app/model.joblib")
