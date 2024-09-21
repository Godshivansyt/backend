# decorators in python here an example to better understand.

# Decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Applying the decorator
@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()

# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.




