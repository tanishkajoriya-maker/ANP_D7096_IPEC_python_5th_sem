# Program to count vowels in a string
'''problem statment: write a program to input a sentence and count the number of vowels present in it.'''
#-------------------------------------coding--------------------------------------------
#input of sentence
sentence = input("Enter any sentence: ")
#initialize vowel count as 0
vowel_count = 0
for x in sentence:
    if(x=='A' or x=='a' or x=='E' or x=='e' or x=='I' or x=='i' or x=='O' or x=='o' or x=='U' or x=='u'):
        vowel_count += 1
        #incorrect vowel count 
        vowel = vowel + 1
#---------------------------------------------------------------------
print("No of vowels =", vowel_count)