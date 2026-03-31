import matplotlib.pyplot as plt

# Input data
categories = ["Food", "Rent", "Transport", "Shopping", "Others"]
values = [5000, 12000, 3000, 4000, 2000]

# Create pie chart
plt.figure()
plt.pie(values, labels=categories, autopct='%1.1f%%')

# Title
plt.title("Expense Distribution")

# Show chart
plt.show()