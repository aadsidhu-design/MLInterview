import pandas as pd

data = pd.read_csv("/Users/aadi/Documents/WA_Fn-UseC_-Telco-Customer-Churn.csv")
print("CSV loaded")

def clean_data(data):
    print("Data Cleaning")

    data = data.drop_duplicates()
    data = data.dropna()
    data = data.drop("")
    #Clamps value b/w 0,1
    data["Senior Citizen"] = data["Senior Citizen"].clip(lower = 0, upper = 1)
    #Tenure can't be <0
    data["Tenure"] = data["Tenure"].clip(lower=0)


