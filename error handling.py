try:
 numerator = float(input("Enter the numerator: "))
 denominator = float(input("Enter the denominator: "))
 result = numerator / denominator
except ZeroDivisionError:
 print("Error: Cannot divide by zero!")
else:
 print(f"The result is: {result}") 
