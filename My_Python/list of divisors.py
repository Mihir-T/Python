n = int(input("Enter a Number: "))
arr = []
d = 1
while(d != n+1):
    if(n % d == 0):
        arr.append(d)
    d += 1
print("List of divisors is:",arr)
