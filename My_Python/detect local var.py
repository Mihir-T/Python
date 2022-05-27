def abc():
    x = 10
    y = 20
    global z
    str = "Hello!"

z = 5
print("Number of local variables are:",abc.__code__.co_nlocals)
#Program to Count Number of Local Variables.
