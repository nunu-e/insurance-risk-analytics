import pandas as pd

# Load raw data
df = pd.read_csv("data/insurance_data.csv")

# Clean data
cleaned_df = df.drop_duplicates()

# Save cleaned version
cleaned_df.to_csv(
    "data/cleaned_insurance_data.csv",
    index=False
)

print("Cleaned data saved successfully")