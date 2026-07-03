#
'''Problem Statement
A university provides a scholarship only to students who score 90 or above.
Write a Python program to accept a student's percentage and determine whether the student is eligible.
•
If percentage is 90 or above, display:
Scholarship Approved
•
Otherwise display:
Scholarship Not Approved
--------------------------------------------------------------
Sample Input
92
-------------------------------------------------------------
Sample Output
Scholarship Approved
#-------------------------------------------------------------------'''
# -------------------coding--------------------------------------
percentage = float(input("Enter the student's percentage: "))
if percentage >= 90:
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")
#--------------------------------------------------------
'''output:
enter the student's percentage: 92
Scholarship Approved'''