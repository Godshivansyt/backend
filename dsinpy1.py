my_dict = {
    'name' : "Shivam",
    'age' : 24,
    'city' : "Delhi",
    'country' : "India"
}

# accessing the values 
print("Name:",my_dict['name'])
print("Age:",my_dict.get('age'))

# adding the new key-value pair
my_dict['role'] = 'Software Engineer'
print("Updated dictionary:",my_dict)

# modify the values 
my_dict['age'] = 20
print("Modified Dictionary:",my_dict)

# removing the key value pair 
del my_dict['role']
print("Dictionary after deletion:",my_dict)

# Methods to view keys, values, and items
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# Updating a dictionary
my_dict.update({'hobby': 'reading', 'age': 27})
print("After Update:", my_dict)

# Removing a key-value pair using pop
age = my_dict.pop('age')
print("Removed Age:", age)
print("Dictionary after pop:", my_dict)


# Clearing all items
my_dict.clear()
print("Dictionary after clearing:", my_dict)

# Creating a dictionary using dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print("Squares Dictionary:", squares)

# Inverting keys and values in a dictionary
inverted_dict = {v: k for k, v in my_dict.items()}
print("Inverted Dictionary:", inverted_dict)

person = {'name': 'Bob', 'age': 30, 'city': 'Boston'}

# Iterating through keys
for key in person:
    print("Key:", key)

# Iterating through values
for value in person.values():
    print("Value:", value)

# Iterating through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")


# Nested Dictionary
student = {
    'name': 'Alice',
    'courses': {
        'math': 95,
        'science': 88
    },
    'age': 20
}

print("Student Name:", student['name'])
print("Math Score:", student['courses']['math'])

# Adding a new course
student['courses']['history'] = 90
print("Updated Courses:", student['courses'])

# Chat GPT home work 
# 1.Create a dictionary that stores the names and ages of three friends.
# 2.Write a function that takes a dictionary and returns a new dictionary with only those key-value pairs where the value is greater than a certain age.
# 3.Create a nested dictionary representing a classroom with students' names as keys and another dictionary as values, which contains their subjects and corresponding marks.

# 1 solution code
fri_ends = {
    "shivam":20,
    "siddharth":21,
    "saurav":22
}

print(fri_ends)

# 2 solution code 

def diction(dictiona,agethreshold):
    filtered_dict = {name:age for name,age in dictiona.items() if age > agethreshold }
    return filtered_dict

friends_ages = {
    'John': 25,
    'Emma': 22,
    'Michael': 30
}

print(diction(friends_ages,23))

# 3 solution code

classroom = {
    "Shivam":{"math":80,"hindi":89,"science":76},
    "Shivans":{"math":84,"social":77,"art":95},
    "AngeL":{"Computer":92,"hindi":86,"English":99}
}

print("Classroom with Dictionary:",classroom)

# accessing the score of computer subject 
print("Math Score of Shivam:",classroom["AngeL"]["Computer"])

# adding the new subject in the Shivam key
classroom["Shivam"]["Computer Science"]=96
print("Updated Dictionary is : ",classroom)