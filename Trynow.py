#  Exception handling in python 

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Plese enter a valid number.")
except ZeroDivisionError:
    print("Cannot Divide by Zero.")
finally:
    print("Execution Completed.")            
    
# else and finally clauses

try: 
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot Divide by Zero.")
else:
    print("Division Was successful :", result)
finally:
    print("Execution Finished.")            


# raise error Exceptions 
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or Older.")
    print("Access Granted.")
    
try:
    check_age(18)
except ValueError as e:
    print(e)        
    
    
    # Create Your own Exceptions 
class NegativeNumberError(Exception):
    pass    

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Number must be positive.")
    print("Positive Number:", num)
    
try:
    check_number(-2)    
except NegativeNumberError as e:
    print(e)    