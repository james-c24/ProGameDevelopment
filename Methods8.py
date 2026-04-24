class Vehicle:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
    def start(self):
        print(self.name,"is starting.")

class Car(Vehicle):
    def __init__(self, name, colour):
        super().__init__(name, colour)
    def drive(self):
        print(self.name,"is driving.")

car1 = Car("Lexus","Red")
car1.start()
car1.drive()
