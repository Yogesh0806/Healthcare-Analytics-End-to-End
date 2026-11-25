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
# save_plot("billing_by_condition.png")

# Billing vs Insurance
sns.boxplot(data=df, x="Insurance Provider", y="Billing Amount")
plt.title("Billing by Insurance Provider")
plt.xticks(rotation=45)
# save_plot("insurance_vs_billing.png")

# Billing vs Admission Type
df.groupby("Admission Type")["Billing Amount"].mean().plot(kind="bar")
plt.title("Average Billing by Admission Type")
plt.ylabel("Average Billing")
# save_plot("billing_by_admission_type.png")

# ================= HOSPITAL =================

# Top 10 Hospitals by Patients
df["Hospital"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Hospitals by Patients")
plt.ylabel("Number of Patients")
# save_plot("hospital_patients.png")

# Top 10 Doctors by Patients
df["Doctor"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Doctors by Patients")
plt.ylabel("Number of Patients")
# save_plot("doctor_patients.png")

# Top 10 Hospitals by Average Billing
hospital_billing = df.groupby("Hospital")["Billing Amount"].mean().sort_values(ascending=False).head(10)

hospital_billing.plot(kind="bar")
plt.title("Top 10 Hospitals by Average Billing")
plt.ylabel("Average Billing")
# save_plot("hospital_vs_billing.png")

# ================= CLINICAL =================

# Medical Condition vs Medication
pd.crosstab(df["Medical Condition"], df["Medication"]).plot(kind="bar")
plt.title("Condition vs Medication")
plt.xticks(rotation=45)
# save_plot("condition_vs_medication.png")

# Medical Condition vs Test Results
pd.crosstab(df["Medical Condition"], df["Test Results"]).plot(kind="bar", stacked=True)
plt.title("Condition vs Test Results")
plt.xticks(rotation=45)
# save_plot("condition_vs_test_results.png")

# Admission Type vs Test Results
pd.crosstab(df["Admission Type"], df["Test Results"]).plot(kind="bar", stacked=True)
plt.title("Admission Type vs Test Results")
# save_plot("admission_vs_test_results.png")

# ================= TIME ANALYSIS =================

df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])

# Admissions by Year
df["Date of Admission"].dt.year.value_counts().sort_index().plot(kind="bar")
plt.title("Admissions by Year")
plt.ylabel("Number of Admissions")
save_plot("admissions_by_year.png")

# Admissions by Month
months = df["Date of Admission"].dt.month_name().value_counts()

month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

months = months.reindex(month_order)

months.plot(kind="line", marker="o")
plt.title("Admissions by Month")
plt.ylabel("Number of Admissions")
save_plot("admissions_by_month.png")

# Admissions by Weekday
weekdays = df["Date of Admission"].dt.day_name().value_counts()

weekday_order = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

weekdays = weekdays.reindex(weekday_order)

weekdays.plot(kind="bar")
plt.title("Admissions by Weekday")
plt.ylabel("Number of Admissions")
save_plot("admissions_by_weekday.png")
