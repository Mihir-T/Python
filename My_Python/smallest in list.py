def min_in_list(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
    return min
    
list=[]
n = int(input("Enter the number of elements:"))
print("Enter the elements:") 
for i in range(0, n): 
    y = int(input()) 
    list.append(y)
print("List is:",list)
print("Largest number in the list is:",min_in_list(list))
