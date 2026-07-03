#
'''problem Statement 
Write a program to input the age of 15 person. And display the person as adult whose age is greater than 18
------------------------------------------------------------------------------------------------------------------'''
#-----------------------------------------------coding-------------------------------------------------------------
age = []
#input agr of 15 person
for i in range(15):
    a = int(input("Enter the age of person {}: ".format(i+1)))
    age.append(a)

#display adult persons
print("Adult persons (age > 18):")
for i, a in enumerate(age):
    if a > 18:
        print("Person {}: {}".format(i+1, a))
#------------------------------------------------------------------------------------------------------------------
'''output:
Enter the age of person 1: 20
Enter the age of person 2: 17
Enter the age of person 3: 25
Enter the age of person 4: 15
Enter the age of person 5: 30
Enter the age of person 6: 18
Enter the age of person 7: 30
Enter the age of person 8: 22
Enter the age of person 9: 19
Enter the age of person 10: 16
Enter the age of person 11: 21
Enter the age of person 12: 17
Enter the age of person 13: 23
Enter the age of person 14: 18
Enter the age of person 15: 25
Adult persons (age > 18):
Person 1: 20
Person 3: 25
Person 5: 30
Person 7: 30
Person 8: 22
Person 9: 19
Person 11: 21
Person 13: 23
Person 15: 25'''