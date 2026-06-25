"""
4. Bank Account Balance

Scenario:
A customer withdraws money from their bank account.

Problem Statement:
Write a Python program to calculate the remaining balance after withdrawal.

Input:
    - Current Balance
    - Withdrawal Amount

Output:
    - Remaining Balance
"""

# ---- CODE ----
balance = int(input("Enter current balance: "))
withdraw = int(input("Enter withdrawal amount: "))

remaining = balance - withdraw

print("Remaining Balance =", remaining)


"""
OUTPUT:
Enter current balance: 100000
Enter withdrawal amount: 1000
Remaining Balance = 99000

=== Code Execution Successful ===
"""