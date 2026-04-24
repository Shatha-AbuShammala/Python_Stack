class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.happiness = 100

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.color = "golden"

class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.favorite_fruit = "banana"

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.color = "brown"

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_lion(self, name):
        self.animals.append(Lion(name, 5))

    def add_tiger(self, name):
        self.animals.append(Monkey(name, 3))

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()

zoo = Zoo("John's Zoo")
zoo.add_lion("Simba")
zoo.add_lion("Nala")
zoo.add_tiger("George")
zoo.print_all_info()
zoo.animals[0].feed() 
zoo.print_all_info()