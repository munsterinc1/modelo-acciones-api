# API de Predicción de Precio de Acciones con FastAPI

Este proyecto implementa una **API REST con FastAPI** que expone un modelo de Machine Learning para predecir el **precio de cierre del día siguiente** de una acción (ejemplo: Apple - AAPL), a partir de datos bursátiles reales descargados con `yfinance`.

El modelo está entrenado con un `RandomForestRegressor` usando los atributos:

- `Open`
- `High`
- `Low`
- `Close`
- `Volume`

---

## Estructura del proyecto

```text
modelo-acciones-api/
├── app/
│   ├── main.py        # API FastAPI
│   ├── utils.py       # Lógica de predicción
│   ├── schemas.py     # Validaciones con Pydantic
│   └── model.joblib   # Modelo entrenado
├── clients.py         # Cliente de pruebas
├── train_model.py     # Script de entrenamiento
├── requirements.txt   # Dependencias
└── README.md          # Documentación
```

## Despliegue en Render

La API está disponible públicamente en Render:

- [https://modelo-acciones-api.onrender.com](https://modelo-acciones-api.onrender.com)

Documentación interactiva (Swagger):  
- [https://modelo-acciones-api.onrender.com/docs](https://modelo-acciones-api.onrender.com/docs)

---

## Instalación y uso local

### 1. Clonar repositorio

git clone https://github.com/munsterinc1/modelo-acciones-api.git
cd modelo-acciones-api

### 2. Crear entorno virtual
python -m venv venv

Activar:

- Windows: venv\Scripts\activate

- Mac/Linux: source venv/bin/activate

### 3. Instalar dependencias
- pip install -r requirements.txt

### 4. Entrenar el modelo (opcional, ya se incluye model.joblib)
- python train_model.py

### 5. Ejecutar servidor local
- uvicorn app.main:app --reload

La API estará disponible en:
- http://127.0.0.1:8000
- Documentación Swagger: http://127.0.0.1:8000/docs

## Uso de la API

- Endpoint principal

https://modelo-acciones-api.onrender.com/docs


Dirigirse a sección -> POST /predict y seleccionar "Trying Out"

- Formato JSON de entrada
{
  "Open": 180,
  "High": 185,
  "Low": 175,
  "Close": 182,
  "Volume": 1000000
}

- Respuesta esperada
{
  "prediccion_precio_de_cierre_mañana": 181.76
}

## Cliente de pruebas

Se incluye un script clients.py que realiza 3 peticiones a la API.

Ejecutar en terminal:

python clients.py

Ejemplo de salida:

- Petición 1: {'Open': 180, 'High': 185, 'Low': 175, 'Close': 182, 'Volume': 1000000}
- Predicción: {'prediccion_precio_de_cierre_mañana': 181.76}

## Autor

Proyecto desarrollado como parte de un trabajo académico de Magíster de Ciencia de Datos UDD.
- Repositorio: https://github.com/munsterinc1/modelo-acciones-api
- Servicio web desplegado en render: https://modelo-acciones-api.onrender.com

---
