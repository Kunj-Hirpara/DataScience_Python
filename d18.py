# Task 1: Monthly Sales Trend (Line Plot)
# Situation: A store has monthly sales data for the first five months. Visualize the data to understand 
# the trend.
# Sample Data:
# Month: Jan, Feb, Mar, Apr, May
# Sales (Units): 120, 150, 170, 140, 180
# Task: Write a Python program to plot a line chart using Matplotlib, mark each point, and display 
# grid lines.

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 170, 140, 180]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (Units)")
plt.grid()
plt.show()

print("Task 1 Finish.")
print("======================================")

# Task 2: Product Category Sales (Bar Chart)
# Situation: The store sells four product categories. Management wants to see which category 
# performs best.
# Sample Data:
# Categories: Electronics, Clothing, Books, Toys
# Sales (Units): 500, 700, 300, 400
# Task: Create a bar chart using Matplotlib with different colors for each bar.

import matplotlib.pyplot as plt

categories = ["Electronics", "Clothing", "Books", "Toys"]
sales_units = [500, 700, 300, 400]

plt.bar(categories, sales_units, color=["blue", "orange", "green", "red"])
plt.title("Product Category Sales")
plt.xlabel("Categories")
plt.ylabel("Sales (Units)")
plt.show()

print("Task 2 Finish.")
print("======================================")

# Task 3: Category Share (Pie Chart)
# Situation: The manager wants to understand the percentage share of each category in total sales.
# Task: Create a pie chart with percentage labels and explode the 'Clothing' slice.

import matplotlib.pyplot as plt

categories = ["Electronics", "Clothing", "Books", "Toys"]
sales_units = [500, 700, 300, 400]

# explode = [0, 0.1, 0, 0]
plt.pie(sales_units, labels=categories, autopct="%.1f%%", explode=[0, 0.1, 0, 0], shadow=True)
plt.title("Category Share in Total Sales")
plt.show()
        
print("Task 3 Finish.")  
print("======================================")

# Task 4: Product Sales Comparison (Multiple Line Plot)
# Situation: Two products (A and B) were sold over five months. The manager wants to compare 
# their sales trends.
# Sample Data:
# Months: Jan, Feb, Mar, Apr, May
# Product A: 120, 150, 170, 140, 180
# Product B: 80, 100, 90, 110, 130
# Task: Plot two lines on the same graph with proper legends, titles, and grid.

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
product_a_sales = [120, 150, 170, 140, 180]
product_b_sales = [80, 100, 90, 110, 130]

plt.plot(months, product_a_sales, marker="o", label="Product A")
plt.plot(months, product_b_sales, marker="s", label="Product B")
plt.title("Product Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales (Units)")
plt.legend()
plt.grid()
plt.show()

print("Task 4 Finish.")
print("======================================")

# Task 5: Time Series Sales (Line Plot with Dates)
# Situation: Sales were recorded monthly throughout 2023. The manager wants a continuous trend 
# line.
# Task: Use pandas date_range() to generate months and plot the sales trend with rotated x-axis ticks.

import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range(start="2023-01-01", periods=12, freq="MS")
sales = [120, 140, 160, 150, 180, 200, 190, 220, 210, 240, 260, 280]

plt.plot(dates, sales, marker="o")
plt.title("Monthly Sales Trend - 2023")
plt.xlabel("Date")
plt.ylabel("Sales (Units)")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

print("Task 5 Finish.")
print("======================================")

# Task 6: Store Sales Comparison (Grouped Bar Chart)
# Situation: Two stores recorded category-wise sales. Compare their performance side by side.
# Sample Data:
# Categories: Electronics, Clothing, Books, Toys
# Store A: 500, 700, 300, 400
# Store B: 450, 600, 350, 300
# Task: Plot a grouped bar chart showing Store A and Store B side by side.

import matplotlib.pyplot as plt
import numpy as np

categories = ["Electronics", "Clothing", "Books", "Toys"]
store_a = [500, 700, 300, 400]
store_b = [450, 600, 350, 300]

x = np.arange(len(categories))
width = 0.35

plt.bar(x - width/2, store_a, width, label="Store A")
plt.bar(x + width/2, store_b, width, label="Store B")

plt.title("Store Sales Comparison")
plt.xlabel("Category")
plt.ylabel("Sales (Units)")
plt.xticks(x, categories)
plt.legend()
plt.show()

print("Task 6 Finish.")
print("======================================")

# Task 7: Exam Scores Distribution (Histogram)
# Situation: 200 students appeared in an exam. The instructor wants to see the score distribution.
# Task: Generate random data using numpy.random.normal() and visualize it using sns.histplot().

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

scores = np.random.normal(loc=70, scale=10, size=200)

sns.histplot(scores, bins=10, kde=True)

plt.title("Exam Scores Distribution")
plt.xlabel("Scores")
plt.ylabel("Number of Students")
plt.show()

print("Task 7 Finish.")
print("======================================")

# Task 8: Item Count per Category (Countplot)
# Situation: A warehouse has a record of items in categories A, B, C. Find out which category has the 
# most items.
# Sample Data: ['A','B','A','C','B','B','A','C','C','A']
# Task: Create a Seaborn countplot for category frequency.

import seaborn as sns
import matplotlib.pyplot as plt

categories = ["A", "B", "A", "C", "B", "B", "A", "C", "C", "A"]

sns.countplot(x=categories)

plt.title("Item Count per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

print("Task 8 Finish.")
print("======================================")

# Task 9: Income Spread (Boxplot)
# Situation: A company has salary data for 100 employees. HR wants to check if there are outliers.
# Task: Generate random salary data using numpy.random.normal() and create a Seaborn boxplot.

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

salary = np.random.normal(loc=50000, scale=10000, size=100)

sns.boxplot(y=salary)

plt.title("Employee Salary Distribution")
plt.ylabel("Salary")
plt.show()

print("Task 9 Finish.")
print("======================================")

# Task 10: Price Spread by Category (Multiple Boxplots)
# Situation: Product prices for four categories are available. Management wants to compare price 
# variation.
# Task: Create a DataFrame with category and price data, then plot boxplots for each category

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Category": [
        "Electronics", "Electronics", "Electronics",
        "Clothing", "Clothing", "Clothing",
        "Books", "Books", "Books",
        "Toys", "Toys", "Toys"
    ],
    "Price": [
        10000, 15000, 20000,
        500, 800, 1200,
        200, 300, 400,
        300, 600, 900
    ]
})

sns.boxplot(data=data, x="Category", y="Price")

plt.title("Price Spread by Category")
plt.xlabel("Category")
plt.ylabel("Price")
plt.show()

print("Task 10 Finish.")