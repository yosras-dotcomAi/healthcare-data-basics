import pandas as pd

# Sample hospital dataset (synthetic data for learning purposes)
data = {
    "Department": ["ICU", "ER", "Ward", "ICU", "ER", "Ward"],
    "Length_of_Stay": [5, 1, 3, 7, 2, 4],
    "Age": [65, 40, 30, 70, 50, 45]
}

df = pd.DataFrame(data)

# Clinical question:
# Which department keeps patients the longest, and are they older?

print("Statistical summary:")
print(df.describe())

summary = df.groupby("Department")[["Length_of_Stay", "Age"]].mean().round(1)
print("\nAverage length of stay and age per department:")
print(summary)

# Interpretation:
# ICU patients are older and stay longer, which suggests higher acuity.
# This matters for staffing and bed planning.
