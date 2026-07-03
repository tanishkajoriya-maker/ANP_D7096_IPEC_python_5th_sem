#
'''Problem Statement
A customer can withdraw money only if the requested amount does not exceed the available balance.
Accept the account balance and withdrawal amount.
•
If withdrawal amount is less than or equal to balance, display:
Transaction Successful
•
Otherwise display:
Insufficient Balance
----------------------------------------------------------------------------------
Sample Input
5000 4500
---------------------------------------------------------------------------------
Sample Output
Transaction Successful
--------------------------------------------------------------------------------'''
#---------------------coding---------------------------------------------------
account_balance = float(input("Enter the account balance: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))

if withdrawal_amount <= account_balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance")
#--------------------------------------------------------------------------------
'''output:
enter the account balance: 5000
enter the withdrawal amount: 4500
Transaction Successful'''