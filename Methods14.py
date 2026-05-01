class CreditCard:
    def __init__(self,amount=0):
        self.amount = amount
    def process_payment(self,amount):
        print("Paid £"+amount,"using credit card.")
class DebitCard:
    def __init__(self,amount=0):
        self.amount = amount
    def process_payment(self,amount):
        print("Paid £"+amount,"using debit card.")
class UPI:
    def __init__(self,amount=0):
        self.amount = amount
    def process_payment(self,amount):
        print("Paid £"+amount,"using UPI.")

c = CreditCard()
d = DebitCard()
u = UPI()

payments = [c,d,u]
for payment in payments:
    payment.process_payment("1000")
  
