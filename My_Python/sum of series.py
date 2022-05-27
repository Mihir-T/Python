n=input("Enter Limit :")
a=2
sum=0
for x in range(0,int(n)):
	sum=sum+a
	a=a*10+2
print(sum)