from fastapi import FastAPI
from service import MLPredictor
from schema import Request

ml_predictor = MLPredictor()
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Fajar M"}

@app.post("/predict")
def predict(req:Request):
    label = ml_predictor.predict(req=req)

    return {"prediction": label}