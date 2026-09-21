# 1 Create a NumPy array of marks obtained by 8 students in a Mathematics test. Print the
# marks, and find the average mark.

import numpy as np

stu = np.array([80,90,95,78,95,75,60,65])
print("8 Student Marks: ", stu)
print("Avg of all student marks: ", np.mean(stu))

# 2 A hospital recorded the body temperatures of 10 patients in °C. Store them in a NumPy
# array, print the array, and find the highest and lowest temperature.

import numpy as np

patient = np.array([82,70,60,85,90,100,78,99,120,111])
print("Patient body temperature: ", patient)
print("Highest temperature: ", np.max(patient))
print("Lowest temperature: ", np.min(patient))

# 3 Create a NumPy array with monthly salaries of 6 employees (in ). 
# ₹ Increase all salaries by
# 10% and print the updated salaries.



# 4 A college library has 5 categories of books: Science, Arts, Commerce, Technology, and
# Literature. Store the number of books in each category in an array and find the total books in
# the library.
# 5 Store attendance (number of days present) for 12 students in a month (out of 30). Find how
# many students attended more than 25 days.
# 6 Create a 2D array (5×2) for 5 patients showing their systolic and diastolic blood pressure
# readings. Print the 3rd patient’s readings.
# 7 A department recorded the number of research papers published by 4 faculty members over
# 3 years. Store the data in a 4×3 NumPy array and print the total publications per faculty.
# 8 An organization rated employees on a scale of 1 to 10 in 5 skill areas. Create a 2D array (4
# employees × 5 skills) and calculate the average score per employee.
# 9 Generate random marks for 15 students in the range 35–100. Print only those marks that are
# above 75.
# 10 Create a NumPy array showing the number of beds occupied in each of 7 wards of a
# hospital. Find which ward has the maximum occupancy.
# 11 A university gives an annual bonus of 20,000 to every faculty member. 
# ₹
# 6 faculty salaries and add the bonus to each salary.
# Create an array of
# 12 Use np.arange() to create roll numbers for students from 101 to 120. Reshape it into a
# 4×5 matrix and print it.
# 13 Create an array for medicine dosages (in mg) for 8 patients. Any dosage below 50mg should
# be replaced with 50.
# 14 Store working hours of 7 employees for a week (in hours). Calculate the total and average
# working hours.
# 15 Create an array of marks for 10 students. Replace all marks below 40 with "Fail" and
# marks 40 and above with "Pass" using NumPy’s array operations.