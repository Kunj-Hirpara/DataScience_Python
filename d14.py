# 1. Create and Analyze Sales Data using Series
# A retail shop records its daily sales (in ) for the first week of January:
# ₹[1500, 1800, 2100, 1900, 2500, 3000, 2800]
# Tasks:
# • Create a Pandas Series for these sales with days of the week as index labels.
# • Display the sales on Wednesday using label indexing and on the 5th day using 
# integer indexing.
# • Calculate the total and average sales.

import pandas as pd

sales = pd.Series({
    "Monday": 1500,
    "Tuesday": 1800,
    "Wednesday": 2100,
    "Thursday": 1900,
    "Friday": 2500,
    "Saturday": 3000,
    "Sunday": 2800
})
print("Sales Data: \n", sales)
print("Sales on wednesday: ", sales["Wednesday"])
print("Sales on 5th day: ", sales.iat[4])
print("Total sales: ", sales.sum())
print("Average sales: ", sales.mean().round(2))

print("======================================")

# 2. Employee Salary Operations
# A company records employee salaries ( ): 
# ₹ [30000, 45000, 50000, 35000].
# Tasks:
# • Create a Series with custom index labels: ['E1', 'E2', 'E3', 'E4'].
# • Apply a 10% bonus (element-wise multiplication).
# • Display the updated salary of E2 and E4.

import pandas as pd

salary = pd.Series({
    "E1": 30000,
    "E2": 45000,
    "E3": 50000,
    "E4": 35000
})
print("Original Salary: \n", salary)
salary_with_bonus = salary * 1.10
print("Updated salary of E2 and E4: \n", salary_with_bonus[["E2", "E4"]])

print("======================================")

# 3. Student Marks from Dictionary
# A school stores student marks in a dictionary:
# {'Math': 78, 'Science': 82, 'English': 90, 'History': 85}
# Tasks:
# • Convert the dictionary into a Pandas Series.
# • Display all subjects where the score is above 80.
# • Find the average score.

import pandas as pd

marks = {
    "Math": 78,
    "Science": 82,
    "English": 90,
    "History": 85
}
marks_series = pd.Series(marks)
print("subjects with score above 80: \n", marks_series[marks_series > 80])
print("Average score: ", marks_series.mean().round(2))

print("======================================")

# 4. DataFrame Creation from Real Data
# Create a DataFrame for 5 employees with columns: Name, Age, Department.
# Tasks:
# • Display the first 3 rows using .head().
# • Show the shape of the DataFrame.
# • Display the data types of all columns.

import pandas as pd

data = pd.DataFrame({
    "Name": ['a', 'b', 'c', 'd', 'e'],
    "Age": [25, 30, 22, 28, 35],
    "Department": ['HR', 'Finance', 'IT', 'Marketing', 'Sales']
})
print("First 3 rows: \n", data.head(3))
print("Shape of dataframe: ", data.shape)
print("Data types of columns: \n", data.dtypes)

print("======================================")

# 5. Customer Filtering by Age & City
# A store has customer data:
# Name,Age,City
# Rahul,24,Delhi
# Neha,30,Mumbai
# Alok,28,Delhi
# Priya,22,Chennai
#  Tasks:
# • Create a DataFrame.
# • Filter customers whose Age > 25.
# • Further filter customers with City = Delhi and select only Name and Age columns.

import pandas as pd

data = pd.DataFrame({
    "Name": ['Rahul', 'Neha', 'Alok', 'Priya'],
    "Age": [24, 30, 28, 22],
    "City": ['Delhi', 'Mumbai', 'Delhi', 'Chennai']
})
print("Customers older than 25 and living in Delhi: ")
print(data[(data["Age"] > 25) & (data["City"] == "Delhi")][["Name", "Age"]])

print("======================================")

# 6. Import & Export Operations
# You have an Excel file products.xlsx with columns: Product, Price, Stock.
# Tasks:
# • Read the Excel file into a Pandas DataFrame.
# • Display the top 5 rows.
# • Export the same data into a CSV file named products.csv without index.

# import pandas as pd

# data = pd.read_excel("products.xlsx")
# print(data.head())
# data.to_csv("products.csv", index=False)

print("======================================")