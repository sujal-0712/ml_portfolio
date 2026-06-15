# =====================================================================
# CENTRALIZED API DATA GATEWAY & RUNTIME SCHEMAS
# =====================================================================
from pydantic import BaseModel, Field, field_validator
from typing import Literal

# ---------------------------------------------------------------------
# 1. REAL ESTATE REGRESSION MODULE (Project #1)
# ---------------------------------------------------------------------
class HousingValuationSchema(BaseModel):
    MedInc: float = Field(..., ge=0.5, le=15.0, description="Median income in tens of thousands.")
    HouseAge: float = Field(..., ge=1.0, le=52.0)
    AveRooms: float = Field(..., ge=1.0, le=15.0)
    AveBedrms: float = Field(..., ge=0.5, le=10.0)
    Population: float = Field(..., ge=3.0, le=35000.0)
    AveOccup: float = Field(..., ge=1.0, le=10.0)
    Latitude: float = Field(..., ge=32.0, le=42.0)
    Longitude: float = Field(..., le=-114.0, ge=-125.0)


# ---------------------------------------------------------------------
# 2. CLINICAL DIABETES DETECTION MODULE (Project #2)
# ---------------------------------------------------------------------
class ClinicalDiabetesSchema(BaseModel):
    Pregnancies: int = Field(..., ge=0, le=20)
    Glucose: float = Field(..., ge=0.0, le=300.0)
    BloodPressure: float = Field(..., ge=0.0, le=200.0)
    SkinThickness: float = Field(..., ge=0.0, le=100.0)
    Insulin: float = Field(..., ge=0.0, le=900.0)
    BMI: float = Field(..., ge=0.0, le=70.0)
    DiabetesPedigreeFunction: float = Field(..., ge=0.0, le=3.0)
    Age: int = Field(..., ge=21, le=120, description="Clinical trial focuses on adult profiles.")


# ---------------------------------------------------------------------
# 3. FINTECH CREDIT RISK SCORING MODULE (Project #3)
# ---------------------------------------------------------------------
class CreditApplicationSchema(BaseModel):
    person_age: int = Field(..., ge=18, le=120)
    person_income: float = Field(..., ge=0.0)
    person_home_ownership: Literal['RENT', 'MORTGAGE', 'OWN', 'OTHER']
    person_emp_length: float = Field(..., ge=0.0, le=60.0)
    loan_intent: Literal['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION']
    loan_grade: Literal['A', 'B', 'C', 'D', 'E', 'F', 'G']
    loan_amnt: float = Field(..., ge=500.0, le=100000.0)
    loan_int_rate: float = Field(..., ge=0.0, le=50.0)
    loan_percent_income: float = Field(..., ge=0.0, le=1.0)
    cb_person_default_on_file: Literal['Y', 'N']
    cb_person_cred_hist_length: int = Field(..., ge=0.0)

    @field_validator('person_income', 'loan_amnt')
    @classmethod
    def enforce_positive_economics(cls, value: float) -> float:
        if value <= 0:
            raise ValueError("Financial fields must be greater than zero.")
        return value


# ---------------------------------------------------------------------
# 4. SAAS RETENTION OPTIMIZATION MODULE (Project #4)
# ---------------------------------------------------------------------
class CustomerBehaviorSchema(BaseModel):
    CreditScore: int = Field(..., ge=300, le=850)
    Geography: Literal['France', 'Spain', 'Germany']
    Gender: Literal['Female', 'Male']
    Age: int = Field(..., ge=18, le=110)
    Tenure: int = Field(..., ge=0, le=10)
    Balance: float = Field(..., ge=0.0)
    NumOfProducts: int = Field(..., ge=1, le=4)
    HasCrCard: Literal[0, 1]
    IsActiveMember: Literal[0, 1]
    EstimatedSalary: float = Field(..., ge=0.0)

    @field_validator('EstimatedSalary')
    @classmethod
    def validate_earnings_floor(cls, value: float) -> float:
        if value < 0:
            raise ValueError("Compensation tracks cannot fall below zero.")
        return value