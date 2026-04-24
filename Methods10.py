class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print(self.name,"makes a sound.")
    def show_name(self):
        print("This animal's name is",self.name+".")

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Lion roars.")

lion1 = Lion("Whiskers")
lion1.show_name()
lion1.sound()
