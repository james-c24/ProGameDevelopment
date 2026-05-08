class Car:
    def __init__(self):
        self.__fuel = 0
    def refuel(self,amount):
        print("Car is refueling.")
        self.__fuel += amount
    def get_fuel(self):
        print("Car has",str(self.__fuel),"litres of fuel.")
    def move(self):
        if self.__fuel - 10 < 0:
            print("Fuel too low to drive.")
        else:
            self.__fuel -= 10
            print("Car is driving.")
        
class Bike:
    def __init__(self):
        self.__fuel = 0
    def refuel(self,amount):
        print("Bike is refueling.")
        self.__fuel += amount
    def get_fuel(self):
        print("Bike has",str(self.__fuel),"litres of fuel.")
    def move(self):
        if self.__fuel - 5 < 0:
            print("Fuel too low to ride.")
        else:
            self.__fuel -= 5
            print("Bike is riding.")
car = Car()
bike = Bike()
vehicles = [car,bike]
for vehicle in vehicles:
    vehicle.refuel(5)
    vehicle.move()
    vehicle.get_fuel()
