# 1. Create menu-driven calculator program using a module. (add, subtract, multiply, divide)

# def add(a,b):
#     return a + b

# def sub(a,b):
#     return a - b

# def mul(a,b):
#     return a * b

# def div(a,b):
#     if b != 0:
#         return a / b
#     else:
#         print("Invalid for Zero")

# ------------------------------------------------
# 2. Calculates area and volume of shapes like Circle, Rectangle, Sphere, and Cube using
# module.(two module separate module files for area and volume)

# area.py
# import math

# def circle(r):
#     return math.pi * r * r

# def rectangle(l, w):
#     return l * w

# def sphere(r):
#     return 4 * math.pi * r * r

# def cube(a):
#     return 6 * a * a

# volume.py
# import math

# def circle(r):
#     return (4 / 3) * math.pi * r * r * r

# def rectangle(l, w, h):
#     return l * w * h

# def sphere(r):
#     return (4 / 3) * math.pi * r * r * r

# def cube(a):
#     return a * a * a

# main.py
# import area
# import volume

# print("1. Circle")
# print("2. Rectangle")
# print("3. Sphere")
# print("4. Cube")

# choice = int(input("Enter choice: "))
# if choice == 1:
#     r = float(input("Enter radius: "))
#     print("Area:", area.circle(r))

# elif choice == 2:
#     l = float(input("Enter length: "))
#     w = float(input("Enter width: "))
#     print("Area:", area.rectangle(l, w))

# elif choice == 3:
#     r = float(input("Enter radius: "))
#     print("Area:", area.sphere(r))
#     print("Volume:", volume.sphere(r))

# elif choice == 4:
#     a = float(input("Enter side: "))
#     print("Area:", area.cube(a))
#     print("Volume:", volume.cube(a))

# else:
#     print("Invalid choice")

# ------------------------------------------------
# 3. Find the second largest number from a list.

# list = [7,8,9,1,2,3,4,5,6]
# list.sort()
# print("List: ", list)
# print("Second largest number: ", list[-2])

# ------------------------------------------------
# 4. Remove duplicates items from list without using set.

# def remove_duplicates(list):
#     new_list = []
#     for x in list:
#         if x not in new_list:
#             new_list.append(x)
#     return new_list

# numbers = [10, 20, 10, 30, 20, 40, 50, 30]
# print("Original List:", numbers)
# result = remove_duplicates(numbers)
# print("After Removing Duplicates:", result)

# ------------------------------------------------
# 5. Write a Python program using a nested dictionary to store student records.

students = {
    "S1": {
        "Name": "Rahul",
        "Marks": {
            "Math": 80,
            "Science": 75,
            "English": 85
        }
    },
    "S2": {
        "Name": "Priya",
        "Marks": {
            "Math": 90,
            "Science": 85,
            "English": 80
        }
    },
    "S3": {
        "Name": "Amit",
        "Marks": {
            "Math": 70,
            "Science": 80,
            "English": 75
        }
    }
}

# ------------------------------------------------
# Each student has a unique student ID, a name, and a dictionary of marks for three subjects:
# Math, Science, and English.
# Perform the following tasks:
# 1. Store the details of at least three students using a nested dictionary format.
# 2. Iterate through the dictionary and print each student’s name and their total marks.
# 3. Find topper from above program.

# Print name and total marks
for sid, data in students.items():

    total = (
        data["Marks"]["Math"]
        + data["Marks"]["Science"]
        + data["Marks"]["English"]
    )

    print("Student ID:", sid)
    print("Name:", data["Name"])
    print("Total Marks:", total)
    print()

topper = ""
highest = 0

for sid,data in students.items():
    total = (
        data["Marks"]["Math"]
        + data["Marks"]["Science"]
        + data["Marks"]["English"]
    )

    if total > highest:
        highest = total
        topper = sid

print("===== Topper =====")
print("Student ID:", topper)
print("Name:", students[topper]["Name"])
print("Total Marks:", highest)

# ------------------------------------------------
# 6. Each patient has a unique Patient ID, a name, and a dictionary of test results for three health
# parameters: Blood Pressure, Blood Sugar, and Cholesterol Level.
# Perform the following tasks:
# • Store the details of at least three patients using a nested dictionary format.
# • Iterate through the dictionary and print each patient’s name and the total of their test values.
# • Find the healthiest patient, assuming lower total test values indicate better health.

patient = {
    "p1": {
        "name": "abc",
        "test": {
            "bp": 120,
            "bs": 90,
            "col":180
        }
    },
    "p2": {
        "name": "def",
        "test": {
            "bp": 130,
            "bs": 100,
            "col": 200
        }
    },
    "p3": {
        "name": "ghi",
        "test": {
            "bp": 110,
            "bs": 85,
            "col": 170
        }
    }
}

for pid,data in patient.items():
    total = {
        data["test"]["bp"]
        +data["test"]["bs"]
        +data["test"]["col"]
    }
    print("Patient ID:", pid)
    print("Patient Name:", data["name"])
    print("Total:", total)
    print()

healthiest = ""
lowest = 999999

for pid,data in patient.items():
    total = (
        data["test"]["bp"]
        +data["test"]["bs"]
        +data["test"]["col"]
    )
    if total < lowest:
        lowest = total
        healthiest = pid

print("===== Healthiest Patient =====")
print("Patient ID:", healthiest)
print("Name:", patient[healthiest]["name"])
print("Total:", lowest)