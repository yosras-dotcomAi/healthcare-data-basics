correlation = df["Age"].corr(df["Length_of_Stay"])

print("Correlation between Age and Length of Stay:", correlation)


plt.scatter(df["Age"], df["Length_of_Stay"])
plt.title("Age vs Length of Stay")
plt.xlabel("Age")
plt.ylabel("Length of Stay (Days)")
plt.show()
