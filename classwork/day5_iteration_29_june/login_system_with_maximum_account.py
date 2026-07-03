#Login System with Maximum Attempts
'''Problem Statement
A system allows only three login attempts.
The correct username is admin and the password is python123.
If the credentials are correct, display "Login Successful".
Otherwise, after three unsuccessful attempts, display "Account Locked".
--------------------------------------------------------------------------------------------------------------------------
Sample Output
Attempt 1 Username: admin Password: abc Invalid Credentials Attempt 2 Username: admin Password: python123 Login Successful
-----------------------------------------------------------------------------------------------------------------------'''
#-------------------------------------coding----------------------------------------------
username = "admin"
password = "python123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user_input_username = input("Username: ")
    user_input_password = input("Password: ")

    if user_input_username == username and user_input_password == password:
        print("Login Successful")
        break
    else:
        attempts += 1
        print("Invalid Credentials")

if attempts == max_attempts:
    print("Account Locked")
#---------------------------------------------------------------------------------------------------------
'''output:
Attempt 1 
Username: admin 
Password: abc 
Invalid Credentials
 Attempt 2 
 Username: admin 
 Password: python123 
 Login Successful
'''