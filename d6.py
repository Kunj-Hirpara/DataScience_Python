import pandas as pd

data = pd.read_csv("customer.csv")
print(data)

city = input("Enter City: ")
print("Customer from: ", city)
# print(data[data["City"] == city])
# 1st data is your dataframe 
# 2nd select your dataframe column
print(data[data["City"].str.lower() == city.lower()])

print("Customer with purchase amount > 10000")
print(data[data["Purchase Amount"] > 10000])