x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

if x > y:
    max = x
    if max > z:
        print("Maximum of 3 numbers is:",max)
    else:
        max = z
        print("Maximum of 3 numbers is:",max)
elif y > z:
    max = y
    if max > x:
        print("Maximum of 3 numbers is:",max)
    else:
        max = x
        print("Maximum of 3 numbers is:",max)
else:
    max = z
    print("Maximum of 3 numbers is:",z)