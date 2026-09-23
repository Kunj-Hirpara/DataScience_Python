# 1. Create a 1D NumPy array for marks obtained by 10 students.
# Options:
# a) Print the array and display dtype, shape, and size.
# b) Find the average mark and highest mark.
# c) Count how many students scored above 75.

import numpy as np

marks = np.array([65, 80, 72, 90, 55, 85, 78, 60, 95, 70])

print("Marks:", marks)
print("Data Type:", marks.dtype)
print("Shape:", marks.shape)
print("Size:", marks.size)

print("Average:", np.mean(marks))
print("Highest Mark:", np.max(marks))

print("Students above 75:", np.sum(marks > 75))

print("-------------------------------------------------------")

# 2. Create an array of body temperatures (in °C) of 8 patients.
# Options:
# a) Display the minimum and maximum temperature.
# b) Find the number of patients with temperature above 37.5°C.
# c) Change all temperatures above 39°C to 39°C.

import numpy as np

temp = np.array([36.5, 37.2, 38.1, 39.2, 36.8, 37.8, 40.1, 38.5])

print("Temperatures:", temp)

print("Minimum Temperature:", np.min(temp))
print("Maximum Temperature:", np.max(temp))

print("Patients above 37.5°C:", np.sum(temp > 37.5))

temp[temp > 39] = 39
print("Updated Temperatures:", temp)

print("-------------------------------------------------------")

# 3. Store salaries of 6 employees in an array.
# Options:
# a) Increase salaries by 15% and display updated salaries.
# b) Find the highest and lowest salary.
# c) Calculate the mean salary.

import numpy as np

salary = np.array([25000, 30000, 35000, 40000, 45000, 50000])
print("Original Salaries:", salary)

salary = salary * 1.15
print("Updated Salaries:", salary)

print("Highest Salary:", np.max(salary))
print("Lowest Salary:", np.min(salary))
print("Mean Salary:", np.mean(salary))

print("-------------------------------------------------------")

# 4. A department recorded research publications by 4 faculty members for 3 years (2D array).
# Options:
# a) Print the total publications for each faculty.
# b) Find which faculty member has the highest total publications.
# c) Print publications for Year 2 only.

import numpy as np

publications = np.array([
    [5, 7, 8],
    [4, 6, 5],
    [8, 9, 10],
    [3, 5, 7]
])

print("Publications:")
print(publications)

# Total publications for each faculty
total = np.sum(publications, axis=1)

print("Total Publications:", total)

# Faculty with highest total
faculty = np.argmax(total) + 1
print("Faculty with Highest Publications:", faculty)

# Year 2 publications
print("Year 2 Publications:", publications[:, 1])

print("-------------------------------------------------------")

# 5 . Store attendance (out of 30) for 12 students.
# Options:
# a) Display students who attended less than 20 days.
# b) Replace attendance below 15 with 15.
# c) Find the average attendance.

import numpy as np

attendance = np.array([
    25, 18, 27, 15, 22, 19,
    29, 14, 26, 20, 17, 24
])

print("Attendance:", attendance)

# Students below 20
print("Attendance below 20:")
print(attendance[attendance < 20])

# Replace below 15 with 15
attendance[attendance < 15] = 15
print("Updated Attendance:", attendance)

# Average
print("Average Attendance:", np.mean(attendance))

print("-------------------------------------------------------")

# 6. Create a 1D array showing the number of beds occupied in 7 hospital wards.
# Options:
# a) Find the ward with maximum occupancy.
# b) Replace any value below 5 with 5.
# c) Count wards with occupancy above 20.

import numpy as np

beds = np.array([15, 25, 3, 30, 18, 4, 22])
print("Beds Occupied:", beds)

# Ward with maximum occupancy
ward = np.argmax(beds) + 1
print("Ward with Maximum Occupancy:", ward)
print("Maximum Occupancy:", np.max(beds))

# Replace values below 5 with 5
beds[beds < 5] = 5
print("Updated Occupancy:", beds)

# Count above 20
print("Wards above 20:", np.sum(beds > 20))

print("-------------------------------------------------------")

# 7. Create roll numbers from 101 to 116 using np.arange().
# Options:
# a) Reshape into 4×4 and print.
# b) Print the first two rows.
# c) Print the last column.

import numpy as np

roll = np.arange(101, 117)

print("Roll Numbers:")
print(roll)

# Reshape into 4 x 4
roll = roll.reshape(4, 4)

print("\n4 x 4 Matrix:")
print(roll)

# First two rows
print("\nFirst Two Rows:")
print(roll[:2])

# Last column
print("\nLast Column:")
print(roll[:, -1])

print("-------------------------------------------------------")

# 8. A company has performance scores of 5 employees in 4 skills (2D array).
# Options:
# a) Calculate the mean score per employee.
# b) Find the employee with the highest overall score.
# c) Print scores of skill 2 for all employees.

import numpy as np

scores = np.array([
    [8, 7, 9, 8],
    [6, 8, 7, 9],
    [9, 9, 8, 10],
    [7, 6, 8, 7],
    [8, 9, 9, 8]
])

print("Performance Scores:")
print(scores)

# Mean score per employee
average = np.mean(scores, axis=1)

print("Average Score per Employee:")
print(average)

# Employee with highest overall score
employee = np.argmax(average) + 1
print("Employee with Highest Score:", employee)

# Skill 2 scores
print("Skill 2 Scores:")
print(scores[:, 1])