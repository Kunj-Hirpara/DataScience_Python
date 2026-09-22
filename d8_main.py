import d8

# Q = 1
print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. div")

choice = int(input("Enter your choice: "))
if choice == 1:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    res = d8.add(num1,num2)
    print("Add: ", res)
elif choice == 2:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    res = d8.sub(num1,num2)
    print("Sub: ", res)
elif choice == 3:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    res = d8.mul(num1,num2)
    print("Mul: ", res)
elif choice == 4:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    res = d8.div(num1,num2)
    if num2 != 0:
        print("Div: ", res)
else:
    print("Invalid.")