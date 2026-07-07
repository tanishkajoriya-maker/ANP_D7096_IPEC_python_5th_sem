# Program to display name
'''Problem Statement: Write a program to ask the user to input the name and display the first name from it without using the library method.'''
#-------------------------------------coding--------------------------------------------
# Input of name
name = input("Enter your full name: ")
# Find the index of the first space
first_space_index = name.find(" ")
# Display the first name
print("First name:", name[:first_space_index])