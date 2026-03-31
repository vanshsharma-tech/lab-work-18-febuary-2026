import matplotlib.pyplot as plt

# Input data
products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
sales = [50, 70, 30, 90, 60]

# Create bar chart
plt.figure()
plt.bar(products, sales)

# Labels and title
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales Bar Chart")

# Show chart
plt.show()