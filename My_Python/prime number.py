n = int(input("Enter a positive number: "))
if n == 1 or n == 0:
    print("Enter a number other than 0 or 1")
elif n == 2 or n == 3 or n == 5 or n == 7:
    print("Number is prime")
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print("Number is not prime")
else:
    print("Number is prime")
