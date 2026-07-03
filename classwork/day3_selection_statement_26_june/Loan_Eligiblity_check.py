#Problem Statement
-----------------------------------------------------------------------------------------------
'''A bank considers an applicant eligible for a personal loan only if their monthly salary is ₹30,000 or more.
Write a Python program to accept the applicant's monthly salary and display whether they are eligible to apply for the loan.
------------------------------------------------------------------------------------------------------
Sample Input 1
Enter your monthly salary: 45000
------------------------------------------------------------
Sample Output 1
Congratulations! You are eligible to apply for the loan.
--------------------------------------------------------------
Sample Input 2
Enter your monthly salary: 22000
---------------------------------------------------------------
Sample Output 2
Sorry! You are not eligible to apply for the loan.
--------------------------------------------------------------'''
#----------------coding----------------------------
# Loan Eligibility Program

salary = float(input("Enter your monthly salary: ₹"))

if salary >= 30000:
    print("Congratulations! You are eligible to apply for the loan.")
else:
    print("Sorry! You are not eligible to apply for the loan.")
    ---------------------------------------------------------------------------
   '''output 1;
    Enter your monthly salary: ₹45000
Congratulations! You are eligible to apply for the loan.
output2;
Enter your monthly salary: ₹22000
Sorry! You are not eligible to apply for the loan.'''

