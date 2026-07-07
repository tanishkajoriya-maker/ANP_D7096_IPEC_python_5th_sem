# Price of a product
'''Problem Statement: write a program to create a tuple of price of 10 product given by the user display the lowest price count the number of product where price is greater than 4 thousand . Along with the price you are require to store the name of product also. while displaying lowest prize and highest prize display the name of product along with it'''
#-----------------------------------------coding-------------------------------------------------------------------

# Program to store product names and prices, then analyze them

# Step 1: Input product details
products = []
for i in range(10):
    name = input(f"Enter name of product {i+1}: ")
    price = float(input(f"Enter price of {name}: "))
    products.append((name, price))

# Step 2: Convert list to tuple
products_tuple = tuple(products)

# Step 3: Find lowest and highest priced products
lowest_product = min(products_tuple, key=lambda x: x[1])
highest_product = max(products_tuple, key=lambda x: x[1])

# Step 4: Count products with price > 4000
count_above_4000 = sum(1 for _, price in products_tuple if price > 4000)

# Step 5: Display results
print("\n--- Results ---")
print(f"Lowest priced product: {lowest_product[0]} at ₹{lowest_product[1]}")
print(f"Highest priced product: {highest_product[0]} at ₹{highest_product[1]}")
print(f"Number of products priced above ₹4000: {count_above_4000}")
