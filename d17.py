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

#5. Calculate Range, Variance, and Standard Deviation of the Salary column.
print("\nTask 5: Dispersion of Salary")
print("Range Salary: ", data["Salary"].max() - data["Salary"].min())
print("Variance Salary: ", data["Salary"].var())
print("Standard Deviation Salary: ", data["Salary"].std())

#6.  Find the Minimum, Maximum, and Interquartile Range (IQR) of the Age column.
print("\nTask 6: Age Analysis")
age = data["Age"].dropna()

Q1 = age.quantile(0.25)
Q3 = age.quantile(0.75)
IQR = Q3 - Q1

print("Minimum Age:", age.min())
print("Maximum Age:", age.max())
print("IQR:", IQR)

#7. Detect Salary Outliers using IQR
print("\nTask 7: Salary Outliers")
salary = data["Salary"].dropna()

Q1 = salary.quantile(0.25)
Q3 = salary.quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = data[
    (data["Salary"] < lower_limit) |
    (data["Salary"] > upper_limit)
]

print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print(outliers[["Employee_ID", "Name", "Salary"]])

#8. Detect missing values in the dataset (NaNs) and count them for each column.
print("\nTask 8: Missing Values Count")
missing_values = data.isnull().sum()
print(missing_values)

#9.  Fill missing values in Age with mean and Salary with median, then display updated dataset.
print("\nTask 9: Handling Missing Values")
data["Age"] = data["Age"].fillna(data["Age"].mean())
data["Salary"] = data["Salary"].fillna(data["Salary"].median())
print(data)

#10. Drop rows with missing Salary values and display the cleaned dataset.
print("\nTask 10: Dropping Rows with Missing Salary Values")
data_cleaned = data.dropna(subset=["Salary"])
print(data_cleaned)

#11. Use .interpolate() to fill missing Age values and show updated column.
print("\nTask 11: Interpolating Missing Age Values")
data["Age"] = data["Age"].interpolate()
print(data["Age"])

#12. Display the correlation matrix between Age, Salary, Experience_Years, and Performance_Score.
print("\nTask 12: Correlation Matrix")
corr = data[["Age", "Salary", "Experience_Years", "Performance_Score"]].corr()
print(corr)

#13. Find the employee(s) with the highest salary.
print("\nTask 13: Employee(s) with Highest Salary")
highest_salary = data[data["Salary"] == data["Salary"].max()]
print(highest_salary)

#14. Find the mean Salary per Department using .groupby().
print("\nTask 14: Mean Salary per Department")
mean_salary_per_department = data.groupby("Department")["Salary"].mean().round(2)
print(mean_salary_per_department)

#15. Find how many employees joined per year using groupby on Joining_Date.
print("\nTask 15: Employees Joined per Year")
data["Joining_Date"] = pd.to_datetime(data["Joining_Date"])
print(data.groupby(data["Joining_Date"].dt.year).size())

#16. Calculate average Salary per year and identify the year with the highest average salary.
print("\nTask 16: Average Salary per Year")
avg_salary_per_year = data.groupby(data["Joining_Date"].dt.year)["Salary"].mean()
print(avg_salary_per_year)
print("Year with Highest Average Salary:", avg_salary_per_year.idxmax())

# Task 17: Fill Missing Values using Forward Fill
print("\nTask 17: Forward Fill")
ffill_data = data.copy()
ffill_data = ffill_data.ffill()

print(ffill_data)

# Task 18: Fill Missing Values with Unknown
print("\nTask 18: Fill Missing Values with Unknown")
unknown_data = data.copy()
unknown_data = unknown_data.fillna("Unknown")

print(unknown_data)