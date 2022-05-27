str = input("Input a string:")
d=l=0
for c in str:
    if c.isdigit():
        d+=1
    elif c.isalpha():
        l+=1
    else:
        pass
print("Letters", l)
print("Digits", d)