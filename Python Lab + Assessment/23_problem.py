import matplotlib.pyplot as plt

# Input data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 25]

# Plot both datasets
plt.figure()
plt.plot(x, y1, label="Dataset 1")
plt.plot(x, y2, label="Dataset 2")

# Labels and title
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Combined Line Plot")

# Legend
plt.legend()

# Show plot
plt.show()