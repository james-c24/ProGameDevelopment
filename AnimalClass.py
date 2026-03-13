class Animals:
    def __init__(self,name,habitat,genus):
        self.name = name
        self.habitat = habitat
        self.genus = genus

    def sound(self):
        print(self.name,"is making a sound.")
    def sleep(self):
        print(self.name,"is sleeping.")

animal1 = Animals("Jerry","Land","Mammals")

animal1.sound()
