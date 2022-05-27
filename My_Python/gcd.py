a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
r = 0
if(a > b):
    while (True):
        if(b == 0):
            print("gcd is:",a)
            break
        elif(a % b == 0):
            print("gcd is:",b)
            break
        else:
            r = a % b
            a = b
            b = r
            if(a % b == 0):
                print("gcd is:",r)
                break
else:
    while (True):
        if(a == 0):
            print("gcd is:",b)
            break
        elif(b % a == 0):
            print("gcd is:",a)
            break
        else:
            r = b % a
            b = a
            a = r
            if(b % a == 0):
                print("gcd is:",r)
                break
 