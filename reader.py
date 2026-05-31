import pandas as pd


def read_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    print("CSV loaded")
    return data

def clean_data(data:pd.DataFrame) -> pd.DataFrame:
    print("Data Cleaning")

    data = data.drop_duplicates()
    data = data.replace(["", " "], None)
    data = data.dropna()

    #Clamps value b/w 0,1
    data["SeniorCitizen"] = data["SeniorCitizen"].clip(lower = 0, upper = 1)
    #Tenure can't be <0
    data["tenure"] = data["tenure"].clip(lower=0)

    return data


data = clean_data(data)
print(data.head())

