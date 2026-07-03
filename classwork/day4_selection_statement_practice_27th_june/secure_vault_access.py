#
'''Problem Statement
A digital vault can only be opened if the user enters the correct security code.
Write a Python program that accepts the entered security code. If the entered code is 7890, display:
"Access Granted to the Vault."
Otherwise, do nothing.
--------------------------------------------------------
Sample Input
7890
---------------------------------------------------------
Sample Output
Access Granted to the Vault
#-----------------------------------------------------------'''
#------------------coding------------------------------------
security_code = input("Enter the security code: ")
if security_code == "7890":
    print("Access Granted to the Vault")
#----------------------------------------------------------
'''output:
enter the security code: 7890
Access Granted to the Vault'''