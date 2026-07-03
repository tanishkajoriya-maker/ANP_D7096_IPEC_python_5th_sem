#Electricity Bill Analysis
'''Problem Statement
An electricity department wants to analyze electricity consumption of N houses.
Accept the monthly units consumed by each house.
Calculate and display:
•
Total units consumed
•
Average units consumed
•
Highest consumption
•
Lowest consumption
-------------------------------------------------------------------------------------------------------'''
#------------------------------------coding-------------------------------------------------------------
n = int(input("Enter the number of houses: "))
total_units = 0
highest_consumption = float('-inf')
lowest_consumption = float('inf')

for _ in range(n):
    units = int(input("Enter the monthly units consumed: "))
    total_units += units

    if units > highest_consumption:
        highest_consumption = units

    if units < lowest_consumption:
        lowest_consumption = units
average_units = total_units / n

print(f"Total units consumed: {total_units}")
print(f"Average units consumed: {average_units}")
print(f"Highest consumption: {highest_consumption}")
print(f"Lowest consumption: {lowest_consumption}")
#---------------------------------------------------------------------------------------------------------------
'''output:
Enter the number of houses: 5
Enter the monthly units consumed: 120
Enter the monthly units consumed: 150
Enter the monthly units consumed: 180
Enter the monthly units consumed: 200
Enter the monthly units consumed: 220
Total units consumed: 970
Average units consumed: 194.0
Highest consumption: 220
Lowest consumption: 120'''
