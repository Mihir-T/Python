def remove_even(list):
	for x in list:
		if x%2==0:
			list.remove(x)
	return list
	
list1 = [] 
n = int(input("Enter number of elements : ")) 
print("Enter the elements") 
for i in range(0, n): 
    element = int(input()) 
  
    list1.append(element)
	
print(remove_even(list1))