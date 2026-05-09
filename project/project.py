import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")

print(df.head())

print("Average Marks:", np.mean(df["Marks"]))

print("Topper:")
print(df[df["Marks"] == df["Marks"].max()])