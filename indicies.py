import numpy as np

# Create a NumPy array
arr = np.array([2, 5, 7, 3, 9, 5, 2, 10, 7])

# Specify a number for comparison
num = 5

# a) Extract numbers less than and greater than a specified number
less_than_num = arr[arr < num]
greater_than_num = arr[arr > num]

print("Array:", arr)
print(f"\nNumbers less than {num}:", less_than_num)
print(f"Numbers greater than {num}:", greater_than_num)

# b) Find max, min and their indices
max_val = np.max(arr)
min_val = np.min(arr)
max_index = np.argmax(arr)
min_index = np.argmin(arr)

print("\nMaximum value:", max_val)
print("Minimum value:", min_val)
print("Index of Maximum value:", max_index)
print("Index of Minimum value:", min_index)

# Find unique elements
unique_elements = np.unique(arr)
print("\nUnique elements:", unique_elements)

# Count occurrences of each unique element using bincount
count_elements = np.bincount(arr)
print("Count of each element:", count_elements)

# Get string representation of the array
print("\nString representation of array:", repr(arr))
