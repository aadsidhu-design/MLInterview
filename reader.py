import pandas as pd
import os
from dataclasses import dataclass, field
from typing import List

@dataclass
class Validation:
    is_valid: bool
    error_msg: List[str] = field(default_factory=list)

def read_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    print("CSV loaded")
    return data

def clean_data(data:pd.DataFrame) -> pd.DataFrame:
    print("Data Cleaning")

    #Strip whitespace
    str_cols = data.select_dtypes(include="object").columns
    data[str_cols] = data[str_cols].apply(lambda col: col.str.strip())

    data = data.drop_duplicates()
    data = data.replace(["", " "], None)

    #Convert Total charges: str -> numerical
    if "TotalCharges" in data.columns:
        data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors="coerce")

    #Drop data from use if these options are blank, or N/A, since we would need for model training.
    data = data.dropna(subset = ["customerID", "Churn", "MonthlyCharges", "TotalCharges"])

    #Clamps value b/w 0,1
    data["SeniorCitizen"] = data["SeniorCitizen"].clip(lower = 0, upper = 1).astype(int)
    #Tenure can't be <0
    data["tenure"] = data["tenure"].clip(lower=0)

    #Remove outliers outside of 99th percentile.
    for col in ["tenure", "MonthlyCharges", "TotalCharges"]:
        if col in data.columns:
            cap = data[col].quantile(0.99)
            data[col] = data[col].clip(upper=cap)

    return data


def validate_data(data:pd.DataFrame) -> Validation:
    print("Data Validation")
    errors = []

    important_cols = ["customerID", "Churn", "MonthlyCharges", "TotalCharges"]
    for col in important_cols:
        if col not in data.columns:
            errors.append(f"Missing column: {col}")

    if(len(data) == 0):
        errors.append("Empty Data")
    if "SeniorCitizen" in data.columns:
        invalid_senior = ~data["SeniorCitizen"].isin([0, 1])
        if invalid_senior.any():
            errors.append("SeniorCitizen contains values other than 0 or 1.")

    if "customerID" in data.columns and data["customerID"].duplicated().any():
        errors.append("customerID contains duplicates")

    if "Churn" in data.columns:
        valid_churn = {"Yes", "No"}
        invalid_churn = ~data["Churn"].isin(valid_churn)
        if invalid_churn.any():
            errors.append("Churn column contains different values")

    #MonthlyCharges and TotalCharges should be positive
    if (data["MonthlyCharges"] <= 0).any():
        errors.append("MonthlyCharges has zero/negative values.")
    if (data["TotalCharges"] < 0).any():
        errors.append("TotalCharges has negative values.")

    if len(data) < 100:
        errors.append(f"Only {len(data)} rows have too small a sample size.")

    return Validation(is_valid=len(errors) == 0, error_msg = errors)


def save_processed_data(df: pd.DataFrame, output_path: str) -> str:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved processed data to {output_path}")
    return output_path



