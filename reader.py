import pandas as pd


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

data = read_data("/Users/aadi/PycharmProjects/MLInterview/WA_Fn-UseC_-Telco-Customer-Churn.csv")
data = clean_data(data)
print(data.head())

