# =====================================================================
# UNIFIED CENTRAL ML INFERENCE ENGINE
# =====================================================================
from fastapi import FastAPI, HTTPException
import pandas as pd
import joblib
import os
import sys
import __main__  # Import the active root execution module

# Import the consolidated validation gateways from our local schemas module
from app.schemas import (
    HousingValuationSchema,
    ClinicalDiabetesSchema,
    CreditApplicationSchema,
    CustomerBehaviorSchema
)

# =====================================================================
# MLOPS SAFEGUARD: CUSTOM TRANSFORMER NAMESPACE INJECTION
# =====================================================================
# 1. Paste your exact 'CaliforniaHousingTransformer' class definition from your notebook here:
from sklearn.base import BaseEstimator, TransformerMixin

class CaliforniaHousingTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
        
    def transform(self, X):
        X_copy = X.copy()
        # Ensure your custom feature engineering steps (like dividing columns)
        # from your notebook are pasted here exactly so the shapes align.
        # e.g., X_copy['rooms_per_household'] = X_copy['total_rooms'] / X_copy['households']
        return X_copy

# --- 2. CLINICAL MODEL CUSTOM CODE ---
class ClinicalDiagnosisTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        X_copy = X.copy()
        # (Paste your exact clinical transformation/feature engineering steps here)
        return X_copy

# 2. Bind the class dynamically to the active running __main__ namespace.
# This forces joblib to find the class when it unpacks your .pkl file under Uvicorn.
__main__.CaliforniaHousingTransformer = CaliforniaHousingTransformer
__main__.ClinicalDiagnosisTransformer = ClinicalDiagnosisTransformer

# =====================================================================
# FASTAPI APPLICATION BOOT SEQUENCE
# =====================================================================
app = FastAPI(
    title="Unified Enterprise ML Inference Platform",
    description="High-performance centralized gateway hosting 4 independent predictive pipelines.",
    version="1.0.0"
)

# Construct a robust relative file path matching our container's file system tree
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_PATH = os.path.join(BASE_DIR, "artifacts")

try:
    print("--- Initializing Production Model Deserialization Sequence ---")
    # Now that the namespace patch is active, this line will execute flawlessly:
    housing_model = joblib.load(os.path.join(ARTIFACT_PATH, "housing_pipeline.pkl"))
    diabetes_model = joblib.load(os.path.join(ARTIFACT_PATH, "diabetes_pipeline.pkl"))
    credit_model = joblib.load(os.path.join(ARTIFACT_PATH, "credit_risk_pipeline.pkl"))
    churn_model = joblib.load(os.path.join(ARTIFACT_PATH, "customer_churn_pipeline.pkl"))
    print("✅ All 4 execution binaries safely mounted into System Memory!")
except Exception as e:
    print(f"❌ CRITICAL INITIALIZATION ERROR: Failed to load binary model assets. Detail: {e}")
    raise RuntimeError(e)




# ---------------------------------------------------------------------
# SYSTEM HEALTH ENDPOINT
# ---------------------------------------------------------------------
@app.get("/", tags=["Infrastructure Health Check"])
def system_root_health():
    return {
        "status": "OPERATIONAL",
        "platform_architecture": "FastAPI ASGI",
        "mounted_pipelines": ["Housing_Regression", "Diabetes_Classification", "Credit_Risk_XGB", "Customer_Churn_XGB"]
    }


# ---------------------------------------------------------------------
# ENDPOINT 1: REAL ESTATE VALUATION ENGINE
# ---------------------------------------------------------------------
@app.post("/predict/housing", tags=["Real Estate Analytics"])
def predict_housing_prices(payload: HousingValuationSchema):
    try:
        # Convert incoming data directly to a DataFrame via Pydantic model_dump
        input_df = pd.DataFrame([payload.model_dump()])
        
        # Execute model pipeline inference pass
        raw_prediction = housing_model.predict(input_df)[0]
        
        # Scale to match original base monetization metrics (value in hundreds of thousands)
        calculated_valuation = float(raw_prediction * 100000.0)
        
        return {
            "success": True,
            "predicted_valuation_usd": round(calculated_valuation, 2)
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Inference Failure: {str(error)}")


# ---------------------------------------------------------------------
# ENDPOINT 2: CLINICAL DIABETES DIAGNOSTIC GATEWAY
# ---------------------------------------------------------------------
@app.post("/predict/diabetes", tags=["Clinical Healthcare Systems"])
def predict_clinical_diabetes(payload: ClinicalDiabetesSchema):
    try:
        input_df = pd.DataFrame([payload.model_dump()])
        
        # Extract binary flag classification and continuous prediction confidence
        binary_prediction = int(diabetes_model.predict(input_df)[0])
        confidence_probabilities = diabetes_model.predict_proba(input_df)[0]
        risk_probability = float(confidence_probabilities[1])
        
        return {
            "success": True,
            "diabetes_risk_detected": True if binary_prediction == 1 else False,
            "calculated_risk_probability": round(risk_probability, 4)
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Clinical Processing Failure: {str(error)}")


# ---------------------------------------------------------------------
# ENDPOINT 3: FINTECH CREDIT RISK SCORING Engine
# ---------------------------------------------------------------------
@app.post("/predict/credit", tags=["FinTech Risk Assessment"])
def predict_credit_default(payload: CreditApplicationSchema):
    try:
        input_df = pd.DataFrame([payload.model_dump()])
        
        binary_prediction = int(credit_model.predict(input_df)[0])
        confidence_probabilities = credit_model.predict_proba(input_df)[0]
        default_probability = float(confidence_probabilities[1])
        
        return {
            "success": True,
            "default_risk_isolated": True if binary_prediction == 1 else False,
            "exposure_probability": round(default_probability, 4)
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"FinTech Matrix Evaluation Failure: {str(error)}")


# ---------------------------------------------------------------------
# ENDPOINT 4: SAAS CUSTOMER RETENTION OPTIMIZATION
# ---------------------------------------------------------------------
@app.post("/predict/churn", tags=["Enterprise Retention Analytics"])
def predict_customer_attrition(payload: CustomerBehaviorSchema):
    try:
        input_df = pd.DataFrame([payload.model_dump()])
        
        binary_prediction = int(churn_model.predict(input_df)[0])
        confidence_probabilities = churn_model.predict_proba(input_df)[0]
        churn_probability = float(confidence_probabilities[1])
        
        return {
            "success": True,
            "attrition_risk_detected": True if binary_prediction == 1 else False,
            "churn_probability_score": round(churn_probability, 4)
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"SaaS System Analytics Failure: {str(error)}")