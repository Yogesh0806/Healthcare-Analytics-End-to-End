import pandas as pd 
from utils import(histogram,bar_plot,pie_chart,box_plot,print_value_counts)


df = pd.read_csv(r'C:\Users\HP\OneDrive\Documents\Desktop\Project-Healthcare-Analysis\Dataset\healthcare_dataset.csv')


#create histogram
histogram(df, "Age")

#Boxplot of using age column 

box_plot(df, "Age")

#creating bar plot
bar_plot(
    df,
    "Gender",
    "Gender Distribution",
    "Gender",
    "Count"
)

#Pie chart
pie_chart(df,"Admission Type")


# printing value counts
print_value_counts(df,"Medical Condition")
        # plot saved ->admission_type_pie.png
# ============================================================
        # MEDICAL CONDITION
# ============================================================
        # Medical Condition
        # Arthritis       9308
        # Diabetes        9304
        # Hypertension    9245
        # Obesity         9231
        # Cancer          9227
        # Asthma          9185
        # Name: count, dtype: int64