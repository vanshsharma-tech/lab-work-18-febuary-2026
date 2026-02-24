# File Name: common_elements.py
# Problem 60
# Find common elements between two lists using function


# Function to find common elements
def find_common_elements(list1, list2):

    common = []  # List to store common elements

    # Traverse through first list
    for item in list1:
        # Check if item is present in second list
        # Also check to avoid duplicate entries
        if item in list2 and item not in common:
            common.append(item)

    return common


# -------- Main Program --------

# Taking first list input
# Example input: 1 2 3 4 5
list1 = list(
    map(int, input("Enter elements of first list separated by space: ").split())
)

# Taking second list input
# Example input: 3 4 5 6 7
list2 = list(
    map(int, input("Enter elements of second list separated by space: ").split())
)

# Calling the function
result = find_common_elements(list1, list2)

# Printing result
print("Common Elements:", result)
