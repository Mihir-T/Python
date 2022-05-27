x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

if x < y:
    min = x
    if min < z:
        print("Minimum of 3 numbers is:",min)
    else:
        min = z
        print("Minimum of 3 numbers is:",min)
elif y < z:
    min = y
    if min < x:
        print("Minimum of 3 numbers is:",min)
    else:
        min = x
        print("Minimum of 3 numbers is:",min)
elif z < x:
    min = z
    if min < y:
        print("Minimum of 3 numbers is:",min)
    else:
        min = y
        print("Minimum of 3 numbers is:",min)
else:
    print("Numbers are equal")