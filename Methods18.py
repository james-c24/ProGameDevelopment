class Warrior:
    def __init__(self):
        self.__health = 100
    def take_damage(self,amount):
        if self.__health - amount < 0:
            print("Character defeated.")
        else:
            self.__health -= 20
            print("Warrior has been hit.")
    def get_health(self):
        print("Warrior is at",self.__health,"health.")
    def attack(self):
        print("Sword attack!")
class Mage:
    def __init__(self):
        self.__health = 100
    def take_damage(self,amount):
        if self.__health - amount < 0:
            print("Character defeated.")
        else:
            self.__health -= 20
            print("Mage has been hit.")
    def get_health(self):
        print("Mage is at",self.__health,"health.")
    def attack(self):
        print("Magic spell!")
warrior = Warrior()
mage = Mage()
characters = [warrior,mage]
