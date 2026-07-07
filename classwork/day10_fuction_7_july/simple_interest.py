# Simple Interest Calculate
'''Problem Statement: Write a Python program to calculate simple interest.'''
#-----------------------------------coding----------------------------------------------
def calculate_simple_interest(principal, rate, time):
    # Calculate simple interest using the formula
    simple_interest = (principal * rate * time) / 100
    return simple_interest
# Input principal amount, rate of interest, and time period
principal = float(input("Enter the principal amount(in Rs.): "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period(in years): "))

# Calculate and display the simple interest
interest = calculate_simple_interest(principal, rate, time)
print(f"Simple interest: Rs. {interest}")