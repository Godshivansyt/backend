class ClassName:
    # Class attribute
    class_variable = 'I am a class variable'

    # Constructor
    def __init__(self, instance_variable):
        # Instance attribute
        self.instance_variable = instance_variable
    
    # Method
    def class_method(self):
        print("I am a method in the class.")

#  creating in a object 
# Creating an object (instance) of the class
obj = ClassName('I am an instance variable')

# Accessing class attribute
print(ClassName.class_variable)

# Accessing instance attribute
print(obj.instance_variable)

# Calling method
obj.class_method()

class Dog:
    # Class Attribute
    species = "Canis familiaris"

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to describe the dog
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Method to simulate a bark
    def bark(self, sound):
        return f"{self.name} says {sound}!"

# Creating Objects
buddy = Dog("Buddy", 4)
charlie = Dog("Charlie", 2)

# Accessing Attributes and Methods
print(buddy.description())  # Output: Buddy is 4 years old.
print(charlie.bark("Woof"))  # Output: Charlie says Woof!


# Chat GPT home work 

# 1.Create a class Car with attributes like make, model, and year. Add methods to display these details and calculate the age of the car.

# 2.Create a class Rectangle that has attributes length and width. Add methods to calculate the area and perimeter of the rectangle.

from datetime import datetime

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model 
        self.year = year 
        
    def display(self):
        return f"The car model is {self.model}"   
    
    def dis_year(self):
        return f"The car year is {self.year}"
    
    def dis_make(self):
        return f"The Car make in country by {self.make}"
    
    def calculateage(self):
        current_year = datetime.now().year
        return current_year - self.year
            
namedis = Car("India","Suzuki",2002)

print(namedis.display())
print(namedis.dis_make())
print(namedis.dis_year())        
print(namedis.calculateage())

class Rectengle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        area = self.length * self.width
        return f"The Area of this Rectengle is {area}" 

    def Perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return f"The Perimeter of this Rectengle is {perimeter}"
    
react = Rectengle(2,4)

print(react.area())    
print(react.Perimeter())