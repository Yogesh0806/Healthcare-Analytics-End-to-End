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
