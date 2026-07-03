#
'''Problem Statement
An electricity department categorizes households based on monthly electricity consumption.
•
Up to 100 units → Low Consumption
•
101–300 units → Moderate Consumption
•
Above 300 units → High Consumption
Write a Python program to display the consumption category.
--------------------------------------------------------------------------------------
Sample Input
245
---------------------------------------------------------------------------------------
Sample Output
Moderate Consumption
-------------------------------------------------------------------------------------'''
#---------------------------coding----------------------------------------
electricity_consumption = int(input("Enter the monthly electricity consumption (units): "))

if electricity_consumption <= 100:
    print("Low Consumption")
elif 101 <= electricity_consumption <= 300:
    print("Moderate Consumption")
else:
    print("High Consumption")
#------------------------------------------------------------------------------------------------
'''output:
enter the monthly electricity consumption (units): 245
Moderate Consumption'''