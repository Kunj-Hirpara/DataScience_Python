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

import pandas as pd

data = pd.DataFrame({
    "Name": ['A','B','C'],
    "Math": [45,35,60],
    "Science": [50,30,70]
})
print("Students passed both subjects: ")
print(data[(data["Math"] >= 40) & (data["Science"] >= 40)])

print("======================================")

# 7. Country population:
# {'India':1400,'USA':331,'Nepal':29,'Bhutan':0.8} (in millions)
# Display countries with pop <50 million.

import pandas as pd

data = {
    'India':1400,
    'USA':331,
    'Nepal':29,
    'Bhutan':0.8
}
for country, pop in data.items():
    if pop < 50:
        print(country, pop)

print("======================================")

# 8. Movies CSV has Movie,Rating. Filter rating>4 and export to Excel.

data = pd.read_csv("d13_movie.csv")

filtered_movies = data[data["Rating"] > 4.0]
print("Movies with rating > 4: \n", filtered_movies)
print("Exporting filtered movies to Excel...")
filtered_movies.to_excel("d13_filtered_movies.xlsx", index=False)

print("======================================")

# 9. Employees:
# Name=['A','B','A']
# Dept=['HR','IT','HR']
# Remove duplicates.

import pandas as pd

data = pd.DataFrame({
    "Name": ['A','B','A'],
    "Dept": ['HR','IT','HR']
})

result = data.drop_duplicates()
print("Employees after removing duplicates: \n", result)

print("======================================")

# 10. Exam scores:
# [45,55,65,80,90]
# Find how many scored above 75.

import pandas as pd

scores = pd.Series([45,55,65,80,90])
count = (scores > 75).sum()
print("Number of students scored above 75: ", count)

print("======================================")

# 11. Prices stored as strings:
# ['100','200','300']
# Convert to numeric.

import pandas as pd

prices = pd.Series(['100','200','300'])
prices_numeric = pd.to_numeric(prices)
print("Prices converted to numeric: \n", prices_numeric)

print("======================================")

# 12. Data:
# Name=['A','B','C']
# City=['Delhi',None,'Mumbai']
# Fill missing city with Unknown, standardize lowercase.

import pandas as pd

data = pd.DataFrame({
    "Name": ['A','B','C'],
    "City": ['Delhi',None,'Mumbai']
})

data["City"] = data["City"].fillna("Unknown")
data["City"] = data["City"].str.lower()
print("Data after filling missing city and standardizing: \n", data)

print("======================================")

# 13. Sales data with Region,Amount. Group by region and display avg sales.

import pandas as pd

data = pd.DataFrame({
    "Region": ['North','South','East','West','North','South'],
    "Amount": [1000,1500,2000,2500,3000,3500]
})

result = data.groupby("Region")["Amount"].mean()
print("Grouped average sales by region: \n", result)

print("======================================")

# 14. Excel sales.xlsx with Date,Sales. Filter sales between '2024-01-01' and '2024-02-01'

# import pandas as pd

# data = pd.read_excel("d13_date_sales.xlsx")

# data["Date"] = pd.to_datetime(data["Date"])

# print("Sales between '2024-01-01' and '2024-02-01' :")
# print(data[(data["Date"] >= '2024-01-01') & (data["Date"] <= '2024-02-01')])