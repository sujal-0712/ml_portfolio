# Unified Multi-Model Inference Platform

A highly optimized, production-grade distributed architecture hosting four independent, enterprise machine learning pipelines behind rigorous runtime schema validation contracts.

This project completely decouples the heavy predictive machine learning stack from the client-facing browser ecosystem using a multi-container Docker topology.

---

## 🏗️ System Architecture Overview

The platform is designed around strict MLOps principles, splitting concerns across two standalone microservices communicating over an isolated, private virtual network bridge:

* **The Predictive Backbone (FastAPI):** An asynchronous ASGI inference engine running Python 3.12. It mounts the serialized pipeline models into system memory at initialization, exposing high-performance POST endpoints. Data shapes are locked down using Pydantic V2 validation matrices.
* **The User Gateway (Flask):** A multi-threaded WSGI frontend proxy interface built on raw, lightweight HTML5 and native embedded CSS. It safely handles external browser interactions, constructs payloads, and reverse-proxies records to the backend for real-time analysis.

### Performance Insulated Containerization
To address standard container compilation bottlenecks when streaming heavy modern ML wheel frameworks (e.g., NumPy, Pandas, XGBoost), the backend image implements **Astral's Rust-backed `uv` pipeline package engine** alongside a `libgomp1` execution layout. This prevents packet truncation errors and achieves near-instant image deployment speeds.

---

## 🧠 Hosted Predictive Engine Profiles

The architecture concurrently drives four distinct predictive systems engineered to map directly onto real-world, high-impact enterprise data challenges:

### 1. Real Estate Valuation Engine (Regression)
* **Objective:** Compute expected housing values across localized spatial zones.
* **Pipeline Topology:** Built using an optimized `XGBRegressor` sequential gradient boosting model paired with automated `StandardScaler` numeric matrices and categorical `OneHotEncoder` tracking loops.
* **Input Context:** Continuous spatial geography (Latitude/Longitude), block layout metrics, and demographic index scaling layers.

### 2. Clinical Diabetes Diagnostic Gateway (Classification)
* **Objective:** Process continuous metabolic and physiological vital tracks to flag medical anomaly patterns.
* **Pipeline Topology:** Class-balanced ensemble learning designed to maximize runtime recall metrics, preventing critical clinical false negatives.
* **Output Metrics:** Computes both direct binary classifications and continuous confidence interval probabilities.

### 3. Enterprise Credit Risk Assessment (Classification)
* **Objective:** Simulate underwriting boundaries for high-frequency consumer lending environments.
* **Pipeline Topology:** An advanced `XGBClassifier` integrated with customized categorical data filters to protect system logic against out-of-bounds numeric anomalies.
* **Output Metrics:** Isolates systemic default exposure and flags high-risk accounts instantly.

### 4. Customer Retention & Churn Optimizer (Classification)
* **Objective:** Track consumer usage behaviors within subscription platforms to mitigate user attrition vectors.
* **Pipeline Topology:** Gradient boosted tree optimization capturing interaction variances, balance thresholds, and account profile features.

---

## 📁 Repository Directory Blueprints

```text
unified-ml-platform/
│
├── backend/                  # FastAPI Application Microservice
│   ├── app/
│   │   ├── __init__.py       # Namespace package definitions
│   │   ├── main.py           # Core ASGI prediction router
│   │   └── schemas.py        # Pydantic validation contracts
│   ├── artifacts/            # Downloaded .pkl model binary files
│   └── Dockerfile            # Rust-insulated container layout
│
├── frontend/                 # Flask Interface Microservice
│   ├── app/
│   │   ├── __init__.py
│   │   └── server.py         # Form proxy & routing layer
│   ├── templates/            # Raw HTML/CSS interface views
│   └── Dockerfile            # Gunicorn deployment profile
│
├── docker-compose.yml        # Orchestration layer configuration
└── .gitignore                # Global version-control blocklist

