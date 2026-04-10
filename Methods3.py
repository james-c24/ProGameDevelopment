class Students:
    def __init__(self,name,age,grades):
        self.name = name #public
        self._age = age #protected
        self.__grades = grades #private
    
class Bank_Account:
    def __init__(self,name,balance,bank_code):
        self.name = name #public
        self._balance = balance #protected
        self.__bank_code = bank_code #private
    def deposit(self,balance):
        deposit = int(input("How much would you like to deposit?"))
        print("£"+deposit+"has beem added to the account. Your balance is now £"+(deposit+balance)+".")
    def withdraw(self,balance):
        withdrawal = int(input("How much would you like to withdraw?"))
        print("£"+withdrawal+"has beem withdrawn from the account. Your balance is now £"+(balance-withdrawal)+".")
    def check_balance(self,balance):
        print("Your balance is currently £"+balance+".")
account1 = Bank_Account("Damian",3000,"7685")
account1.check_balance()

class Character:
    def __init__(self,name,health,secret_power):
        self.name = name #public
        self._health = health #protected
        self.__secret_power = secret_power #private
    def heal(self,health):
        heal = 10
        if self._health + heal > 100:
            health = 100
        else:
            health = health + heal
    def take_damage(self,health):
        damage = 10
        if self._health - damage < 0:
            health = 0
        else:
            health = health - damage
    def show_health(self,name,health):
        print(name,"is at",self._health,"health.")
character1 = Character("Sonic",75,"Super Speed")
character1.heal(20)
