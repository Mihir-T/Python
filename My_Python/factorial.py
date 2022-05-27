def fact(n):
    if n == 0 or n ==1:
        return 1
    else:
        f=n*fact(n-1)
        return f

num = int(input("Enter a number:"))
print("The factorial of given number is:",fact(num))
