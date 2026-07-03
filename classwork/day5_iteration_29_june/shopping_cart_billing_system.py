#Shopping Cart Billing System
'''Problem Statement
A supermarket allows a customer to purchase multiple products.
The customer first enters the number of products.
For each product, enter:
•
Product Name
•
Quantity
•
Price per Unit
Finally display:
•
Individual Product Cost
•
Total Bill Amount
•
Most Expensive Product
•
Cheapest Product
•
Average Product Cost
----------------------------------------------------------------------------------------------------------------------'''
#------------------------------------coding-----------------------------------------------------------------------
n = int(input("Enter the number of products: "))
products = []

for i in range(n):
    product_name = input(f"Enter the name of product {i+1}: ")
    quantity = int(input(f"Enter the quantity of product {i+1}: "))
    price_per_unit = float(input(f"Enter the price per unit of product {i+1}: "))
    products.append((product_name, quantity, price_per_unit))

total_bill = 0
most_expensive_product = None
cheapest_product = None
total_product_cost = 0

for product_name, quantity, price_per_unit in products:
    individual_cost = quantity * price_per_unit
    total_bill += individual_cost
    total_product_cost += individual_cost

    if most_expensive_product is None or price_per_unit > most_expensive_product[2]:
        most_expensive_product = (product_name, quantity, price_per_unit)

    if cheapest_product is None or price_per_unit < cheapest_product[2]:
        cheapest_product = (product_name, quantity, price_per_unit)

average_product_cost = total_product_cost / n if n > 0 else 0

print(f"Individual Product Cost: {individual_cost}")
print(f"Total Bill Amount: {total_bill}")
print(f"Most Expensive Product: {most_expensive_product[0]}")
print(f"Cheapest Product: {cheapest_product[0]}")
print(f"Average Product Cost: {average_product_cost:.2f}")
#------------------------------------------------------------------------------------------------------------
'''output:
Enter the number of products: 3
Enter the name of product 1: Apple
Enter the quantity of product 1: 5
Enter the price per unit of product 1: 2.0
Enter the name of product 2: Banana
Enter the quantity of product 2: 3
Enter the price per unit of product 2: 1.5
Enter the name of product 3: Orange
Enter the quantity of product 3: 4
Enter the price per unit of product 3: 2.5
Individual Product Cost: 10.0
Total Bill Amount: 26.5
Most Expensive Product: Orange
Cheapest Product: Banana
Average Product Cost: 8.83
'''