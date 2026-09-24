# 1. Create a Pandas Series for monthly expenses: Rent=12000, Groceries=5000, Utilities=2000, 
# Entertainment=3000.  Tasks: Display total and average expenses. Access Groceries using label and 
# 2nd element using index.

import pandas as pd

expenses = pd.Series({
    "Rent": 12000,
    "Groceries": 5000,
    "Utilities": 2000,
    "Entertainment": 3000
})
print("Expenses: \n", expenses)
print("Total Expenses: ", expenses.sum())
print("Average Expenses: ", expenses.mean())
print("Groceries: ", expenses["Groceries"])
print("2nd Element: ", expenses.iloc[1])

print("======================================")

# 2. A company records weekly sales revenue: [15000, 18000, 21000, 19000]. 
# Tasks: Create a Series with week labels ['Week1','Week2','Week3','Week4'], find maximum and 
# minimum revenue weeks.

import pandas as pd

sales = pd.Series({
    "Week1": 15000,
    "Week2": 18000,
    "Week3": 21000,
    "Week4": 19000
})
print("Sales: \n", sales)

max_week = sales.idxmax()
min_week = sales.idxmin()

print("Maximum Revenue:", sales.max())
print("Maximum Revenue Week:", max_week)

print("Minimum Revenue:", sales.min())
print("Minimum Revenue Week:", min_week)

print("======================================")

# 3. Convert dictionary marks={'Math':35,'Science':48,'English':55,'History':42} into Series. 
# Display subjects where marks < 50.

import pandas as pd

marks = {
    "Math": 35,
    "Science": 48,
    "English": 55,
    "History": 42
}
data = pd.Series(marks)
print("Data: \n", data)
print("Subjects with less than 50 marks: ")
print(data[data < 50])

print("======================================")

# 4. Create DataFrame for students:
# Name=['Amit','Riya','John','Meena','Sam','Alok']
# Age=[15,16,15,17,14,16]
# Grade=['A','B','A','A','C','B']
# Display top 4 rows and bottom 2 rows.

import pandas as pd

data = pd.DataFrame({
    "Name": ['Amit','Riya','John','Meena','Sam','Alok'],
    "Age": [15,16,15,17,14,16],
    "Grade": ['A','B','A','A','C','B']
})
print("Top 4 Rows: ")
print(data.head(4))

print("Bottom 2 Rows: ")
print(data.tail(2))

print("======================================")

# 5. Data:
# Name=['Rahul','Neha','Alok','Priya']
# Age=[24,30,28,22]
# City=['Delhi','Mumbai','Delhi','Chennai']
# Filter students older than 25 living in Delhi.

import pandas as pd

data = pd.DataFrame({
    "Name": ['Rahul','Neha','Alok','Priya'],
    "Age": [24,30,28,22],
    "City": ['Delhi','Mumbai','Delhi','Chennai']
})
print(data)
print("Older than 25: \n", data[(data["Age"] > 25) & (data["City"] == "Delhi")])

print("======================================")

# 6. Assume 'products.csv' has columns Product,Price,Stock. Read CSV, display shape, top 5 rows 
# and dtypes.

import pandas as pd

data = pd.read_csv("d12_product.csv")

print("Shape:")
print(data.shape)

print("\nTop 5 Rows:")
print(data.head(5))

print("\nData Types:")
print(data.dtypes)

print("======================================")

# 7. Data:
# Product=['Pen','Notebook','Pencil']
# Price=[10,50,5]
# Export DataFrame to Excel 'sales.xlsx'.

import pandas as pd

data = pd.DataFrame({
    "Product": ['Pen','Notebook','Pencil'],
    "Price": [10,50,5]
})
print(data)
data.to_excel("d12_sales.xlsx", index = False)
print("Data export successfully.")

print("======================================")

# 8. Data:
# Name=['A','B','C','D']
# Salary=[30000,None,40000,None]
# Fill missing salary with mean.

import pandas as pd

data = pd.DataFrame({
    "Name": ['A','B','C','D'],
    "Salary": [30000,None,40000,None]
})
print("Before Fill missing value: \n", data)
mean_salary = data["Salary"].mean()
data["Salary"] = data["Salary"].fillna(mean_salary)
print("After Fill missing value: \n", data)

print("======================================")

# 9. Data:
# Full Name=['John Smith','Alice Johnson',None,'Bob Brown']
# Split into first,last name, fill missing with 'Unknown'.

import pandas as pd

data = pd.DataFrame({
    "Full Name": ['John Smith','Alice Johnson',None,'Bob Brown']
})
data["Full Name"] = data["Full Name"].fillna("Unknown Unknown")

data[["First Name", "Last Name"]] = data["Full Name"].str.split(" ", n=1, expand=True)

print(data)

print("======================================")

# 10. Data:
# Customer=['A','B','C','D']
# Age=[25,-5,0,40]
# Replace invalid age (<=0) with mean of valid ages.

import pandas as pd

data = pd.DataFrame({
    "Customer": ["A", "B", "C", "D"],
    "Age": [25.0, -5.0, 0.0, 40.0]
})
valid_mean = data.loc[data["Age"] > 0, "Age"].mean()
data.loc[data["Age"] <= 0, "Age"] = valid_mean

print(data)

print("======================================")

# 11. Data:
# Date=['2024-01-01','2024-02-01','2024-03-01']
# Convert Date to datetime format.



# 12. Data:
# Product=['Laptop','Mobile','Tablet','Printer']
# Price=[75000,30000,None,500000]
# Remove outlier price>3*std, fill missing with mean.



# 13. Excel file employees.xlsx with Name,DOB columns.
# Convert DOB to datetime, display age in years.



# 14. Data:
# Name=['A','B','C']
# Marks=[40,60,80]
# Normalize Marks using min-max scaling between 0 and 1.