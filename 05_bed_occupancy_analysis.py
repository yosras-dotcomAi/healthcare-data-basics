import pandas as pd
import matplotlib.pyplot as plt

# Synthetic patient data for learning purposes
data = {
    "Patient_ID": range(1, 21),
    "Age": [25, 60, 45, 70, 34, 50, 80, 29, 66, 40,
            55, 73, 38, 62, 47, 30, 85, 52, 44, 68],
    "Gender": ["F", "M", "F", "M", "F", "M", "F", "F", "M", "M",
               "F", "M", "F", "F", "M", "F", "M", "F", "M", "F"],
    "Diagnosis": ["Pneumonia", "Diabetes", "Fracture", "COPD", "Appendicitis",
                  "Hypertension", "Stroke", "UTI", "Heart Failure", "Infection",
                  "Asthma", "COPD", "Fracture", "Diabetes", "Infection",
                  "Appendicitis", "Stroke", "Hypertension", "UTI", "Heart Failure"],
    "Length_of_Stay": [3, 7, 4, 10, 2, 5, 12, 3, 9, 6,
                       4, 11, 5, 8, 6, 2, 14, 7, 3, 9]
}

df = pd.DataFrame(data)

# Overview
print("First rows:")
print(df.head())
print("\nShape (rows, columns):", df.shape)
print("\nStatistical summary:")
print(df.describe())

print("\nMaximum LOS:", df["Length_of_Stay"].max())
print("Minimum LOS:", df["Length_of_Stay"].min())

# Age vs length of stay
correlation = df["Age"].corr(df["Length_of_Stay"])
print("\nCorrelation between Age and LOS:", round(correlation, 2))

plt.figure()
plt.scatter(df["Age"], df["Length_of_Stay"])
plt.xlabel("Age")
plt.ylabel("Length of Stay (days)")
plt.title("Age vs Length of Stay")
plt.show()

# Average length of stay per diagnosis
diagnosis_los = df.groupby("Diagnosis")["Length_of_Stay"].mean().sort_values(ascending=False)
print("\nAverage LOS per diagnosis:")
print(diagnosis_los.round(1))

diagnosis_los.plot(kind="bar")
plt.title("Average Length of Stay per Diagnosis")
plt.ylabel("Days")
plt.tight_layout()
plt.show()
