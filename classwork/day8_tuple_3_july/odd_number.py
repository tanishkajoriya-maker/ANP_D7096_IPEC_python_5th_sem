# Find odd numbers in a list

'''------- Problem Statement: Display Odd Numbers from a Tuple

Write a Python program to create a tuple of 15 numbers
by taking input from the user.
Display all the odd numbers present in the tuple.
-------------------------------------------------------------'''

#------- Coding ---------------

#create an empty list
numbers = []

#to input 15 numbers
for i in range(1,16):

    num = int(input("Enter number "+str(i)+" :"))

    #store number in the list
    numbers.append(num)

#create tuple from the list
numbers = tuple(numbers)

print("--------------------------------------------")

print("Tuple is :")
print(numbers)

print("--------------------------------------------")

print("Odd Numbers are :")

#to display odd numbers
for num in numbers:

    if(num % 2 != 0):
        print(num)

#----------------------------------------------------
'''Output :
Enter number 1 :10
Enter number 2 :15
Enter number 3 :22
Enter number 4 :37
Enter number 5 :40
Enter number 6 :51
Enter number 7 :68
Enter number 8 :79
Enter number 9 :84
Enter number 10 :95
Enter number 11 :12
Enter number 12 :17
Enter number 13 :28
Enter number 14 :39
Enter number 15 :50
--------------------------------------------
Tuple is :
(10, 15, 22, 37, 40, 51, 68, 79, 84, 95, 12, 17, 28, 39, 50)
--------------------------------------------
Odd Numbers are :
15
37
51
79
95
17
39
--------------------------------------------'''