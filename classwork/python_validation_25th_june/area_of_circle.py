""" Program to calculate the area of a circle with validation"""

radius = float(input("Enter the radius of the circle: "))

if radius <= 0:
    print("Invalid input! Radius must be greater than 0.")
else:
    area = 3.14 * radius * radius
    print("Area of the circle =", area)
    """output: Enter the radius of the circle: 4
Area of the circle = 50.24"""