# Step 5: Bivariate Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import BASE_DIR, save_plot

# Load cleaned dataset
df = pd.read_csv(BASE_DIR / "Dataset" / "cleaned_healthcare_dataset.csv")

sns.set_theme(style="whitegrid")