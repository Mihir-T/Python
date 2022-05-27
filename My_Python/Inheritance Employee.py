class Employee():
    
    def empid(self,empid):
        print("ID:",empid)

    def empname(self,empname):
        print("Name:",empname)

        
    def doj(self,doj):
        print("Date of joining:",doj)

        
class Salesperson(Employee):
    def sales_performed(self,sales_perfomed):
        print("Sales:",sales_perfomed)
        
    def commission_earned(self,commission_earned):
        print("Commission:",commission_earned)
    
    def salary(self,sales_performed,commission_earned):
        self.sal = sales_performed * commission_earned
        print ("Salary is:",self.sal)
        
def Employee_Details(n):
    i=0
    while i<n:
        ename=input(("\nEnter name:"))
        eid=int(input(("Enter id: ")))
        ed=input(("Enter date of joining : "))
        sp=int(input("Enter sales performed: "))
        ce=int(input("Enter the commission earned:"))
        print("Employee details:")
        e=Salesperson()
        e.empid(eid)
        e.empname(ename)
        e.doj(ed)
        e.sales_performed(sp)
        e.commission_earned(ce)
        e.salary(sp,ce)
        i+=1
        
n = int(input("Enter the number of Employees:"))
Employee_Details(n)



