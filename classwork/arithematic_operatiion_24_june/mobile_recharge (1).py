"""
9. Mobile Recharge Plan

Scenario:
A telecom company charges a fixed amount per GB of data.

Problem Statement:
Write a Python program to calculate the total recharge amount based on the data pack selected.

Input:
    - Cost per GB
    - Number of GBs

Output:
    - Total Recharge Cost
"""

# ---- CODE ----
cost_per_gb = int(input("Enter cost per GB: "))
gb = int(input("Enter number of GBs: "))

total_cost = cost_per_gb * gb

print("Total Recharge Cost =", total_cost)


"""
OUTPUT:
Enter cost per GB: 10
Enter number of GBs: 10
Total Recharge Cost = 100

=== Code Execution Successful ===
"""