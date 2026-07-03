"""
Food Delivery Business Profit Analysis

Scenario:
A food delivery startup wants to calculate its daily profit and package distribution details.

Problem Statement:
Write a Python program that:
    1. Calculates total revenue generated.
    2. Calculates profit after deducting expenses.
    3. Determines how many complete delivery boxes can be prepared.
    4. Finds remaining food packets.
    5. Predicts revenue after a certain number of days assuming revenue doubles daily.

Input:
    - Number of orders
    - Price per order
    - Daily expenses
    - Total food packets
    - Packets per box
    - Number of days

Output:
    - Total Revenue
    - Profit
    - Complete Boxes
    - Remaining Packets
    - Future Revenue
"""

# ---- CODE ----
orders = int(input("Enter number of orders: "))
price = int(input("Enter price per order: "))
expenses = int(input("Enter daily expenses: "))
packets = int(input("Enter total food packets: "))
packets_per_box = int(input("Enter packets per box: "))
days = int(input("Enter number of days: "))

revenue = orders * price
profit = revenue - expenses
boxes = packets // packets_per_box
remaining = packets % packets_per_box
future_revenue = revenue * (2 ** days)

print("Total Revenue =", revenue)
print("Profit =", profit)
print("Complete Boxes =", boxes)
print("Remaining Packets =", remaining)
print("Future Revenue =", future_revenue)


"""
OUTPUT:
Enter number of orders: 10
Enter price per order: 10
Enter daily expenses: 5
Enter total food packets: 10
Enter packets per box: 10
Enter number of days: 5
Total Revenue = 100
Profit = 95
Complete Boxes = 1
Remaining Packets = 0
Future Revenue = 3200

=== Code Execution Successful ===
"""