"""
3. Fuel Consumption Tracker

Scenario:
A person wants to calculate the average fuel consumption of a car.

Problem Statement:
Write a Python program to find the average mileage of a car.

Input:
    - Total distance traveled (km)
    - Fuel consumed (liters)
"""

# ---- CODE ----
distance = float(input("Enter distance traveled (km): "))
fuel = float(input("Enter fuel consumed (liters): "))

mileage = distance / fuel

print("Mileage =", mileage, "km/l")


"""
OUTPUT:
Enter distance traveled (km): 10
Enter fuel consumed (liters): 10
Mileage = 1.0 km/l

=== Code Execution Successful ===
"""