class Bird:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def fly(self):
        print(self.name,"can fly.")

class Parrot(Bird):
    def __init__(self, name, breed):
        super().__init__(name, breed)
    def speak(self):
        print(self.name,"can speak.")

parrot1 = Parrot("Nate","Macaw")
parrot1.fly()
parrot1.speak()
