from datetime import date
import os
from reader import read_data, clean_data, validate_data, save_processed_data


PATH = "/Users/aadi/PycharmProjects/MLInterview/WA_Fn-UseC_-Telco-Customer-Churn.csv"


def train_model(processed_path: str):
    print(f"Training model on {processed_path}")
    # Plug in your training logic here


def run_pipeline() -> bool:
    today = date.today().strftime("%Y-%m-%d")
    processed_path = os.path.join("processed", f"churn_{today}.csv")

    print("Loading raw data")
    try:
        data = read_data(PATH)
    except (FileNotFoundError, IOError) as e:
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
    train_model(processed_path)

    print("Pipeline completed successfully.")
    return True


if __name__ == "__main__":
    run_pipeline()