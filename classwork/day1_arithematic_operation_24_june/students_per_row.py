"""
5. Classroom Seating Arrangement

Scenario:
A school wants to arrange students into equal rows.

Problem Statement:
Write a Python program to determine how many complete rows can be formed.

Input:
    - Total Students
    - Students per Row

Output:
    - Number of Complete Rows
"""

# ---- CODE ----
students = int(input("Enter total students: "))
per_row = int(input("Enter students per row: "))

rows = students // per_row

print("Complete Rows =", rows)


"""
OUTPUT:
Enter total students: 20
Enter students per row: 4
Complete Rows = 5

=== Code Execution Successful ===
"""