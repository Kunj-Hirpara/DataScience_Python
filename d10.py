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
# 4. A department recorded research publications by 4 faculty members for 3 years (2D array).
# Options:
# a) Print the total publications for each faculty.
# b) Find which faculty member has the highest total publications.
# c) Print publications for Year 2 only.
# 5 . Store attendance (out of 30) for 12 students.
# Options:
# a) Display students who attended less than 20 days.
# b) Replace attendance below 15 with 15.
# c) Find the average attendance.
# 6. Create a 1D array showing the number of beds occupied in 7 hospital wards.
# Options:
# a) Find the ward with maximum occupancy.
# b) Replace any value below 5 with 5.
# c) Count wards with occupancy above 20.
# 7. Create roll numbers from 101 to 116 using np.arange().
# Options:
# a) Reshape into 4×4 and print.
# b) Print the first two rows.
# c) Print the last column.
# 8. A company has performance scores of 5 employees in 4 skills (2D array).
# Options:
# a) Calculate the mean score per employee.
# b) Find the employee with the highest overall score.
# c) Print scores of skill 2 for all employees.