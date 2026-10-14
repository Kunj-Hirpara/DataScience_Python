import pandas as pd

# Create Dataset
data = pd.DataFrame({
    "Customer_ID": [1, 2, 3, 4, 5, 6, 7],
    "Name": ["Arjun", "Beena", "Chetan", "Diya", "Esha", "Farhan", "Gita"],
    "Age": [22, 34, None, 41, 26, 29, None],
    "Total_Bill": [1200, 800, 1600, None, 1300, 1400, 1100],
    "Purchase_Date": [
        "2024-01-12",
        "2024-01-14",
        "2024-01-16",
        "2024-01-17",
        "2024-01-19",
        "2023-12-22",
        "2023-12-25"
    ]
})

# Task 1: Display First 5 Rows
print("Task 1: First 5 Rows")
print(data.head())

# Task 2: Dataset Information
print("\nTask 2: Dataset Information")
data.info()
print("Shape: ", data.shape)
print("Data Types: ", data.dtypes)

# Task 3: Sales Summary Statistics
print("\nTask 3: Sales Summary Statistics: ")
print(data["Total_Bill"].describe())

# Task 4: Mean, Median and Mode
print("\nTask 4: Central Tendency")
print("Mean: ", data["Total_Bill"].mean())
print("Median: ", data["Total_Bill"].median())
print("Mode: ", data["Total_Bill"].mode())

# Task 5: Range, Variance and Standard Deviation
print("\nTask 5: Variability")
bill_range = data["Total_Bill"].max() - data["Total_Bill"].min()
print("Range:", bill_range)
print("Variance:", data["Total_Bill"].var())
print("Standard Deviation:", data["Total_Bill"].std())

# Task 6: Age Distribution and Outlier Detection
print("\nTask 6: Age Distribution")

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

# Task 7: Handling Missing Values
print("\nTask 7: Handling Missing Values")

data["Age"] = data["Age"].fillna(data["Age"].mean())
data["Total_Bill"] = data["Total_Bill"].fillna(data["Total_Bill"].median())
print(data)

# Task 8: Yearly Purchase Trend
print("\nTask 8: Yearly Purchase Trend")

data["Purchase_Date"] = pd.to_datetime(data["Purchase_Date"])

yearly_purchases = data.groupby(data["Purchase_Date"].dt.year)["Customer_ID"].count()
print(yearly_purchases)