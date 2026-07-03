"""
8. Online Shopping Discount

Scenario:
An e-commerce website offers a fixed discount on products.

Problem Statement:
Write a Python program to calculate the final payable amount after applying the discount.

Input:
    - Product Price
    - Discount Amount

Output:
    - Final Price
"""

# ---- CODE ----
price = int(input("Enter product price: "))
discount = int(input("Enter discount amount: "))

final_price = price - discount

print("Final Price =", final_price)


"""
OUTPUT:
Enter product price: 100
Enter discount amount: 10
Final Price = 90

=== Code Execution Successful ===
"""