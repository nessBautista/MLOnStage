from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass 

class Express(Coffee):
    def prepare(self):
        return "Preparing Express Coffee"

class Latte(Coffee):
    def prepare(self):
        return "Preparing Latte Coffee"

class Cappucino(Coffee):
    def prepare(self):
        return "Preparing Cappucino Coffee"

class CoffeeFactory:
    def make_coffee(self, coffee_type):
        if coffee_type == "express":
            return Express().prepare()
        elif coffee_type == "latte":
            return Latte().prepare()
        elif coffee_type == "cappucino":
            return Cappucino().prepare()
        else:
            return "Invalid coffee type"


if __name__ == "__main__":
    coffee_factory = CoffeeFactory()
    coffee = coffee_factory.make_coffee("cappucino")
    print(coffee)

    coffee = coffee_factory.make_coffee("latte")
    print(coffee)

    coffee = coffee_factory.make_coffee("express")
    print(coffee)

    coffee = coffee_factory.make_coffee("Americano")
    print(coffee)
            