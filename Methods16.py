class Dog:
    def __init__(self):
        self.__energy = 0
    def eat(self,amount):
        print("Dog is eating",str(amount)+"g of food.")
        if (self.__energy + (int(amount))/10) > 100:
            self.__energy = 100
        else:
            self.__energy += (amount/10)
    def get_energy(self):
        print("Dog is at",self.__energy,"percent energy.")
    def make_sound(self):
        print("Bark!")
class Cat:
    def __init__(self):
        self.__energy = 0
    def eat(self,amount):
        print("Cat is eating",str(amount)+"g of food.")
        if (self.__energy + (int(amount)/10)) > 100:
            self.__energy = 100
        else:
            self.__energy += (amount/10)
    def get_energy(self):
        print("Cat is at",self.__energy,"percent energy.")
    def make_sound(self):
        print("Meow!")
        
dog = Dog()
cat = Cat()
pets = [dog,cat]

for pet in pets:
    pet.eat(100)
    pet.get_energy()
    pet.make_sound()
