import pandas as pd

data = pd.DataFrame({
    "Order_ID": [201, 202, 203, 204, 205, 206, 207, 208],
    "Customer_Name": [
        "Raj", "Sneha", "Karan", "Leela",
        "John", "Priya", "Yusuf", "Pooja"
    ],
    "City": [
        "Mumbai", "Delhi", "Pune", "Jaipur",
        "Delhi", "Mumbai", "Chennai", "Delhi"
    ],
    "Age": [24, None, 31, 29, 45, None, 36, 27],
    "Order_Amount": [2500, 1800, None, 3200, 1500, 2700, 3500, 4000],
    "Order_Date": [
        "2024-02-05", "2024-02-06", "2024-02-06",
        "2024-01-30", "2024-01-29", "2023-12-15",
        "2023-12-20", "2023-11-22"
    ]
})

# Task 1: Display First 5 Orders
print("Task 1: First 5 Orders")
print(data.head())

# Task 2: Dataset Overview
print("\nTask 2: Dataset Overview")
data.info()
print("Shape: ", data.shape)
print("Data Types: ", data.dtypes)

# Task 3: Order Amount Summary
print("\nTask 3: Order Amount Summary")
print(data["Order_Amount"].describe())

# Task 4: Mean, Median and Mode
print("\nTask 4: Central Tendency")
print("Mean: ", data["Order_Amount"].mean())
print("Median: ", data["Order_Amount"].median())
print("Mode: ", data["Order_Amount"].mode())

# Task 5: Range, Variance and Standard Deviation
print("\nTask 5: Spread of Order Amount")
order_range = data["Order_Amount"].max() - data["Order_Amount"].min()
print("Range:", order_range)
print("Variance:", data["Order_Amount"].var())
print("Standard Deviation:", data["Order_Amount"].std())

# Task 6: Age Analysis and Outlier Detection
print("\nTask 6: Age Analysis")

age = data["Age"].dropna()

Q1 = age.quantile(0.25)
Q3 = age.quantile(0.75)
IQR = Q3 - Q1

print("Minimum Age:", age.min())
print("Maximum Age:", age.max())
print("IQR:", IQR)

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = age[(age < lower_limit) | (age > upper_limit)]
print("Outlier Ages:", outliers.tolist())

# Task 7: Missing Value Handling
print("\nTask 7: Handling Missing Values")

data["Age"] = data["Age"].fillna(data["Age"].mean())
data["Order_Amount"] = data["Order_Amount"].fillna(data["Order_Amount"].median())

print(data)

# Task 8: Orders Per City
print("\nTask 8: Orders Per City")

city_orders = data.groupby("City")["Order_ID"].count()
print(city_orders)