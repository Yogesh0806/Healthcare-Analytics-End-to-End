'''HEALTHCARE ANALYTICS END-TO-END'''

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv(r'C:\Users\HP\OneDrive\Documents\Desktop\Project-Healthcare-Analysis\Dataset\healthcare_dataset.csv')
# print(df.head())

# ==========================================================
'''Step 1 : Dataset Understanding'''
#
# Workflow:
# 1. Import Required Libraries
# 2. Load Dataset
# 3. Display First & Last Records
# 4. Check Dataset Shape
# 5. Display Column Names
# 6. Check Data Types
# 7. Dataset Information
# 8. Statistical Summary
# 9. Missing Value Analysis
# 10. Duplicate Record Analysis
# 11. Unique Values Analysis
# 12. Initial Observations
# ==========================================================

# print(df.tail())

# print(df.shape) #(55500, 15)

# print(df.columns)

# print(df.info())

# print(df.describe())

# print(df.isnull().sum())

# print(df.duplicated().sum())

# for col in df.columns:
#     print(f"\n{col}")
#     print(df[col].nunique())