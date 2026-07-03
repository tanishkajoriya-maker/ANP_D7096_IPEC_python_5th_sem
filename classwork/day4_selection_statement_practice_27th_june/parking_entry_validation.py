#
'''Problem Statement
Only vehicles having a valid parking pass are allowed to enter a private parking area.
Accept either 1 (Valid Pass) or 0 (No Pass).
•
If the input is 1, display:
Entry Allowed
•
Otherwise display:
Entry Denied
------------------------------------------
Sample Input
0
-----------------------------------------
Sample Output
Entry Denied
---------------------------------------------'''
#-------------------------coding----------------------------
parking_pass = int(input("Enter 1 for Valid Pass, 0 for No Pass: "))
if parking_pass == 1:
    print("Entry Allowed")
else:
    print("Entry Denied")
#---------------------------------------------------------
'''output:
enter 1 for Valid Pass, 0 for No Pass: 0
Entry Denied'''

