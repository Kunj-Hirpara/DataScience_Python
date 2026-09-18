employees = {
    "e1": {
        "Name": "Rahul",
        "Work Quality": 8,
        "Attendance": 9,
        "Punctuality": 7
    },
    "e2": {
        "Name": "Priya",
        "Work Quality": 9,
        "Attendance": 8,
        "Punctuality": 9
    },
    "e3": {
        "Name": "Amit",
        "Work Quality": 7,
        "Attendance": 8,
        "Punctuality": 6
    },
    "e4": {
        "Name": "Neha",
        "Work Quality": 8,
        "Attendance": 9,
        "Punctuality": 8
    }
}

scores = {}

# Calculate total performance score
print("----- Total Performance Scores -----")
for emp_id, data in employees.items():
    total = data["Work Quality"] + data["Attendance"] + data["Punctuality"]
    scores[emp_id] = total
    print(emp_id, employees[emp_id]["Name"], ":", total)

# Find best employee
best_emp = max(scores, key=scores.get)
print("\n----- Best Employee -----")
print("ID: ", best_emp)
print("Name: ", employees[best_emp]["Name"])
print("Score: ", scores[best_emp])

# Average Score
avg = sum(scores.values()) / len(scores)
print("\nAverage Score: ", avg)

# Employees scoring above average
print("\n----- Employees Above Average -----")
for emp_id, data in scores.items():
    if data > avg:
        print(emp_id, employees[emp_id]["Name"], ":", data)