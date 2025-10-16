import numpy as np

# a) To get help on the multiply function
print("Help on numpy.multiply function:")
help(np.multiply)

# Creating arrays using arange(), full(), and random()
arr1 = np.arange(1, 6)
arr2 = np.full(5, 3)
rand_arr = np.random.randint(1, 10, 5)

print("\nArray 1:", arr1)
print("Array 2:", arr2)
print("Random Array:", rand_arr)

# b) To test whether any of the elements of a given array is non-zero
print("\nAny of the elements are non-zero (arr1):", np.any(arr1))
print("Any of the elements are non-zero (zeros):", np.any(np.zeros(5)))

# c) Element-wise multiplication and division of arrays
print("\nElement-wise Operations between arr1 and arr2:")
print("Multiply:", np.multiply(arr1, arr2))
print("Divide:", np.divide(arr1, arr2))

# d) Finding maximum, minimum, and average values
max_val = np.max(rand_arr)
min_val = np.min(rand_arr)
avg_val = np.mean(rand_arr)

print("\nMaximum value in Random Array:", max_val)
print("Minimum value in Random Array:", min_val)
print("Average value in Random Array:", avg_val)

# e) Square root and power operations
sqrt_arr = np.sqrt(arr1)
power_arr = np.power(arr1, 2)

print("\nSquare root of arr1:", sqrt_arr)
print("arr1 squared:", power_arr)

# f) Sum and Product of elements
sum_result = np.sum(arr1)
prod_result = np.prod(arr1)

print("\nSum of elements in arr1:", sum_result)
print("Product of elements in arr1:", prod_result)
