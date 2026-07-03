# 
'''Program to Calculate Simple Interest with Validation'''
# Program to Calculate Simple Interest with Validation

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

if principal > 0 and rate > 0 and time > 0:
    simple_interest = (principal * rate * time) / 100
    amount = principal + simple_interest

    print("Simple Interest =", simple_interest)
    print("Total Amount =", amount)
else:
    print("Invalid Input! Principal, Rate, and Time must be greater than 0.")
    #---------------------------------------------------------------------------------------
    '''output:
    Enter Principal Amount: 1000
    Enter Rate of Interest (%): 5
    Enter Time (in years): 2
    Simple Interest = 100.0
    Total Amount = 1100.0'''
