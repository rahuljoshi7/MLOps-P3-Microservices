
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI(title="Data Preprocessing Service")

class DataRequest(BaseModel):
    data: dict

@app.get("/")
def home():
    return {"message": "Preprocessing Service is running"}

@app.post("/preprocess")
def preprocess(request: DataRequest):
    df = pd.DataFrame([request.data])

    # Clean missing values
    df = df.fillna(0)

    return {
        "message": "Data preprocessing successful",
        "processed_data": df.to_dict(orient="records")[0]
    }
