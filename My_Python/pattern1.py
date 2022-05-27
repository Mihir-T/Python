n = int(input("Enter the number of rows:"))
print("The pattern is:")
for i in range(n):
    for j in range(i+1):
        print("* ",end = "")
    print("")


