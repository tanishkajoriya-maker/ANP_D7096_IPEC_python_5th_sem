'''Problem Statement: Write a Python program to find the greatest number among two numbers.'''
#input two numbers from user
num1 = int(input("Enter first number: "))
#----------------------------------------------
#input second number from user
num2 = int(input("Enter second number: "))
#----------------------------------------------
print("-------------------------")
#finding the greatest 
if num1 > num2:
    print(num1, "is the greater than", num2)
if num2 > num1:
    print(num2, "is the greater than", num1)
else:
    print("Both numbers are equal.")
#-----------------------------------------------
'''output : 
Enter first number: 10
Enter second number: 20
-------------------------
20 is the greater than 10'''