#  write the file and close as well..
filew = open("userhandle.txt",'w')
filew.write("Hello Hii I am Shivam Maurya.")
filew.close()


# read the file and close as well..
file = open("userhandle.txt",'r')
content = file.readlines()
print(content)
file.close()


# try with statement. automatic close the file after read and write.
with open("userhandle.txt",'r') as file:
    content = file.readlines()
    print(content)
    
    # work Chat GPT
    
with open("userhandle.txt",'w') as file:
    cont = file.write("Hello this is the new line \n and next line is this conetent.")
    print(cont)

with open("userhandle.txt",'r') as file:
    content = file.readlines()
    print(content)
    
 
    
import csv 

    # writing the csv files 

data = [['Name','Age','City'],['Alice H',30,'New Work'], ['Bob', 25, 'Los Angeles']]    
    
with open("userhandles.csv","w") as file:
    writer = csv.writer(file)
    writer.writerows(data)
        
        
# reading the csv files    
with open("./userhandles.csv",'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    
    
with open('userhandles.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Each row is a dictionary
    
# Writing dictionaries to a CSV
with open('userhandles.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'GoD', 'Age': 24, 'City': 'USA'})    
    
import json

with open('users.json', 'r') as file:
    data = json.load(file)
    print(data)  # JSON data is converted to Python dictionary
    
import json

data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

with open('users.json', 'w') as file:
    json.dump(data, file, indent=4)  # Pretty-print with indentation
    
    
    