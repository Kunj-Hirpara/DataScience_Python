# 1. City population:
# City=['Mumbai','Delhi','Pune','Mysore']
# Population=[20000000,19000000,5000000,800000]
# Filter cities with population>1 million OR name starts with M.

import pandas as pd

data = pd.DataFrame({
    "City": ['Mumbai','Delhi','Pune','Mysore'],
    "Population": [20000000,19000000,5000000,800000]
})
print("Cities with population > 1 million OR name starts with M: ")
print(data[(data["Population"] > 1000000) | (data["City"].str.startswith("M"))]) 

print("======================================")

# 2. Orders:
# OrderID=[1,2,3,4]
# Amount=[200,800,600,400]
# Select OrderID,Amount where Amount>500.

import pandas as pd

data = pd.DataFrame({
    "OrderID": [1,2,3,4],
    "Amount": [200,800,600,400]
})
print("Orders with Amount > 500: ")
print(data[data["Amount"] > 500])

print("======================================")

# 3. Assume 'sales.csv' with columns Region,Sales.
# Read CSV and display descriptive stats using describe().

import pandas as pd

data = pd.read_csv("d13_sales.csv")

print("Descriptive Statistics: \n", data.describe())

print("======================================")

# 4. Product stock:
# Product=['Pen','Pencil','Book']
# Stock=[100,200,300]
# Apply 5% restock and display updated stock.

import pandas as pd

data = pd.DataFrame({
    "Product": ['Pen','Pencil','Book'],
    "Stock": [100,200,300]
})
data["Stock"] = data["Stock"] * 1.05
print("Updated Stock after 5% restock: \n", data)

print("======================================")

# 5. Vehicles:
# Model=['X','Y','Z']
# Price=[500000,700000,600000]
# Mileage=[15,18,20]
# Display rows sorted by Price descending.

import pandas as pd

data = pd.DataFrame({
    "Model": ['X','Y','Z'],
    "Price": [500000,700000,600000],
    "Mileage": [15,18,20]
})
print("Vehicles sorted by price descending :")
print(data.sort_values(by="Price", ascending=False))

print("======================================")

# 6. Students:
# Name=['A','B','C']
# Math=[45,35,60]
# Science=[50,30,70]
# Filter students passed both subjects>=40.


# 7. Country population:
# {'India':1400,'USA':331,'Nepal':29,'Bhutan':0.8} (in millions)
# Display countries with pop <50 million.


# 8. Movies CSV has Movie,Rating. Filter rating>4 and export to Excel.


# 9. Employees:
# Name=['A','B','A']
# Dept=['HR','IT','HR']
# Remove duplicates.


# 10. Exam scores:
# [45,55,65,80,90]
# Find how many scored above 75.


# 11. Prices stored as strings:
# ['100','200','300']
# Convert to numeric.


# 12. Data:
# Name=['A','B','C']
# City=['Delhi',None,'Mumbai']
# Fill missing city with Unknown, standardize lowercase.


# 13. Sales data with Region,Amount. Group by region and display avg sales.


# 14. Excel sales.xlsx with Date,Sales. Filter sales between '2024-01-01' and '2024-02-01'