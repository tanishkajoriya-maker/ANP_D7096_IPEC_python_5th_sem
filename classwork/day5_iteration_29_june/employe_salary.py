#Employee Salary Statistics
'''Problem Statement
A company has N employees.
Accept the salary of each employee and determine:
•
Highest salary
•
Lowest salary
•
Average salary
•
Number of employees earning more than ₹50,000
---------------------------------------------------------------------------------------------------------'''
#------------------------------------coding----------------------------------------------------------
n = int(input("Enter the number of employees: "))
total_salary = 0
highest_salary = float('-inf')
lowest_salary = float('inf')
employees_above_50k = 0

for _ in range(n):
    salary = float(input("Enter employee salary: "))
    total_salary += salary

    if salary > highest_salary:
        highest_salary = salary

    if salary < lowest_salary:
        lowest_salary = salary

    if salary > 50000:
        employees_above_50k += 1

average_salary = total_salary / n

print(f"Total Salary: {total_salary}")
print(f"Average Salary: {average_salary}")
print(f"Highest Salary: {highest_salary}")
print(f"Lowest Salary: {lowest_salary}")
print(f"Employees earning more than ₹50,000: {employees_above_50k}")
#---------------------------------------------------------------------------------------------------------
'''output:
Enter the number of employees: 5
Enter employee salary: 60000
Enter employee salary: 45000
Enter employee salary: 75000
Enter employee salary: 55000
Enter employee salary: 80000'''
