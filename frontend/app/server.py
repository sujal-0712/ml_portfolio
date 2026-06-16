import os
import requests
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
)
app.secret_key = "enterprise_multi_tenant_secret"

BACKEND_URL = os.getenv("BACKEND_SERVICE_URL", "http://backend-api:8000")

@app.route("/", methods=["GET", "POST"])
def index():
    active_project = request.args.get("project", "credit")
    prediction_result = None

    if request.method == "POST":
        active_project = request.form.get("_target_project_type")
        target_api_endpoint = f"{BACKEND_URL}/predict/{active_project}"
        
        # Clean down structural parameters to match schema expectation keys
        raw_payload = request.form.to_dict()
        raw_payload.pop("_target_project_type", None)
        
        # Enforce numeric processing lines natively
        processed_payload = {}
        for key, val in raw_payload.items():
            if val.isdigit():
                processed_payload[key] = int(val)
            else:
                try:
                    processed_payload[key] = float(val)
                except ValueError:
                    processed_payload[key] = val

        try:
            response = requests.post(target_api_endpoint, json=processed_payload, timeout=10)
            if response.status_code == 200:
                prediction_result = response.json()
            else:
                err_detail = response.json().get("detail", "Boundary Contract Validation Exception")
                flash(f"Data Matrix Rejected: {err_detail}")
        except Exception as e:
            flash(f"Network Gateway Failure Connecting To Analytical Engine: {str(e)}")
            
        return render_template("index.html", project=active_project, result=prediction_result)

    return render_template("index.html", project=active_project, result=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)