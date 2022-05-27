class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

v1 = Vehicle(50, 8)
print("Maximum speed is:",v1.max_speed,"km/hr")
print("Mileage is :",v1.mileage,"l/100km")