class Student(object):
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
    def Age(self,age):
        self.age=age
        
    def setMarks(self,marks):
        self.marks=marks
        
    def Display(self):
        print("\nMy name is:",self.name)
        print("My roll no is:",self.rollno)
        print("I am",self.age,"years old")
        print("I have scored",self.marks,"marks")
        print("------------------------------")
        
n = int(input("Enter the number of students:"))
i=0
while i<n:
    name=input(("Enter name:"))
    rollno=int(input(("Enter rollno: ")))
    age=int(input(("Enter age: ")))
    marks=int(input("Enter marks: "))
    
    s=Student(name,rollno)
    s.Age(age)
    s.setMarks(marks)
    s.Display()
    i+=1

