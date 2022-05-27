l, u, c, d = 0, 0, 0, 0
s = str(input("Enter your password:"))
if (len(s)>6 and len(s)<16):
	for i in s:
		if (i.islower()):
			l+=1			
		if (i.isupper()):
			u+=1			
		if (i.isdigit()):
			d+=1			
		if(i=='@'or i=='$' or i=='_' or i=='!'):
			c+=1		
if (l>=1 and u>=1 and c>=1 and d>=1 and l+c+u+d==len(s)):
	print("Valid Password")
else:
	print("Invalid Password")
