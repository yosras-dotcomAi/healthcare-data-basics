import pandas as pd
import matplotlib.pyplot as plt


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

df.head()


df.shape


df.describe()


print("Maximum LOS:", df["Length_of_Stay"].max())
print("Minimum LOS:", df["Length_of_Stay"].min())



plt.figure()
plt.scatter(df["Age"], df["Length_of_Stay"])
plt.xlabel("Age")
plt.ylabel("Length of Stay (days)")
plt.title("Age vs Length of Stay")
plt.show()



diagnosis_los = df.groupby("Diagnosis")["Length_of_Stay"].mean()
print(diagnosis_los)




