from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Logging Service")

class LogRequest(BaseModel):
    message: str
    level: str = "INFO"

@app.get("/")
def home():
    return {"message": "Logging Service is running"}

@app.post("/log")
def create_log(request: LogRequest):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "level": request.level,
        "message": request.message
    }

    with open("logs.txt", "a") as file:
        file.write(str(log_entry) + "\n")

    return {
        "message": "Log saved successfully",
        "log": log_entry
    }