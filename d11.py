# 1. Create a 2D array for 5 patients (Systolic, Diastolic).
# Options:
# a) Print blood pressure of the 3rd patient.
# b) Display all diastolic readings.
# c) Replace all systolic readings below 100 with 100.

import numpy as np

bp = np.array([
    [120, 80],
    [90, 60],
    [140, 90],
    [95, 65],
    [130, 85]
])

print("Blood Pressure:")
print(bp)

# a) 3rd patient's blood pressure
print("\n3rd Patient:", bp[2])

# b) All diastolic readings
print("Diastolic Readings:", bp[:, 1])

# c) Replace systolic below 100 with 100
bp[bp[:, 0] < 100, 0] = 100

print("Updated Blood Pressure:")
print(bp)

print("-------------------------------------------------------")

# 2. Store number of books in 6 categories.
# Options:
# a) Find the total number of books.
# b) Replace any category with less than 50 books to 50.
# c) Print books in categories 3 to 5.

import numpy as np

books = np.array([100, 45, 80, 30, 60, 120])
print("Books:", books)

# a) Total books
print("Total Books:", np.sum(books))

# b) Replace below 50 with 50
books[books < 50] = 50
print("Updated Books:", books)

# c) Categories 3 to 5
print("Categories 3 to 5:", books[2:5])

print("-------------------------------------------------------")

# 3. Generate 12 random marks between 30–100.
# Options:
# a) Print only marks above 60.
# b) Replace marks below 40 with “Fail”.
# c) Find how many marks are in the range 70–90.

import numpy as np

marks = np.random.randint(30, 101, 12)
print("Marks:", marks)

# a) Marks above 60
print("Marks Above 60:", marks[marks > 60])

# b) Replace marks below 40 with Fail
result = np.where(marks < 40, "Fail", marks)
print("Updated Marks:", result)

# c) Count marks between 70 and 90
count = np.sum((marks >= 70) & (marks <= 90))
print("Marks between 70 and 90:", count)

print("-------------------------------------------------------")

# 4. Store weekly working hours of 7 employees.
# Options:
# a) Find total and average working hours.
# b) Print hours of employees who worked less than 35 hours.
# c) Increase hours by 2 for all employees.

import numpy as np

hours = np.array([40, 32, 45, 38, 30, 42, 35])
print("Working Hours:", hours)

# a) Total and average
print("Total Hours:", np.sum(hours))
print("Average Hours:", np.mean(hours))

# b) Employees who worked less than 35
print("Less than 35 Hours:", hours[hours < 35])

# c) Increase hours by 2
hours = hours + 2
print("Updated Hours:", hours)

print("-------------------------------------------------------")

# 5. Create an array of annual salaries for 5 faculty members.
# Options:
# a) Add a fixed bonus of 25,000 to each salary.
# b) Find the faculty member with the lowest salary after bonus.
# c) Print salaries greater than 8,00,000.

import numpy as np

salary = np.array([600000, 750000, 850000, 900000, 700000])

# a) Add bonus of 25000
salary = salary + 25000
print("Salary After Bonus:", salary)

# b) Lowest salary
print("Lowest Salary:", np.min(salary))

# c) Salaries greater than 800000
print("Salaries Greater Than 800000:")
print(salary[salary > 800000])

print("-------------------------------------------------------")

# 6. Create an array for medicine dosages (in mg) for 10 patients.
# Options:
# a) Find the average dosage.
# b) Replace all dosages below 50mg with 50mg.
# c) Print dosages for patients 3 to 7.

import numpy as np

dosage = np.array([40, 60, 75, 45, 80, 55, 30, 90, 65, 35])

# a) Average dosage
print("Average Dosage:", np.mean(dosage))

# b) Replace below 50 with 50
dosage[dosage < 50] = 50
print("Updated Dosage:", dosage)

# c) Patients 3 to 7
print("Patients 3 to 7:", dosage[2:7])

print("-------------------------------------------------------")

# 7. Create an array of marks for 15 students.
# Options:
# a) Replace all marks below 40 with “Fail”.
# b) Count how many students passed (marks ≥ 40).
# c) Print the top 5 marks in sorted order.

import numpy as np

marks = np.array([
    35, 78, 55, 90, 42,
    30, 85, 67, 95, 38,
    72, 88, 45, 60, 25
])

# a) Replace below 40 with Fail
result = np.where(marks < 40, "Fail", marks)
print("Result:", result)

# b) Count students who passed
passed = np.sum(marks >= 40)
print("Students Passed:", passed)

# c) Top 5 marks in sorted order
sorted_marks = np.sort(marks)
print("Top 5 Marks:", sorted_marks[-5:])