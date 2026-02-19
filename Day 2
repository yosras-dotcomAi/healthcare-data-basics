import numpy as np

# Create dataset with missing values
data = {
    "Department": ["ICU", "ER", "Ward", "ICU", "ER", "Ward", "ICU", None],
    "Length_of_Stay": [5, 1, 3, 7, 2, 4, None, 6],
    "Age": [65, 40, 30, 70, 50, None, 80, 55]
}

df = pd.DataFrame(data)

print("Missing Values:")
print(df.isnull().sum())


df["Length_of_Stay"].fillna(df["Length_of_Stay"].mean(), inplace=True)
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Department"].fillna("Unknown", inplace=True)

print("After Cleaning:")
print(df)



avg_stay = df.groupby("Department")["Length_of_Stay"].mean()

print("\nAverage Length of Stay per Department:")
print(avg_stay)

avg_stay.plot(kind="bar")
plt.title("Average Length of Stay per Department")
plt.ylabel("Days")
plt.show()
