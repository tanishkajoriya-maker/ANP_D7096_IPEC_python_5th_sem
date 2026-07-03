#Problem Statement:
'''Create a reward of 15 person along with their name and salary.Display the name of person who are eligible for EWS category . A person will be consider in EWS category if the salary is below 5 lakhs for annum.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#----------------------------------------------------coding------------------------------------------------------------------------------------------
person = []
for i in range(15):
    name = input("Enter the name of person {}: ".format(i+1))
    salary = float(input("Enter the salary of person {}: ".format(i+1)))
    person.append((name, salary))

print("Persons eligible for EWS category (salary < 5 lakhs):")
for name, salary in person:
    if salary < 500000:
        print(name)
#---------------------------------------------------------------------------------------------------------------------------------------------
'''output:
Enter the name of person 1: Anjali
Enter the salary of person 1: 600000
Enter the name of person 2: Ramesh
Enter the salary of person 2: 400000
Enter the name of person 3: Priya
Enter the salary of person 3: 450000
Enter the name of person 4: Suresh
Enter the salary of person 4: 550000
Enter the name of person 5: Meera
Enter the salary of person 5: 300000
Enter the name of person 6: Arjun
Enter the salary of person 6: 700000
Enter the name of person 7: Sneha
Enter the salary of person 7: 480000
Enter the name of person 8: Rohit
Enter the salary of person 8: 520000
Enter the name of person 9: Pooja
Enter the salary of person 9: 600000
Enter the name of person 10: Kartik
Enter the salary of person 10: 400000
Enter the name of person 11: Nisha
Enter the salary of person 11: 450000
Enter the name of person 12: Vijay
Enter the salary of person 12: 550000
Enter the name of person 13: Deepa
Enter the salary of person 13: 300000
Enter the name of person 14: Sunil
Enter the salary of person 14: 700000
Enter the name of person 15: Rekha
Enter the salary of person 15: 480000'''