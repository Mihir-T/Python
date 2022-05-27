import math 
def Pythagoras():
    p=int(input('Enter the perpendicular:'))
    b=int(input('Enter the base:'))
    h=math.sqrt(p**2 + b**2)
    print("Hypotenuse is:",h)
Pythagoras()
