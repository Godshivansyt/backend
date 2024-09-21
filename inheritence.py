class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} is barks."
        
class Lion(Animal):
    def speak(self):
        return f"{self.name} is Roars."     
        

dog = Dog("Luci")
lion = Lion("King")

print(dog.speak())
print(lion.speak())        

# Polymorphism in the python 

# Common interface
def animal_sound(animal):
    animal.speak()

# Using polymorphism
animal_sound(dog)  # Output: Buddy says Woof!
animal_sound(lion)  # Output: Whiskers says Meow!
