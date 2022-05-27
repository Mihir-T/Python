import math
def pascal(n):
    for i in range (0,n):
        Fn=math.factorial(i)
        for j in range(0,i+1):
            Fr=math.factorial(j)
            Fnr=math.factorial(i-j)
            p=Fn/(Fnr*Fr)
            print(int(p) ,end=" ")
        print("\n")
n=int(input("Enter n For pascal's triangle:"))
pascal(n)
