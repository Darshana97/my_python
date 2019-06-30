
class Car:

    Wheels = 5   #class variable

    def __init__(self):
        self.mileage = 100          #instance variable
        self.brand = "Jaguar"       #instance variable


c1 = Car()
c2 = Car()

c1.brand = "Audi"
Car.Wheels = 4

print("c1 brand:",c1.brand, "c1 mil:",c1.mileage)
print(c2.brand,c2.mileage)
print("c1 wheels:",c1.Wheels)
print("c2 wheels:",c2.Wheels)