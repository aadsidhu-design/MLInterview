# MLInterview Pipeline

A small data pipeline for telecom churn data. The script:

1. Loads raw CSV data
2. Cleans and validates records
3. Writes a processed CSV into `processed/`
4. Starts a placeholder training step

## Project Structure

- `main.py` - pipeline entry point
- `reader.py` - data loading, cleaning, validation, save, and training stub
- `WA_Fn-UseC_-Telco-Customer-Churn.csv` - source dataset used by the pipeline
- `processed/` - output directory for processed files

## Requirements

- Python 3.10+ (project currently uses a local `.venv`)
- Packages:
  - `pandas`
  - `numpy`

## Setup

1. Update the variable PATH in main.py to the path of the dataset in your computer. It should have "WA_Fn-UseC_-Telco-Customer-Churn.csv" in its name. 


From the project root (`MLInterview`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy
```

## Run the Pipeline from main

From the project root:

```bash
source .venv/bin/activate
python main.py
```

You should see logs similar to:

- `Loading raw data`
- `Cleaning data`
- `Validating data`
- `Saving processed data`
- `Starting model training`

## Output

Processed files are written to:

- `processed/churn_<timestamp>.csv`

Example:

- `processed/churn_2026-05-31_10-35-58.csv`

## Notes

- `main.py` currently loads data from the hardcoded `PATH` variable.
- The `run_pipeline("data/raw/churn_raw.csv")` argument is not used by the current implementation.
- `train_model()` is currently a stub that only prints `Training Model`.


