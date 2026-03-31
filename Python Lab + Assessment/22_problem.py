import matplotlib.pyplot as plt
import numpy as np

# Generate random dataset
data = np.random.randint(1, 100, 50)

# Create histogram
plt.figure()
plt.hist(data, bins=10)

# Labels and title
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram of Dataset")

# Show plot
plt.show()