class Person:
    def __init__(self,in_name,in_age):
        self.name = in_name
        self.age = in_age

    def get_name(self):
        return self.name

class Customer(Person):
    def __init__(self, in_name, in_age):
        super().__init__(in_name,in_age)
        self.hasTicket = False
        self.inZoo = False

    def buy_ticket(self):
        if self.age <= 12:
            print(f"{self.name} has purchased a children's ticket for the zoo!")
        else:
            print(f"{self.name} has purchased an adult ticket for the zoo!")
        self.hasTicket = True

    def enter_zoo(self, zoo):
        if self.hasTicket:
            zoo.add_customer(self.name)
            self.hasTicket = False
            self.inZoo = True
        else:
            print("Please purchase a ticket before entering the zoo.")

    def exit_zoo(self, zoo):
        if self.inZoo:
            self.inZoo = False
            zoo.remove_customer(self.name)

class Zoo:
    def __init__(self,name="Local Zoo"):
        self.name = name
        self.animals = []
        self.customers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{self.name} has a(n) {animal}")

    def add_animals(self, animals):
        self.animals.extend(animals)
        print(f"{self.name} has many animals")

    def add_customer(self, name):
        self.customers.append(name)
        print(f"{name} has entered {self.name}")

    def remove_customer(self, name):
        self.customers.remove(name)
        print(f"{name} has left {self.name}")

    def visit_animals(self):
        for a in self.animals:
            print(f"visiting {a.get_name()}")
            a.make_noise()
            a.eat_food()

class Animal:
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def make_noise(self):
        print("Every animal makes noise")

    def eat_food(self):
        print("All creatures need sustenance")

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name} says blub, blub, blub")

    def eat_food(self):
        print(f"{self.name} eats seafood.")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name} says tweet, tweet")

    def eat_food(self):
        print(f"{self.name} eats seeds, nuts and berries.")

class Chimp(Animal):
    def __init__(self,name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name} says hoot-grunt")

    def eat_food(self):
        print(f"{self.name} eats seeds, fruit, leaves, and bark.")

"""
Test Code
"""

nycZoo = Zoo("NYC Zoo")

salmon = Fish("salmon")
robin  = Bird("robin")
bonobo = Chimp("bonobo")

animals = [salmon, robin, bonobo]

nycZoo.add_animals(animals)

alice   = Customer("Alice",   25)
bob     = Customer("Bob",     20)
charlie = Customer("Charlie", 10)
dave    = Customer("Dave",    30)

customers = [alice, bob, charlie, dave]

for customer in customers:
    customer.buy_ticket()
    customer.enter_zoo(nycZoo)

nycZoo.visit_animals()

for customer in customers:
    customer.exit_zoo(nycZoo)
