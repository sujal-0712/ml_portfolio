# Unified Enterprise ML Analytics Platform

Welcome to the **Unified Enterprise ML Analytics Platform**—a production-ready, multi-tenant prediction hub. This architecture consolidates four distinct, high-dimensional machine learning engines under a single microservice control plane, serving industries across FinTech, Biotech, Logistical Supply Chains, and SaaS operations.

By decoupling our heavy computation layers (**FastAPI**) from user interaction clients (**Flask**), the platform achieves absolute structural resiliency. 

---

## 🚀 Core Engine Architecture

Rather than deploying four redundant microservices, this hub uses a **dynamic multi-tenant routing grid**. Incoming payloads pass through automated, schema-enforced perimeter gateways before reaching their respective tree-boosting decision nodes.

* **FinTech Credit Risk Control:** Predicts consumer loan default probabilities using historical application profiles. Optimizes classification cost against high-loss asymmetric financial risks.
* **Biotech Clinical Diabetes Analytics:** Isolates 30-day early hospital readmission trajectories from dense patient care records, helping systems proactively identify care gaps before patient discharge.
* **Logistics Late Shipping Risk:** Evaluates international e-commerce transit details to isolate supply chain bottlenecks and flag delayed delivery items prior to shipment confirmation.
* **SaaS Customer Retention Engine:** Tracks customer subscription data and behavioral traits to calculate real-time user churn scoring, enabling retention teams to trigger contextual incentives.

---

## 🛠️ The Technical Stack

* **Core Logic Layers:** FastAPI (Asynchronous Python ASGI), Flask (Frontend Proxy Router)
* **Predictive Infrastructure:** Scikit-Learn `ColumnTransformer` pipelines paired with optimized `XGBClassifier` nodes.
* **Data Validation Perimeter:** Strict Pydantic contracts verifying raw input stream bounds before execution.
* **Environment Management:** Automated, blazing-fast dependency tracking and resolution driven entirely by **uv**.
* **Container Isolation Engine:** Multi-stage Docker virtualization unified via Docker Compose.

---

## 📁 Repository Layout

```text
unified-ml-platform/
│
├── backend/                  # Asynchronous Core Analytics Service
│   ├── app/
│   │   ├── main.py           # Multi-tenant prediction routing engine
│   │   └── schemas.py        # Strict Pydantic validation boundaries
│   ├── artifacts/            # Storage folder for serialized pipeline binaries (.pkl)
│   └── Dockerfile            # UV-bootstrapped builder image profile
│
├── frontend/                 # User Interaction Interface Proxy
│   ├── app/
│   │   └── server.py         # Form payload parsing and endpoint proxy layer
│   ├── templates/            # Dynamic Tailwind HTML dashboard interfaces
│   └── Dockerfile            # Ultra-lightweight Flask worker deployment script
│
├── docker-compose.yml        # Internal bridge network orchestrator
├── data/                    # contain all the csv file used for training
├── assets/                   # conatin all the jupyter notebook code for model training 
