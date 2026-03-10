import mlflow
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Predict diabets app")
model = None

class DiabetData(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

@app.on_event("startup")
def startup():
    pass

@app.post("/api/v1/setup_model/{run_id}")
def setup_model(run_id: str):
    MLFLOW_TRACKING_URI = "http://mlflow:8080"
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    global model
    model = mlflow.sklearn.load_model(f"runs:/{run_id}/diabetes")

@app.post("/api/v1/predict")
async def predict(data: DiabetData):
    values = np.array(list(data.model_dump().values()))
    values = values.reshape(1, -1)
    prediction = model.predict(values)
    return {"predict": prediction.tolist()}
