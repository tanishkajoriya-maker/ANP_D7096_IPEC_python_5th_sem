"""
10. Event Management Budget

Scenario:
An event manager wants to calculate the cost contribution per participant.

Problem Statement:
Write a Python program to calculate how much each participant should pay.

Input:
    - Total Event Cost
    - Number of Participants

Output:
    - Amount per Participant
"""

# ---- CODE ----
event_cost = int(input("Enter total event cost: "))
participants = int(input("Enter number of participants: "))

amount = event_cost / participants

print("Amount per Participant =", amount)


"""
OUTPUT:
Enter total event cost: 10000
Enter number of participants: 100
Amount per Participant = 100.0

=== Code Execution Successful ===
"""S