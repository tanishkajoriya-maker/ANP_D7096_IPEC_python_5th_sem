"""
6. Pizza Distribution

Scenario:
A party organizer wants to distribute pizza slices equally among children.

Problem Statement:
Write a Python program to find how many slices remain after equal distribution.

Input:
    - Total Pizza Slices
    - Number of Children

Output:
    - Remaining Slices
"""

# ---- CODE ----
slices = int(input("Enter total pizza slices: "))
children = int(input("Enter number of children: "))

remaining = slices % children

print("Remaining Slices =", remaining)


"""
OUTPUT:
Enter total pizza slices: 8
Enter number of children: 4
Remaining Slices = 0

=== Code Execution Successful ===
"""