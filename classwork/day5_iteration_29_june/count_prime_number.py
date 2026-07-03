# Count Prime Numbers
'''Problem Statement
Accept two integers representing the starting and ending values of a range.
Display all prime numbers within the range and finally display the total number of prime numbers found.
-------------------------------------------------------------------------------------------------------'''
#--------------------------coding------------------------------------------------------------------------
start = int(input("Enter the starting value of the range: "))
end = int(input("Enter the ending value of the range: "))
prime_count = 0

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
            prime_count += 1

print(f"Total prime numbers found: {prime_count}")
#----------------------------------------------------------------------------------------------------------
'''output:
Enter the starting value of the range: 10
Enter the ending value of the range: 50
11
13
17
19
23
29
31
37
41
43
47
Total prime numbers found: 11'''