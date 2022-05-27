def max_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
    
list=[]
n = int(input("Enter the number of elements:"))
print("Enter the elements:") 
for i in range(0, n): 
    y = int(input()) 
    list.append(y)
print("List is:",list)
print("Largest number in the list is:",max_in_list(list))
