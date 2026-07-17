#import twodfigure

while True:

    print("\n--- Geometry Calculator ---")
    print("1. Square")
    print("2. Circle")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Exit")

    figure = int(input("Select a figure (1-5): "))

    if figure == 5:
        print("Thank you for using Geometry Calculator!")
        break

    if figure not in [1, 2, 3, 4]:
        print("Invalid Choice!")
        continue

    print("\nChoose Operation:")
    print("1. Area")
    print("2. Perimeter")

    operation = int(input("Enter choice (1-2): "))

    # ---------------- Square ----------------
    if figure == 1:
        side = float(input("Enter side: "))

        if operation == 1:
            result = twodfigures.square_area(side)
            print("Area of Square =", result)

        elif operation == 2:
            result = twodfigures.square_perimeter(side)
            print("Perimeter of Square =", result)

        else:
            print("Invalid Operation!")

    # ---------------- Circle ----------------
    elif figure == 2:
        radius = float(input("Enter radius: "))

        if operation == 1:
            result = twodfigures.circle_area(radius)
            print("Area of Circle =", round(result, 2))

        elif operation == 2:
            result = twodfigures.circle_perimeter(radius)
            print("Circumference of Circle =", round(result, 2))

        else:
            print("Invalid Operation!")

    # ---------------- Triangle ----------------
    elif figure == 3:

        if operation == 1:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            result = twodfigures.triangle_area(base, height)
            print("Area of Triangle =", result)

        elif operation == 2:
            side1 = float(input("Enter side 1: "))
            side2 = float(input("Enter side 2: "))
            side3 = float(input("Enter side 3: "))

            result = twodfigures.triangle_perimeter(side1, side2, side3)
            print("Perimeter of Triangle =", result)

        else:
            print("Invalid Operation!")

    # ---------------- Rectangle ----------------
    elif figure == 4:
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))

        if operation == 1:
            result = twodfigures.rectangle_area(length, breadth)
            print("Area of Rectangle =", result)

        elif operation == 2:
            result = twodfigures.rectangle_perimeter(length, breadth)
            print("Perimeter of Rectangle =", result)

        else:
            print("Invalid Operation!")