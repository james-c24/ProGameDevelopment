class Warehouse_Product:
    def __init__(self,name,quantity):
        self.name = name
        self.__quantity = quantity
    def check_stock(self,quantity):
        print(self.name,"has",quantity,"stock remaining.")
    def restock(self,quantity):
        restock = int(input("How much of the product should be restocked? "))
        quantity += restock
        print(str(restock),"have been restocked.")
    def sell(self,quantity):
        sell = int(input("How much of the product should be sold? "))
        quantity -= sell
        print(str(sell),"have been sold.")
product1 = Warehouse_Product("Books",500)
product1.check_stock(500)
product1.restock(500)
product1.sell(550)
product1.check_stock(510)
