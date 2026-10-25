import pandas as pd
import matplotlib.pyplot as plt

# Sample hospital dataset (synthetic data for learning purposes)
data = {
    "Department": ["ICU", "ER", "Ward", "ICU", "ER", "Ward"],
    "Length_of_Stay": [5, 1, 3, 7, 2, 4],
    "Age": [65, 40, 30, 70, 50, 45]
}

df = pd.DataFrame(data)

# Correlation between age and length of stay
correlation = df["Age"].corr(df["Length_of_Stay"])
print("Correlation between Age and Length of Stay:", round(correlation, 2))

# Scatter plot
plt.scatter(df["Age"], df["Length_of_Stay"])
plt.title("Age vs Length of Stay")
plt.xlabel("Age")
plt.ylabel("Length of Stay (Days)")
plt.show()
