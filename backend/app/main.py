import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from app.schemas import CreditPayload, DiabetesPayload, ShippingPayload, ChurnPayload

app = FastAPI(
    title="Enterprise ML Core Analytics Engine",
    version="1.0.0",
    description="Asynchronous microservice serving FinTech, Biotech, E-Commerce, and SaaS pipelines."
)

# FORCE DIRECTORY RESOLUTION:
# This ensures that whether running inside Docker (/app) or locally, 
# it accurately steps up out of 'app' to find 'artifacts'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIR = os.path.join(BASE_DIR, "artifacts")

def load_artifact(filename: str):
    path = os.path.join(ARTIFACT_DIR, filename)
    print(f"--- [SYSTEM DEBUG] Attempting to load tracking asset from: {path} ---")
    if os.path.exists(path):
        try:
            model = joblib.load(path)
            print(f"--- [SUCCESS] Safely loaded: {filename} ---")
            return model
        except Exception as e:
            print(f"--- [CRITICAL] Failed reading model asset {filename}: {str(e)} ---")
    else:
        print(f"--- [WARNING] Path does not exist on filesystem: {path} ---")
    return None

# Re-trigger tenant initialization registry maps
models = {
    "credit": load_artifact("credit_risk_pipeline.pkl"),
    "diabetes": load_artifact("healthcare_readmit_pipeline.pkl"),
    "shipping": load_artifact("shipping_risk_pipeline.pkl"),
    "churn": load_artifact("customer_churn_pipeline.pkl")
}


def execute_pipeline_inference(model_key: str, payload_data: dict):
    model = models.get(model_key)
    if model is None:
        raise HTTPException(status_code=503, detail=f"Model artifact tracking stream for '{model_key}' is uninitialized or corrupt.")
    try:
        input_df = pd.DataFrame([payload_data])
        prediction = int(model.predict(input_df)[0])
        probability = float(model.predict_proba(input_df)[0][1])
        return {"prediction": prediction, "risk_score_probability": round(probability, 4)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference Execution Engine Error: {str(e)}")

@app.get("/health")
def system_health():
    return {
        "status": "operational",
        "registry_telemetry": {k: (v is not None) for k, v in models.items()}
    }

@app.post("/predict/credit")
async def run_credit(payload: CreditPayload):
    return execute_pipeline_inference("credit", payload.model_dump())

@app.post("/predict/diabetes")
async def run_diabetes(payload: DiabetesPayload):
    return execute_pipeline_inference("diabetes", payload.model_dump())

@app.post("/predict/shipping")
async def run_shipping(payload: ShippingPayload):
    return execute_pipeline_inference("shipping", payload.model_dump())

@app.post("/predict/churn")
async def run_churn(payload: ChurnPayload):
    return execute_pipeline_inference("churn", payload.model_dump())