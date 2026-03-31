import matplotlib.pyplot as plt

# Input data (Monthly revenue)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [2000, 2500, 2200, 3000, 2800, 3500]

# Create plot
plt.figure()
plt.plot(months, revenue)

# Customization
plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.grid()

# Show plot
plt.show()