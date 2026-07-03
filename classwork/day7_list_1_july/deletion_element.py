# Deletion of Elements from a List
'''Problem statement:Program to create a list of 10 numbers and delete an element at a given index'''

numbers = []

# Input 10 numbers from the user
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("\nOriginal List:", numbers)

# Ask the user for the index to delete
index = int(input("Enter the index (0-9) of the element to delete: "))

# Check if the index is valid
if 0 <= index < len(numbers):
    deleted = numbers.pop(index)
    print("Deleted element:", deleted)
    print("Updated List:", numbers)
else:
    print("Invalid index! Please enter an index between 0 and 9.")
#--------------------------------------------------------------------------------------------------------------
'''output:
Enter 10 numbers:
Enter number 1: 1
Enter number 2: 2
Enter number 3: 3
Enter number 4: 4
Enter number 5: 5
Enter number 6: 6
Enter number 7: 7
Enter number 8: 8
Enter number 9: 9
Enter number 10: 10

Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter the index (0-9) of the element to delete: 4
Deleted element: 5
Updated List: [1, 2, 3, 4, 6, 7, 8, 9, 10]
'''