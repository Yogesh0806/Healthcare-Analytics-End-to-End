"""
Healthcare Analytics End-to-End
Step 5: Feature Engineering

Purpose:
Create additional analytical features from the cleaned
healthcare dataset for EDA and Power BI.
"""
import pandas as pd
from pathlib import Path


# ==========================================================
# 1. PROJECT PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "Dataset"

INPUT_FILE = DATASET_DIR / "cleaned_healthcare_dataset.csv"

OUTPUT_FILE = DATASET_DIR / "feature_engineered_healthcare_dataset.csv"


# ==========================================================
# 2. LOAD DATASET
# ==========================================================

df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

print(f"Dataset loaded successfully: {df.shape}")

# ==========================================================
# 3. CONVERT DATE COLUMNS
# ==========================================================

df["Date of Admission"] = pd.to_datetime(
    df["Date of Admission"],
    errors="coerce"
)

df["Discharge Date"] = pd.to_datetime(
    df["Discharge Date"],
    errors="coerce"
)


# ==========================================================
# 4. LENGTH OF STAY
# ==========================================================

df["Length of Stay"] = (
    df["Discharge Date"] - df["Date of Admission"]
).dt.days

print("\nLength of Stay created successfully.")


# ==========================================================
# 5. AGE GROUP
# ==========================================================

age_bins = [0, 17, 29, 44, 59, 74, 120]

age_labels = [
    "0-17",
    "18-29",
    "30-44",
    "45-59",
    "60-74",
    "75+"
]

df["Age Group"] = pd.cut(
    df["Age"],
    bins=age_bins,
    labels=age_labels,
    include_lowest=True
)

print("Age Group created successfully.")

