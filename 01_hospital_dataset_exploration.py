import pandas as pd
import matplotlib.pyplot as plt

# Create simple hospital dataset
data = {
    "Department": ["ICU", "ER", "Ward", "ICU", "ER", "Ward"],
    "Length_of_Stay": [5, 1, 3, 7, 2, 4],
    "Age": [65, 40, 30, 70, 50, 45]
}

df = pd.DataFrame(data)

print("Dataset Preview:")
print(df)

print("\nAverage Length of Stay:", df["Length_of_Stay"].mean())

dept_counts = df["Department"].value_counts()

dept_counts.plot(kind="bar")
plt.title("Patients per Department")
plt.xlabel("Department")
plt.ylabel("Number of Patients")
plt.show()
