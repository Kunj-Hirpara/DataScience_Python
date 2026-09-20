import d4_area

print("===== Area Calculator =====")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter the choice: "))

if choice == 1:
    radius = float(input("Enter radius: "))
    result = d4_area.circle(radius)
    print("Area of circle: ", result)
elif choice == 2:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    result = d4_area.rectangle(length, width)
    print("Area of rectangle: ", result)
elif choice == 3:
    base = int(input("Enter base: "))
    height = int(input("Enter width: "))
    result = d4_area.triangle(base, height)
    print("Area of triangle: ", result)
else:
    print("Invalid Choice.")