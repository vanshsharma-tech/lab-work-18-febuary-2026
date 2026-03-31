# Create a line plot using given x and y values

import matplotlib.pyplot as plt

# Example input data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Plot
plt.figure()
plt.plot(x, y)

# Labels and title
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line Plot")

# Show plot
plt.show()