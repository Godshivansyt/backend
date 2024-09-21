# polymorphism in python 
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

def animal_sound(animal: Animal):
    animal.speak()

# Create instances
dog = Dog()
cat = Cat()

# Demonstrate polymorphism
animals = [dog, cat]

for animal in animals:
    print(f"\n{type(animal).__name__}:")
    animal_sound(animal)

# Encapsulation in python 
# example of banking system small just deposit withdraw

class BankAccount:
    def __init__(self, balance,name):
        self.__balance = balance  # Private attribute
        self.__name = name

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return f"{self.__name} your bank balance is:{self.__balance}."

# Creating an instance
account = BankAccount(1000,"Shivam Maurya")
print(account.get_balance())

# Accessing methods
account.deposit(500)
print("Current Balance:", account.get_balance())  # Output: Current Balance: 1500

account.withdraw(200)
print("Current Balance:", account.get_balance())  # Output: Current Balance: 1300

# Trying to access the private attribute directly will raise an AttributeError
# print(account.__balance)  # This will cause an error



# abstraction in python example 

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Creating instances
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!



# another example of abstraction 
from abc import ABC, abstractmethod

class AbstractVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

class Car(AbstractVehicle):
    def start_engine(self):
        print("Car engine started")

    def accelerate(self):
        print("Car accelerating")

class Motorcycle(AbstractVehicle):
    def start_engine(self):
        print("Motorcycle engine started")

    def accelerate(self):
        print("Motorcycle accelerating")

# Usage
car = Car()
motorcycle = Motorcycle()

car.start_engine()
car.accelerate()

motorcycle.start_engine()
motorcycle.accelerate()

