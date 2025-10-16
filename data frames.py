import pandas as pd
import numpy as np

# Sample data
student_data = {
    'student': ['Ravi', 'Sneha', 'Arjun', 'Priya', 'Anjali',
                'Rahul', 'Neha', 'Amit', 'Divya', 'Karan'],
    'marks': [15, 11, 18, np.nan, 12, 20, 14, np.nan, 10, 17],
    'attempts': [2, 1, 3, 2, 1, 3, 2, 1, 2, 1],
    'passed': ['yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'no', 'no', 'yes']
}

index_labels = list('abcdefghij')

# i) Create and display the DataFrame
df = pd.DataFrame(student_data, index=index_labels)
print("Original DataFrame:\n")
print(df)

# ii) Change the name 'Priya' to 'Sunita'
df.replace({'student': {'Priya': 'Sunita'}}, inplace=True)
print("\nDataFrame after changing name 'Priya' to 'Sunita':\n")
print(df)

# iii) Add a new column 'grade' based on marks
df['grade'] = ['A' if x >= 17 else 'B' if x >= 13 else 'C' for x in df['marks'].fillna(0)]
print("\nDataFrame after adding new column 'grade':\n")
print(df)

# iv) Get list of column headers
column_headers = list(df.columns)
print("\nList of column headers:")
print(column_headers)
