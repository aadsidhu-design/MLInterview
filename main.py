from datetime import date, datetime
import os
from reader import read_data, clean_data, validate_data, save_processed_data, train_model
import pandas as pd

PATH = "/Users/aadi/PycharmProjects/MLInterview/WA_Fn-UseC_-Telco-Customer-Churn.csv"




def run_pipeline(input_path: str) -> bool:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    processed_path = os.path.join("processed", f"churn_{timestamp}.csv")

    print("Loading raw data")
    try:
        data = read_data(PATH)
    except (FileNotFoundError, pd.errors.EmptyDataError) as e:
        print(f"Pipeline failed at load step: {e}")
        return False

    print("Cleaning data")
    data = clean_data(data)

    print("Validating data")
    result = validate_data(data)

    if not result.is_valid:
        print("Validation failed. Issues found:")
        for e in result.error_msg:
            print(f"  - {e}")
        print("Pipeline stopped.")
        return False

    print("Saving processed data")
    save_processed_data(data, processed_path)

    print("Starting model training")
    train_model()
    return True


if __name__ == "__main__":
    run_pipeline("data/raw/churn_raw.csv")