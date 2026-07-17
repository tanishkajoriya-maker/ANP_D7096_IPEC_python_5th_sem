 #Program to count uppercase and lowercase letters in a string
'''Problem Statement: Write a program to count the uppercase characters as well as lowercase characters is given sentence, without using library function.'''
#-------------------------------------------------coding----------------------------------------------------------
sentence = input("Enter a sentence: ")
uppercase_count = 0
lowercase_count = 0
for char in sentence:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
