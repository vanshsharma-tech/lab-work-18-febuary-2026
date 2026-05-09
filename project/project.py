import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv("students.csv")

print("===== STUDENT DATA ANALYSIS =====")

# First 5 rows
print("\nFirst 5 Records:")
print(df.head())

# Total students
print("\nTotal Students:", len(df))

# Average marks
print("\nAverage Marks:", np.mean(df["Marks"]))

# Highest marks
print("Highest Marks:", df["Marks"].max())

# Lowest marks
print("Lowest Marks:", df["Marks"].min())

# Pass/Fail
df["Status"] = np.where(df["Marks"] >= 40, "Pass", "Fail")

# Grade System
def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(grade)

# Topper
print("\nTopper:")
print(df[df["Marks"] == df["Marks"].max()])

# Top 3 students
print("\nTop 3 Students:")
print(df.sort_values(by="Marks", ascending=False).head(3))

# Save updated CSV
df.to_csv("result.csv", index=False)

print("\nResult saved successfully!")