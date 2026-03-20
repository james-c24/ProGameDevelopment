class car:
    wheels = 4
    @classmethod
    def show_wheels(cls):
        print("All the cars have ",str(cls.wheels)," wheels.")
#car.show_wheels()

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def show_details(self):
        print(self.name,"received",str(self.marks),"marks.")
student1 = Student("Ralph",78)
student2 = Student("Tommy",89)
#student1.show_details()

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    bank_name = "Barclays"
    @classmethod
    def show_bank_name(cls):
        print("The name of this bank is",cls.bank_name+".")
    def deposit_money(self,deposit):
        print("£"+str(deposit),"has been deposited into your account.")
        self.balance += deposit
    def show_balance(self):
        print("There is £"+str(self.balance),"in your account.")
account1 = BankAccount("James' Account",500)
#account1.show_bank_name()
#account1.deposit_money(200)
#account1.show_balance()

class Student:
    def __init__(self,name):
        self.name = name
    school_name = "Greenwood High"
    @classmethod
    def show_school_name(cls):
        print("This student goes to",cls.school_name+".")
    def show_student_name(self):
        print("This student's name is",self.name+".")
student1 = Student("Harley")
student1.show_school_name()
student1.show_student_name()
