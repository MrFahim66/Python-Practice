class Vehicle():
    def __init__(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, capacity, distance):
        self.name = name
        self.capacity = int(capacity)
        self.distance = int(distance)

    def calculateFare(self):
        total = (self.capacity * (2.15 * self.distance))
        final = total + (total/100) * 10
        return final

    def printDetails(self):
        print("\nBus Details:")
        print("Bus Name:", self.name)
        print("Total Seat:", self.capacity)
        print("Travelled Distance:", self.distance)
        print("Total Fare:", self.calculateFare())


busName = input("Enter Bus Name:")
busCapacity = input("Enter Capacity:")
distance = input("Enter Distance:")

Bus1 = Bus(busName, busCapacity, distance)
Bus1.printDetails()

Bus2 = Bus("Hanif", 50, 400)
Bus2.printDetails()
