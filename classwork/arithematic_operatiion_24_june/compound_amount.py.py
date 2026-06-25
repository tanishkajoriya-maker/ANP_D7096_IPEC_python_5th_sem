"""
7. Compound Growth of Savings

Scenario:
A person invests money and wants to see how the amount grows over years.

Problem Statement:
Write a Python program to calculate the value of money after a certain number of years assuming it doubles every year.

Input:
    - Initial Amount
    - Number of Years

Output:
    - Final Amount
"""

# ---- CODE ----
amount = int(input("Enter initial amount: "))
years = int(input("Enter number of years: "))

final_amount = amount * (2 ** years)

print("Final Amount =", final_amount)


"""
OUTPUT:
Enter initial amount: 10000
Enter number of years: 2
Final Amount = 40000

=== Code Execution Successful ===
"""