#Employee Information System
'''Problem Statement: Create a dictionary where:
•
Employee ID is the key.
•
Value is another dictionary containing:
o
Name
o
Department
o
Salary
Perform the following operations:
•
Display all employee details.
•
Search for an employee using Employee ID.
•
Increase the salary of all employees by 10%.
•
Display employees belonging to a specific department entered by the user'''
#---------------------------------coding-----------------------------------------------
# Create a dictionary where Employee ID is the key
employees = {
    101: {"Name": "Aman", "Department": "HR", "Salary": 50000},
    102: {"Name": "Riya", "Department": "IT", "Salary": 60000},
    103: {"Name": "Karan", "Department": "Finance", "Salary": 55000},
    104: {"Name": "Sneha", "Department": "IT", "Salary": 65000},
    105: {"Name": "Vikram", "Department": "Marketing", "Salary": 48000}
}

# 1. Display all employee details
print("All Employee Details:")
for emp_id, details in employees.items():
    print(f"ID: {emp_id}, Name: {details['Name']}, Department: {details['Department']}, Salary: {details['Salary']}")

# 2. Search for an employee using Employee ID
search_id = int(input("\nEnter Employee ID to search: "))
if search_id in employees:
    emp = employees[search_id]
    print(f"Found -> ID: {search_id}, Name: {emp['Name']}, Department: {emp['Department']}, Salary: {emp['Salary']}")
else:
    print("Employee not found.")

# 3. Increase the salary of all employees by 10%
for emp_id in employees:
    employees[emp_id]["Salary"] *= 1.10

print("\nAfter 10% Salary Increase:")
for emp_id, details in employees.items():
    print(f"ID: {emp_id}, Name: {details['Name']}, Department: {details['Department']}, Salary: {details['Salary']}")

# 4. Display employees belonging to a specific department
dept = input("\nEnter department name to filter employees: ")
print(f"\nEmployees in {dept} Department:")
found = False
for emp_id, details in employees.items():
    if details["Department"].lower() == dept.lower():
        print(f"ID: {emp_id}, Name: {details['Name']}, Salary: {details['Salary']}")
        found = True
if not found:
    print("No employees found in this department.")
#--------------------------------------------------------------------------------------------
'''output:
All Employee Details:
ID: 101, Name: Aman, Department: HR, Salary: 50000
ID: 102, Name: Riya, Department: IT, Salary: 60000
ID: 103, Name: Karan, Department: Finance, Salary: 55000
ID: 104, Name: Sneha, Department: IT, Salary: 65000
ID: 105, Name: Vikram, Department: Marketing, Salary: 48000
Enter Employee ID to search: 103
Found -> ID: 103, Name: Karan, Department: Finance, Salary: 55000.0
After 10% Salary Increase:
ID: 101, Name: Aman, Department: HR, Salary: 55000.0
ID: 102, Name: Riya, Department: IT, Salary: 66000.0
ID: 103, Name: Karan, Department: Finance, Salary: 60500.0
ID: 104, Name: Sneha, Department: IT, Salary: 71500.0
ID: 105, Name: Vikram, Department: Marketing, Salary: 52800.0
'''
