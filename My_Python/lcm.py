a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = 0
if(a > b):
    lcm = a
else:
    lcm = b
while(1):
    if( lcm % a == 0 and lcm % b == 0 ):
        print("lcm is:",lcm)
        break
    lcm = lcm + 1
