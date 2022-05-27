def uppercase(str1):
    count = 0
    for letter in str1[:4]: 
        if letter.upper() == letter:
            count += 1
    if count >= 2:
        return str1.upper()
    return str1

s = input("Enter a string: ")
print(uppercase(s))
