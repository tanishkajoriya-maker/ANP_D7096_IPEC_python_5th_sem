# count special characters in a string
'''Problem Statement: Write a program to count the number of special characters in a given sentence.'''
#----------------------------------------coding-----------------------------------------------
# Input of sentence
sentence = input("Enter any sentence: ")
# Initialize special character count as 0
special_count = 0
# Iterate through each character in the sentence
for char in sentence:
    # Check if the character is a special character (not alphanumeric)
    if not char.isalnum():
        special_count += 1
# Print the count of special characters
print("Number of special characters:", special_count)