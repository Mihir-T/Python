class Temperature:
    def convertFahrenheit(self,celsius):
        self.celsius=celsius
        self.fahrenheit=9*self.celsius/5 + 32
        print("Temperature in Fahrenheit is:",self.fahrenheit)
        
    def convertCelsius(self,fahrenheit):
        self.fahrenheit=fahrenheit
        self.celsius=(self.fahrenheit-32)*5/9
        print("Temperature in Celsius:",self.celsius)
        
t1=Temperature()
t1.convertFahrenheit(100)
t2=Temperature()
t2.convertCelsius(50)
