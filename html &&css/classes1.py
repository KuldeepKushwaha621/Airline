class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self, name):
        if not self.open_sheet():
            return False
        self.passenger.append(name)
        return True 

    def open_sheet(self):
        return self.capacity - len(self.passenger)
flight = Flight(3)

people = ["Harry", "Kuldeep", "Hermionee", "Khushboo"]

for person in people:
    success = flight.add_passenger(person)

    if success:
        print(f"Addes {person} to flight succesfully.")
    else:
        print(f"No available sheet for {person}")