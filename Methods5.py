class Profile:
    def __init__(self,name,password):
        self.name = name
        self.__password = password
    def change_password(self):
        check = input("Input old password: ")
        if check == self.__password:
            self.__password = input(print("Correct password. Please input new password: "))
            print("Password has been changed.")
        else:
            print("Incorrect password, please try again.")
    def login(self):
        check = input(print("Please enter password to login: "))
        if check == self.__password:
            print("Succesful login.")
        else:
            print("Incorrect password. Login unsuccessful.")
profile1 = Profile("Ayden","9845")
profile1.change_password()
profile1.login()
