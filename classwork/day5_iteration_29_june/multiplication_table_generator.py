# Multiplication Table Generator
'''Problem Statement
Write a Python program that accepts a number from the user and displays its multiplication table up to 20.
Sample Output
Enter Number: 8 8 x 1 = 8 8 x 2 = 16 ... 8 x 20 = 160
---------------------------------------------------------------------------------------------------------'''
#-------------------------coding-----------------------------------------------------------------
number = int(input("Enter Number: "))
for i in range(1, 21):
    print(f"{number} x {i} = {number * i}")
#-------------------------------------------------------------------------------------------------
'''output:
Enter Number: 8
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
...
8 x 20 = 160'''