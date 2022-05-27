cel = 0
fah = 0
while True:
        
        print("\nEnter a choice:\n1.Celsius to Fahrenheit\n2.Fahrenheit to Celsius")
        ch=int(input("\nChoice:"))

        if ch == 1:
                cel = float(input("\nEnter the Celsius temperature:"))
                fah = float((cel * 9 / 5) + 32)
                print("The temperature in Fahrenheit is:",fah,"℉")

        elif ch == 2:
                fah = float(input("\nEnter the Fahrenheit temperature:"))
                cel = float((fah - 32) * 5 / 9)
                print("The temperature in Celsius is:",cel,"℉")
        else:
                print("Enter a valid choice.")
        

    

