# 1.Create a class Shape with an abstract method area(). Then create two child classes Circle and Rectangle that implement the area() method.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    # implementing the abstract method
    def area(self):
        return math.pi * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length 
        self.width = width
            
    #implement the abstract method
    def area(self):
        return self.length * self.width

# creating instances to a class
circle = Circle(5)
rectangle = Rectangle(2,4)

print("Area of the Circle is",round(circle.area(),2))
print("Area of the Rectengle is",rectangle.area())

# 2.Create a class Employee with attributes like name and salary. Create a child class Manager that inherits from Employee and adds an attribute for department. Implement methods to display employee details and manager details.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self,name, salary, department):
        super().__init__(name,salary)
        self.department = department
        
    def display_details(self):
        return super().display_details() + f", Department: {self.department}"

employee = Employee("AngeL",50000)
manager = Manager("Shivam",40000,"computer")

print(employee.display_details())
print(manager.display_details())       
        
        