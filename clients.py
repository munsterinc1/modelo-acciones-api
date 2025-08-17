import requests

URL = "https://modelo-acciones-api.onrender.com/predict"

payloads = [
    {"Open": 180, "High": 185, "Low": 175, "Close": 182, "Volume": 1000000},
    {"Open": 150, "High": 153, "Low": 148, "Close": 151, "Volume": 2000000},
    {"Open": 200, "High": 205, "Low": 198, "Close": 203, "Volume": 1500000},
]

for i, payload in enumerate(payloads, 1):
    response = requests.post(URL, json=payload)
    print(f"🔹 Petición {i}: {payload}")
    print(f"🔸 Predicción: {response.json()}\n")
