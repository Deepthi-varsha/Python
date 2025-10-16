user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
largest_number = max(numbers)
print("The largest number in the list is:", largest_number)
