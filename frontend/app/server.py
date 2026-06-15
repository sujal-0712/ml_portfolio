# =====================================================================
# FLASK WEB INTERFACE GATEWAY ROUTER
# =====================================================================
from flask import Flask, render_template, request
import requests
import os

# Initialize Flask configuration before assigning endpoints
app = Flask(__name__, template_folder="../templates")

# Resolve the backend microservice network container pointer
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")


@app.route('/')
def index():
    return render_template("index.html")


# -------------------------------------------------------------------
# 1. CALIFORNIA HOUSING VALUATION ROUTE (PROJECT 1)
# -------------------------------------------------------------------
@app.route('/housing', methods=['GET', 'POST'])
def route_housing():
    if request.method == 'POST':
        try:
            payload = {
                "MedInc": float(request.form.get("MedInc")),
                "HouseAge": float(request.form.get("HouseAge")),
                "AveRooms": float(request.form.get("AveRooms")),
                "AveBedrms": float(request.form.get("AveBedrms")),
                "Population": float(request.form.get("Population")),
                "AveOccup": float(request.form.get("AveOccup")),
                "Latitude": float(request.form.get("Latitude")),
                "Longitude": float(request.form.get("Longitude"))
            }
            response = requests.post(f"{BACKEND_URL}/predict/housing", json=payload)
            res_data = response.json()
            
            if response.status_code == 200:
                # RECTIFIED: Matches backend 'predicted_valuation_usd' response key
                return render_template("housing.html", result=res_data.get("predicted_valuation_usd"))
            return render_template("housing.html", error=res_data.get("detail", "Inference Failed."))
        except Exception as e:
            return render_template("housing.html", error=str(e))
            
    return render_template("housing.html")


# -------------------------------------------------------------------
# 2. CLINICAL DIABETES DIAGNOSTICS ROUTE (PROJECT 2)
# -------------------------------------------------------------------
@app.route('/diabetes', methods=['GET', 'POST'])
def route_diabetes():
    if request.method == 'POST':
        try:
            # RECTIFIED: Now maps to PIMA features declared in schemas.py
            payload = {
                "Pregnancies": int(request.form.get("Pregnancies")),
                "Glucose": float(request.form.get("Glucose")),
                "BloodPressure": float(request.form.get("BloodPressure")),
                "SkinThickness": float(request.form.get("SkinThickness")),
                "Insulin": float(request.form.get("Insulin")),
                "BMI": float(request.form.get("BMI")),
                "DiabetesPedigreeFunction": float(request.form.get("DiabetesPedigreeFunction")),
                "Age": int(request.form.get("Age"))
            }
            response = requests.post(f"{BACKEND_URL}/predict/diabetes", json=payload)
            res_data = response.json()
            
            if response.status_code == 200:
                # RECTIFIED: Maps backend output tokens cleanly and converts decimal to percentage score
                raw_prob = res_data.get("calculated_risk_probability", 0.0)
                return render_template(
                    "diabetes.html", 
                    risk_detected=res_data.get("diabetes_risk_detected"), 
                    probability=float(raw_prob * 100.0)
                )
            return render_template("diabetes.html", error=res_data.get("detail", "Inference Failed."))
        except Exception as e:
            return render_template("diabetes.html", error=str(e))
            
    return render_template("diabetes.html")