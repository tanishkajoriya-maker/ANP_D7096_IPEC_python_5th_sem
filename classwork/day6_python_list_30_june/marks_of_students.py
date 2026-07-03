# Problem Statement:
''' Write a program to create a list of 15 students along withe their name display the name of student who are eligible for admission . A student is eligible if his/her marks should be above 75.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#---------------------------------------coding-------------------------------------------------------------
students = []

for i in range(15):
    name = input("Enter the name of student {}: ".format(i+1))
    marks = float(input("Enter the marks of student {}: ".format(i+1)))
    students.append((name, marks))

print("Students eligible for admission (marks > 75):")
for name, marks in students:
    if marks > 75:
        print(name)
#---------------------------------------------------------------------------------------------------------------------------------------
'''output:
Enter the name of student 1: Anjali
Enter the marks of student 1: 80
Enter the name of student 2: Ramesh
Enter the marks of student 2: 70
Enter the name of student 3: Priya
Enter the marks of student 3: 85
Enter the name of student 4: Suresh
Enter the marks of student 4: 90
Enter the name of student 5: Meera
Enter the marks of student 5: 82
Enter the name of student 6: Arjun
Enter the marks of student 6: 78
Enter the name of student 7: Sneha
Enter the marks of student 7: 88
Enter the name of student 8: Rohit
Enter the marks of student 8: 95
Enter the name of student 9: Pooja
Enter the marks of student 9: 81
Enter the name of student 10: Kartik
Enter the marks of student 10: 76
Enter the name of student 11: Nisha
Enter the marks of student 11: 89
Enter the name of student 12: Vijay
Enter the marks of student 12: 74
Enter the name of student 13: Deepa
Enter the marks of student 13: 83
Enter the name of student 14: Sunil
Enter the marks of student 14: 92
Enter the name of student 15: Rekha
Enter the marks of student 15: 79'''

