n = int(input("Enter a positive number:"))
rem = 0
sum = 0
while n != 0:
    rem = n % 10             
    sum = sum + rem 
    n = n//10
print("Sum of digits of given number is:",sum)

