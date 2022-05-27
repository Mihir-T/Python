import random
import math

def Guess():
    attempts=0
    while attempts<c:
        attempts+=1
        g=int(input("Enter your guess:"))
        if(g<x):
            print("Guess higher")
        elif g>x:
            print("Guess lower")
        else :
            print("Correct! You used",attempts, "attempts!")
            break
        if attempts >= c:
            print("\nThe number is ",x)
            print("\nBetter Luck Next time!") 
        
lower,upper=1,100
c=round(math.log(upper - lower + 1, 2))     
print("You've only",c,"chances to guess number")
x=int(random.randrange(lower,upper))
Guess()

  




