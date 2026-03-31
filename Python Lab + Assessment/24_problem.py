import matplotlib.pyplot as plt

# Input data
x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]

# Scatter plot
plt.figure()
plt.scatter(x, y)

# Find maximum point
max_y = max(y)
max_index = y.index(max_y)
max_x = x[max_index]

# Highlight maximum point
plt.scatter(max_x, max_y, color='red')
plt.text(max_x, max_y, f"({max_x}, {max_y})")

# Labels and title
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with Maximum Point Highlighted")

# Show plot
plt.show()