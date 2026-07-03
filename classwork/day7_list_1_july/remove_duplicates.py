# Remove duplicates from a list
'''wap to create a list of 20 number guven by user .ask the user to input any other no is present in list then remove all its duplicate occurenece from the list'''

    # Step 1: Take 20 numbers from the user
numbers = []
print("Enter 20 numbers:")

for i in range(20):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

print("\nYour list is:", numbers)

# Step 2: Ask for another number
target = int(input("\nEnter a number to remove duplicates: "))

# Step 3: Remove all duplicate occurrences
if target in numbers:
    # Keep only one occurrence of target
    new_list = []
    found = False
    for x in numbers:
        if x == target:
            if not found:   # keep the first one
                new_list.append(x)
                found = True
        else:
            new_list.append(x)
    print("\nUpdated list:", new_list)
else:
    print(f"\n{target} is not in the list")
'''output:
Enter 20 numbers:
Number 1: 1
Number 2: 2
Number 3: 3
Number 4: 4
Number 5: 5
Number 6: 6
Number 7: 7
Number 8: 8
Number 9: 9
Number 10: 10
Number 11: 11
Number 12: 12
Number 13: 13
Number 14: 14
Number 15: 15
Number 16: 16
Number 17: 17
Number 18: 18
Number 19: 19
Number 20: 20

Your list is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Enter a number to remove duplicates: 5
Updated list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]'''