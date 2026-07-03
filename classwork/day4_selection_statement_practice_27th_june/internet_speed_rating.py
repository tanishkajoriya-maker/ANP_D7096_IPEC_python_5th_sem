#
'''Problem Statement
An Internet Service Provider categorizes connection quality based on download speed.
•
Less than 25 Mbps → Slow
•
25–99 Mbps → Good
•
100 Mbps or above → Excellent
Write a Python program to display the connection quality.
-------------------------------------------------------------------------------------
Sample Input
120
---------------------------------------------------------------------------------------
Sample Output
Excellent Connection
--------------------------------------------------------------------------------------'''
#-------------------------coding--------------------------------------
download_speed = float(input("Enter the download speed (Mbps): "))

if download_speed < 25:
    print("Slow Connection")
elif 25 <= download_speed <= 99:
    print("Good Connection")
else:
    print("Excellent Connection")
#-----------------------------------------------------------------------------------------
'''output:
enter the download speed (Mbps): 120
Excellent Connection'''