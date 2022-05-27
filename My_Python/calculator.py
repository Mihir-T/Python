# Program to make a simple calculator

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Remainder")
print("6.Power")

choice = input("Enter choice(1/2/3/4/5/6): ")

if choice == '1':
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Addition is:",x+y)
    
elif choice == '2':
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Subtraction is:",x-y)
    
elif choice == '3':
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Multiplication is:",x*y)
    
elif choice == '4':
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Divison is:",x/y)   
    
elif choice == '5':
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Remainder is:",x%y)
    
elif choice == '6':
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Power of the first number  is:",x**y)
    
else:
    print("Invalid Input")
