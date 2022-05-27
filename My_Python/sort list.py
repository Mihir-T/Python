list = [] 
n = int(input("Enter number of elements : ")) 
 
for i in range(0, n): 
    x = int(input()) 
  
    list.append(x) 
      
list.sort()
print("The list is sorted as:")
print(list)