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

# 3. Does house size affect total price? 
correlation = data["sqft"].corr(data["totalprice"])
print("Correlation between Area and Price: ", correlation)

print("======================================")

# 4. Does the number of bedrooms affect price? 
avg_bhk_price = data.groupby("bhk")["totalprice"].mean().round(2).sort_values(ascending=False)
print("bhk according Average: \n", avg_bhk_price)
print("Correlation between bhk and price: ")
print(data["bhk"].corr(data["totalprice"]))

print("======================================")

# 5. Compare different property types.
 
# aggregate .agg

property_comparison = data.groupby("propertytype")["totalprice"].agg(
    ["count", "mean", "min", "max"]
).round(2)
print(property_comparison)

print("======================================")

# 6. Identify unusually expensive or inexpensive properties. 

mean_price = data["totalprice"].mean()
std_price = data["totalprice"].std()

expensive = data[
    data["totalprice"] > mean_price + 3 * std_price
]

inexpensive = data[
    data["totalprice"] < mean_price - 3 * std_price
]

print("Unusually Expensive Properties:")
print(expensive)

print("\nUnusually Inexpensive Properties:")
print(inexpensive)

print("Expensive:", len(expensive))
print("Inexpensive:", len(inexpensive))

print("======================================")

# 7. Analyze the correlation between area and price. 

correlation = data["sqft"].corr(data["totalprice"])
print("Correlation between Area and Price: ", correlation)

print("======================================")

# 8. Create a scatter plot of area vs. price. 

import matplotlib.pyplot as plt

plt.scatter(data["sqft"], data["totalprice"])

plt.xlabel("Area (sqft)")
plt.ylabel("Total Price")
plt.title("Area vs Total Price")

plt.show()

print("======================================")

# 9. Generate a correlation heatmap. 

import seaborn as sns
import matplotlib.pyplot as plt

corr = data[
    ["bhk", "sqft", "pricepersqft", "totalprice"]
].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

print("======================================")

# 10.Identify the major factors associated with house prices. 
print(
    data[
        ["bhk", "sqft", "pricepersqft", "totalprice"]
    ].corr()["totalprice"].sort_values(ascending=False)
)