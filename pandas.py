import pandas as pd

# i) Create and display a Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 35, 28],
    'Marks': [85, 90, 75, 88, 92]
}

df = pd.DataFrame(data)
print("Pandas DataFrame:")
print(df)

# ii) Display column names and data types
print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# iii) Convert one column to a Python list
marks_list = df['Marks'].tolist()
print("\nMarks Column as Python List:")
print(marks_list)
print("Type of marks_list:", type(marks_list))
