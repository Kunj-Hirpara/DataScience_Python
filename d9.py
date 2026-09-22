# 1. Create a Python program to store student details (Roll No, Name, and Marks) in a CSV file.
# Provide options to:
# • Add a new student record 
# • Display all records 
# • Search a student by Roll No

# import pandas as pd

# file = "students.csv"

# while True:
#     print("\n1. Add student.")
#     print("2. Display all student.")
#     print("3. Search student.")
#     print("4. Exit")

#     choice = int(input("Enter the choice: "))

#     if choice == 1:
#         rno = int(input("Enter Student RollNo: "))
#         name = input("Enter Student Name: ")
#         marks = int(input("Enter Student marks: "))

#         data = pd.DataFrame({
#             "Roll No": [rno],
#             "Name": [name],
#             "Marks": [marks]
#         })
#         data.to_csv(file, mode="a", index=False, header=False)
#         print("Student Added Successfully.")

#     elif choice == 2:
#         data = pd.read_csv(file)
#         print(data)

#     elif choice == 3:
#         rno = int(input("Enter Roll No: "))
#         data = pd.read_csv(file)
#         result = data[data["Roll No"] == rno]
#         print(result)

#     elif choice == 4:
#         break

#     else:
#         print("Invalid choice.")

print("-------------------------------------------------------")

# 2. Write a Python program to maintain product information in a CSV file with fields:
# • Product ID , Product Name , Quantity,Price 
# The program should calculate and display the total inventory value.

import pandas as pd

data = pd.read_csv("product.csv")
print(data)

data["Total"] = data["Quantity"] * data["Price"]
print("\n----- Inventory Value -----")
print(data)

total = data["Total"].sum()
print("\nTotal Inventory Value:", total)

print("-------------------------------------------------------")

# 3. Write a program that accepts a word from the user and searches for it in a text file. Display:
# • Number of occurrences of the word 
# • Whether the word exists or not

word = input("Enter a word: ")
file = open("data.txt", "r")
text = file.read()
file.close()
count = text.lower().count(word.lower())
print("Occurances: ", count)
if count > 0:
    print("Word exists.")
else:
    print("Word dose not exists.")

print("-------------------------------------------------------")

# 4. Write a Python program that reads a text file and displays:
# • Total number of characters 
# • Total number of words 
# • Total number of lines

file = open("data.txt", "r")
text = file.read()
file.close()
characters = len(text)
words = len(text.split())
lines = len(text.splitlines())
print("Total Characters:", characters)
print("Total Words:", words)
print("Total Lines:", lines)