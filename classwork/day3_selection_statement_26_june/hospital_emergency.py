ccc# Bonus Challenge – Hospital Emergency Triage System
'''Problem Statement
A hospital prioritizes patients based on:
•
Critical Condition
•
Age
•
Oxygen Level
Rules:
•
Critical condition → Immediate Treatment
•
Oxygen below 90 → High Priority
•
Age above 65 → Medium Priority
•
Others → Normal Priority
-------------------------------------------------------------------------
Sample Input
Critical Condition (Y/N): N Age: 70 Oxygen Level: 94
-----------------------------------------------------------------------
Sample Output
Patient Priority: Medium Priority Reason: Senior Citizen
#-----------------------------------------------------------------------------------'''
#---------------------------------coding--------------------------------------
# WAP for Hospital Emergency Triage System with Validation

try:
    critical = input("Critical Condition (Y/N): ").upper()
    age = int(input("Enter Age: "))
    oxygen = float(input("Enter Oxygen Level: "))

    # Validation
    if critical not in ['Y', 'N']:
        print("Invalid Input! Enter Y or N for Critical Condition.")

    elif age < 0:
        print("Invalid Age! Age cannot be negative.")

    elif oxygen < 0 or oxygen > 100:
        print("Invalid Oxygen Level! Enter a value between 0 and 100.")

    else:
        # Priority Decision
        if critical == 'Y':
            print("Patient Priority: Immediate Treatment")
            print("Reason: Critical Condition")

        elif oxygen < 90:
            print("Patient Priority: High Priority")
            print("Reason: Oxygen Level below 90")

        elif age > 65:
            print("Patient Priority: Medium Priority")
            print("Reason: Senior Citizen")

        else:
            print("Patient Priority: Normal Priority")
            print("Reason: Stable Condition")

except ValueError:
    print("Invalid Input! Please enter numeric values only.")
#----------------------------------------------------------------------------------
'''output:
Critical Condition (Y/N): N
Age: 70
Oxygen Level: 94
Patient Priority: Medium Priority
Reason: Senior Citizen'''