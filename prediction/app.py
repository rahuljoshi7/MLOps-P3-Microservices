
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path

app = FastAPI(title="ML Prediction Service")

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "model.pkl"

class PredictionRequest(BaseModel):
    features: dict

@app.get("/")
def home():
    return {"message": "Prediction Service is running"}

@app.post("/predict")
def predict(request: PredictionRequest):
    model = joblib.load(MODEL_PATH)

    input_data = pd.DataFrame([request.features])
    prediction = int(model.predict(input_data)[0])

    return {
        "message": "Prediction successful",
        "prediction": prediction,
        "result": "Malignant" if prediction == 0 else "Benign"
    }
