#
'''Problem Statement
Create a simple Bank Account class that allows users to deposit and withdraw money.
#------------------------------------------------------------------------------------
Requirement
1.Create a class BankAccount.
2.Define the following instance variables:
account_number
customer_name
balance
3.Create the following methods:
accept_details() – Accept account details from the user.
deposit(amount) – Add the amount to the balance.
withdraw(amount) – Deduct the amount if sufficient balance is available; otherwise display "Insufficient Balance".
display_balance() – Display account details and current balance.
4.
Create an object of the class.
5.
Accept a deposit amount and a withdrawal amount from the user and perform both operations.
#------------------------------------------------------------------------------------
Sample Input
Enter Account Number : 1001
Enter Customer Name : Anjali
Enter Initial Balance : 5000
Enter Deposit Amount : 2000
Enter Withdrawal Amount : 4500
#------------------------------------------------------------------------------------------
Expected Output
Deposit Successful.
Withdrawal Successful.
------ Account Details ------
Account Number : 1001
Customer Name : Anjali
Current Balance: 2500
#------------------------------------------------------------------------------------------
Sample Output (Insufficient Balance)
Enter Withdrawal Amount : 9000
Insufficient Balance.
------ Account Details ------
Account Number : 1001
Customer Name : Anjali
Current Balance: 7000
#-----------------------------------------------------------------------------------------'''
#---------------------------------------------coding--------------------------------------
class BankAccount:
    def __init__(self):
        self.account_number = None
        self.customer_name = None
        self.balance = 0

    def accept_details(self):
        self.account_number = input("Enter Account Number : ")
        self.customer_name = input("Enter Customer Name : ")
        self.balance = float(input("Enter Initial Balance : "))

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successful.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")

    def display_balance(self):
        print("------ Account Details ------")
        print("Account Number :", self.account_number)
        print("Customer Name :", self.customer_name)
        print("Current Balance:", self.balance)


# Create object and perform operations
account1 = BankAccount()
account1.accept_details()

deposit_amount = float(input("Enter Deposit Amount : "))
account1.deposit(deposit_amount)

withdraw_amount = float(input("Enter Withdrawal Amount : "))
account1.withdraw(withdraw_amount)

account1.display_balance()
#---------------------------------------------------------------------------
#----------------------------------output---------------------------------
