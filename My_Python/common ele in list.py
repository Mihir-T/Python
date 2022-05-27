list1 = [] 
n = int(input("Enter number of elements : ")) 
print("Enter the elements:") 
for i in range(0, n): 
    x = int(input())   
    list1.append(x)

list2 = [] 
n = int(input("Enter number of elements : ")) 
print("Enter the elements:") 
for i in range(0, n): 
    y = int(input()) 
    list2.append(y)
	
result = False
for x in list1:
    for y in list2:
        if x == y:
            result = True
            print(result)
    break  
      
