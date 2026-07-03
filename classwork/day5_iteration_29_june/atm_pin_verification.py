# ATM PIN Verification
'''Problem Statement
An ATM allows a user to enter the correct PIN. The correct PIN is 4589. The user can keep entering the PIN until it matches the correct one.
Display "Access Granted" when the correct PIN is entered.
---------------------------------------------------------------------------------------------------
Sample Output
Enter PIN: 1234 Incorrect PIN Enter PIN: 9876 Incorrect PIN Enter PIN: 4589 Access Granted
-----------------------------------------------------------------------------------------------------'''
#------------------------coding--------------------------------------------------
correct_pin = 4589
while True:
    pin = int(input("Enter PIN: "))
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")
#-------------------------------------------------------------------------------------
'''output:
Enter PIN: 1234
Incorrect PIN
Enter PIN: 9876
Incorrect PIN
Enter PIN: 4589
Access Granted'''