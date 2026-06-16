from pydantic import BaseModel, Field, field_validator
from typing import Literal

# =====================================================================
# 1. FINTECH CREDIT RISK VALIDATION SCHEMA
# =====================================================================
class CreditPayload(BaseModel):
    person_age: int = Field(..., ge=18, le=120, description="Borrower age.")
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
    def enforce_nonzero_economics(cls, value: float) -> float:
        if value <= 0:
            raise ValueError("Financial parameters must represent positive numeric values.")
        return value

# =====================================================================
# 2. BIOTECH CLINICAL DIABETES READMISSION SCHEMA
# =====================================================================
class DiabetesPayload(BaseModel):
    time_in_hospital: int = Field(..., ge=1, le=14)
    num_lab_procedures: int = Field(..., ge=1, le=150)
    num_procedures: int = Field(..., ge=0, le=10)
    num_medications: int = Field(..., ge=1, le=100)
    number_outpatient: int = Field(..., ge=0, le=50)
    number_emergency: int = Field(..., ge=0, le=50)
    number_inpatient: int = Field(..., ge=0, le=50)
    number_diagnoses: int = Field(..., ge=1, le=20)
    race: Literal['Caucasian', 'AfricanAmerican', 'Unknown', 'Other', 'Asian', 'Hispanic']
    gender: Literal['Female', 'Male', 'Unknown']
    age: Literal['[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)', '[50-60)', '[60-70)', '[70-80)', '[80-90)', '[90-100)']
    metformin: Literal['No', 'Steady', 'Up', 'Down']
    insulin: Literal['No', 'Steady', 'Up', 'Down']
    change: Literal['No', 'Ch']
    diabetesMed: Literal['No', 'Yes']

# =====================================================================
# 3. E-COMMERCE SHIPPING LATE DELIVERY RISK SCHEMA
# =====================================================================
class ShippingPayload(BaseModel):
    Warehouse_block: Literal['A', 'B', 'C', 'D', 'F']
    Mode_of_Shipment: Literal['Ship', 'Flight', 'Road']
    Customer_care_calls: int = Field(..., ge=2, le=10)
    Customer_rating: int = Field(..., ge=1, le=5)
    Cost_of_the_Product: float = Field(..., ge=50.0, le=1000.0)
    Prior_purchases: int = Field(..., ge=2, le=20)
    Product_importance: Literal['low', 'medium', 'high']
    Gender: Literal['F', 'M']
    Discount_offered: float = Field(..., ge=0.0, le=100.0)
    Weight_in_gms: float = Field(..., ge=500.0, le=15000.0)

# =====================================================================
# 4. ENTERPRISE CONSUMER RETENTION/CHURN SCHEMA
# =====================================================================
class ChurnPayload(BaseModel):
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