import pandas as pd

data = pd.read_csv("d17_emp.csv")
print("Data: \n", data)

#1. Load the dataset and display the first 5 rows.
print("\nTask 1: First 5 Rows of the Dataset")
print(data.head())

#2. Display basic dataset information using .info(), .shape, and .dtypes.
print("\nTask 2: Dataset Overview")
data.info()
print("Shape: ", data.shape)
print("Data Types: ", data.dtypes)

#3.  Display summary statistics for numerical columns using .describe()
print("\nTask 3: Summary Statistics for Numerical Columns")
print(data.describe())

#4.  Find the Mean, Median, and Mode of the Salary column.
print("\nTask 4: Central Tendency of Salary")
print("Mean Salary: ", data["Salary"].mean())
print("Meadian Salary: ", data["Salary"].median())
print("Mode Salary: \n", data["Salary"].mode())