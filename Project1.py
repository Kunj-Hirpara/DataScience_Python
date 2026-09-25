# Project Question
# Analyze the factors associated with house prices in India using Python.

# Students should investigate:
# 1. What is the average house price? 
# 2. Which locations have the highest average prices? 
# 3. Does house size affect total price? 
# 4. Does the number of bedrooms affect price? 
# 5. Compare different property types. 
# 6. Identify unusually expensive or inexpensive properties. 
# 7. Analyze the correlation between area and price. 
# 8. Create a scatter plot of area vs. price. 
# 9. Generate a correlation heatmap. 
# 10.Identify the major factors associated with house prices. 

import pandas as pd

data = pd.read_csv("House_Price_Data.csv")

# 1. What is the average house price? 
print("The Average of house price: ")
print(data["totalprice"].mean().round(2))

print("======================================")

# 2. Which locations have the highest average prices? 
print("Which locations have the highest average prices? ")
print(
    data.groupby("location")["totalprice"]
    .mean().round(2)
    .sort_values(ascending=False)
)

print("======================================")
