#Sampledic={‘’name”:”kelly”,”age”:25,”salary”:8000,”city”:”new york”}
#Keys=[“name”,”salary”]

Sampledic = {'name':'kelly','age':25, 'salary':8000,'city':'new york'} 
  
print("Original dictionary : ", Sampledic )

resultant = {key: Sampledic[key] for key in Sampledic.keys() 
                               & {'name', 'salary'}} 

print("Resultant dictionary is : " ,resultant) 