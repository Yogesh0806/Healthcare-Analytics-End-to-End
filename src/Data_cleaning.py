import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv(r'C:\Users\HP\OneDrive\Documents\Desktop\Project-Healthcare-Analysis\Dataset\healthcare_dataset.csv')

# print(df)

# ==========================================================
# Step 3 : Data Cleaning & Preprocessing
#
# Workflow
# 1. Import Libraries
# 2. Load Dataset
# 3. Check Missing Values
# 4. Handle Missing Values
# 5. Remove Duplicate Records
# 6. Correct Data Types
# 7. Detect Outliers
# 8. Standardize Text Columns
# 9. Validate Dataset
# 10. Export Cleaned Dataset
# ==========================================================

print(df.isnull().sum())
        # 0
        
print(df.duplicated().sum())
        # 534
        
df = df.drop_duplicates()

print(df.dtypes)

df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])

test_columns = df.select_dtypes(include='object').columns

for col in test_columns :
    df[col] = df[col].str.strip()
    
    
# Validation :

print(df.info())
    
print(df.isnull().sum())

print(df.duplicated().sum())


df.to_csv(r'C:\Users\HP\OneDrive\Documents\Desktop\Project-Healthcare-Analysis\Dataset\cleaned_healthcare_dataset.csv',index=False)

print("Cleaned dataset saved successfully!")