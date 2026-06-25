"""
Arithmetic Operators – Real-Life Problem Statements

1. Monthly Salary Calculation

Scenario:
A company pays an employee a fixed monthly salary and additional incentives based on performance.

Problem Statement:
Write a Python program to calculate the total monthly salary of an employee by adding the fixed salary and incentive amount.

Input:
    - Basic Salary
    - Incentive

Output:
    - Total Salary
"""

# ---- CODE ----
salary = int(input("Enter basic salary: "))
incentive = int(input("Enter incentive: "))

total_salary = salary + incentive

print("Total Salary =", total_salary)


"""
OUTPUT:
Enter basic salary: 100000
Enter incentive: 50000
Total Salary = 150000

=== Code Execution Successful ===
"""