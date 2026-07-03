# Number Guessing Game
'''Problem Statement
A secret number is 37.
Keep asking the user to guess the number until the correct number is entered.
Display whether the entered number is too high, too low, or correct.
-------------------------------------------------------------------------------------------------------'''
#-------------------------coding-------------------------------------------------------------------------
secret_number = 37
while True:
    guess = int(input("Guess the number: "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct!")
        break
#---------------------------------------------------------------------------------------------------------
'''output:
Guess the number: 50
Too high!
Guess the number: 25
Too low!
Guess the number: 37
Correct!'''