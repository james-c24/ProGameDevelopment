class Tickets:
    def __init__(self,destination,departure):
        self.destination = destination
        self.departure = departure
class Passengers(Tickets):
    def __init__(self,destination,seat_number):
        self.destination = destination
        self.seat_number = seat_number
        super().__init__(destination)
    def book_ticket(self):
        print("Passenger has booked a flight to",self.destination+".")
class Pilots(Tickets):
    def __init__(self,departure):
        self.departure = departure
        super().__init__(departure)
    def view_schedule(self):
        print("Time of flight is",self.departure+".")
class Ground_Staff(Passenger):
    def __init__(self,seat_number):
        super().__init__(seat_number)
