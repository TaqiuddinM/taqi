class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity-len(self.passengers)


flight1 = Flight(3)

for person in ["Harry", "Ron", "Hermione", "Ginny"]:

    if flight1.add_passenger(person):
        print(f"Successfully added {person} in the flight")
    else:
        print(f"No room for {person}")


