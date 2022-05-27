x = input("Enter a string: ")
 
w = ""
for i in x:
    w = i + w
 
if (x == w):
    print("String is Palindrome.")
else:
    print("String is not Palindrome.")