#
'''Problem Statement
A smartphone displays a low battery warning only when the battery percentage falls below 15%.
Write a Python program to accept the battery percentage.
If the battery is below 15, display:
Connect Charger Immediately
Otherwise, display nothing.
-------------------------------------------------------
Sample Input
10
---------------------------------------------------------
Sample Output
Connect Charger Immediately
----------------------------------------------------'''
#-----------------------coding---------------------------------
battery_percentage = float(input("Enter the battery percentage: "))
if battery_percentage < 15:
    print("Connect Charger Immediately")
elif battery_percentage >= 15:
    print("Battery level is sufficient")
else:
    print("Battery level is sufficient")
#--------------------------------------------------------
'''output:
enter the battery percentage: 10
Connect Charger Immediately'''