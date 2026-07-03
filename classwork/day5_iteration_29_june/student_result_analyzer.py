#Student Result Analyzer
'''Problem Statement
A teacher wants to analyze the marks of N students.
Accept the marks of each student (out of 100).
Finally display:
•
Highest Marks
•
Lowest Marks
•
Average Marks
•
Number of students who passed (Marks ≥ 40)
•
Number of students who scored distinction (Marks ≥ 75)
----------------------------------------------------------------------------------------------------------------------'''
#-------------------------------------coding--------------------------------------------------------------------------
n = int(input("Enter the number of students: "))
marks = []

for i in range(n):
    mark = int(input(f"Enter marks for student {i+1}: "))
    marks.append(mark)

highest_marks = max(marks)
lowest_marks = min(marks)
average_marks = sum(marks) / len(marks)
passed_students = len([mark for mark in marks if mark >= 40])
distinction_students = len([mark for mark in marks if mark >= 75])

print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Number of students who passed: {passed_students}")
print(f"Number of students who scored distinction: {distinction_students}")
#-----------------------------------------------------------------------------------------------------------
'''output:
Enter the number of students: 5
Enter marks for student 1: 85
Enter marks for student 2: 90
Enter marks for student 3: 75
Enter marks for student 4: 60
Enter marks for student 5: 80
'''

