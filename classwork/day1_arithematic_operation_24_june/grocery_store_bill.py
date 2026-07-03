"""
2. Grocery Store Bill

Scenario:
A customer purchases multiple packets of rice from a grocery store.

Problem Statement:
Write a Python program to calculate the total cost of rice packets purchased.

Input:
    - Price per packet
    - Number of packets

Output:
    - Total Bill Amount
"""

# ---- CODE ----
price = int(input("Enter price per packet: "))
packets = int(input("Enter number of packets: "))

bill = price * packets

print("Total Bill =", bill)


"""
OUTPUT:
Enter price per packet: 10
Enter number of packets: 10
Total Bill = 100

=== Code Execution Successful ===
"""