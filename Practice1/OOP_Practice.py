class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetails(self):
        print("\nName:", self.name)
        print("Age:", self.age)

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

class Parrot2(Parrot):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food

    def printDetails(self):
        print("\nName:", self.name)
        print("Age:", self.age)
        print("Food:", self.food)

bird1 = Parrot("Rio1", 25)
bird1.printDetails()

bird2 = Parrot2("Rio2",50,"BirdFood")
bird2.printDetails()
