class Car:
    def move(self):
        print("Driving on road.")

class Bike:
    def move(self):
        print("Riding on road.")

c = Car()
b = Bike()
vehicles = [c,b]

for vehicle in vehicles:
    vehicle.move()
