class Subscription:
    def __init__(self,name,premium_status,status_duration):
        self.name = name
        self.__premium_status = premium_status
        self.__status_duration = status_duration
    def activate(self):
        if self.__premium_status == True:
            print("Subscription is already activated.")
        else:
            self.__premium_status = True
            print("Subscription has been activated.")
    def deactivate(self):
        if self.__premium_status == False:
            print("Subscription is already inactive.")
        else:
            self.__premium_status = False
            print("Subscription has been deactivated.")
    def access_content(self):
        if self.__premium_status == True:
            print("You now have access to premium content.")
        else:
            print("You do not have access to premium content.")
subscription1 = Subscription("Sam",False,5)
subscription1.activate()
subscription1.deactivate()
subscription1.access_content()
