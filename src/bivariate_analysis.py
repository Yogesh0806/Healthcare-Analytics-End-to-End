# Step 5: Bivariate Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import BASE_DIR, save_plot

# Load cleaned dataset
df = pd.read_csv(BASE_DIR / "Dataset" / "cleaned_healthcare_dataset.csv")

sns.set_theme(style="whitegrid")
# ================= DEMOGRAPHICS =================

# Age vs Gender
sns.boxplot(data=df, x="Gender", y="Age")
plt.title("Age by Gender")
# save_plot("age_by_gender.png")

# Billing vs Gender
sns.boxplot(data=df, x="Gender", y="Billing Amount")
plt.title("Billing by Gender")
# save_plot("billing_by_gender.png")

# Patients by Gender
df["Gender"].value_counts().plot(kind="bar")
plt.title("Patients by Gender")
plt.ylabel("Number of Patients")
# save_plot("patients_by_gender.png")

# ================= FINANCIAL =================

# Billing vs Medical Condition
sns.boxplot(data=df, x="Medical Condition", y="Billing Amount")
plt.title("Billing by Medical Condition")
plt.xticks(rotation=45)
save_plot("billing_by_condition.png")

# Billing vs Insurance
sns.boxplot(data=df, x="Insurance Provider", y="Billing Amount")
plt.title("Billing by Insurance Provider")
plt.xticks(rotation=45)
save_plot("insurance_vs_billing.png")

# Billing vs Admission Type
df.groupby("Admission Type")["Billing Amount"].mean().plot(kind="bar")
plt.title("Average Billing by Admission Type")
plt.ylabel("Average Billing")
save_plot("billing_by_admission_type.png")