# Hello world
print("Hello World!")

# Draw shape
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# Varables
name = "Mahdiy"
age = "19"
print("My name is " + name + " I`m " + age + " years old")
name = "balo"
age = "23"
print("My name is " + name + " I`m " + age + " years old")

# Working on string
print("Mahdiy\nSulaymonov")
print("This is \"Oga Buga\" !!!")

# Working on string function
name = "Asal"
print(name.lower())
print(name.islower())
print(name.upper())
print(name.isupper())
print(len(name))
print(name[2])
print(name.index("A"))
print(name.replace("A", "Ka"))

# Working with numbers
num = 47
print(num + " My favorite number") # You get error
print(str(num) + " My favorite number")
num = -21
print(abs(num))
print(pow(3, 2))
print(max(21, 213))
print(min(21, 213))
print(round(34.123))

from math import *
print(ceil(3.7))
print(sqrt(81))

# Getting input from user
name = input("Enter your name: ") 
age = input("Enter your age: ") 
print("Hello " + name + "! You are " + age)

# Building basic calculator
num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")
result = int(num_1) + int(num_2) # for int 
result = float(num_1) + float(num_2) # for decimal
print(result)

# Working with Arrays
arr = ["mahdiy", "oga buga", "foo", "OMG!", "hello"]
print(arr)
print(arr[1])     # output "oga buga"
print(arr[-1])    # output hello
print(arr[1:])    # output ['oga buga', 'foo', 'OMG!', 'hello']
print(arr[1:3])   # output ['oga buga', 'foo']
arr[0] = "Jeo Doe"
print(arr)

# Array function
arr = ["mahdiy", "oga buga", "foo", "OMG!", "hello"]
numArr = [1, 2, 3, 5]
arr.append("Max")
arr.extend(numArr)
arr.insert(2, "Max")
arr.remove("foo")
arr.clear()
arr.pop()
arr.sort()
print(arr)
arr = ["mahdiy", "oga buga", "foo", "foo", "OMG!", "hello"]
print(arr.count("foo"))
numArr = [12, 2, 33, 5]
numArr.reverse()
print(numArr)
newNumArr = numArr.copy()
print(newNumArr)

# Tuples
obj = (2, 4)
obj[0] = 3 # You get error
arrTup = [(2, 4), (5, 3), (7, 4)]
print(arrTup)

# Function
def sayHi(name):
    print("Hello " + name + "!")

sayHi("Mike")
sayHi("Doe")

# Function return
def cube(num):
    return num * num * num

print(cube(2))

# if statements
isMale = True
isTall = False

if isMale: 
    print("You are Male")
else:
    print("You are not male")

if isMale or isTall: 
    print("You are Male")
else:
    print("You are not male")

if isMale and isTall: 
    print("You are Male")
else:
    print("You are not male")

if isMale and isTall: 
    print("You are Male")
elif isMale and not(isTall):
    print("You are not Tall")
elif not(isMale) and isTall:
    print("You are Tall but you are not male")
else:
    print("You are not male")

# Building better calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '/':
    print(num1 / num2)
elif op == '*':
    print(num1 * num2)
else: 
    print("Invalid operator")

# Working on objects
obj = {
    "name": "Max",
    "age": 43
}

print(obj["age"])
print(obj.get("name"))

# While loop
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done Loop")

# For Loop
arr = ["Max", "foo", "ak-47"]

for name in arr:
    print(name)

for i in range(10, 40):
    print(i)

for i in range(len(arr)):
    print(arr[i])

# 2d array
arr = [
    [1, 5, 3],
    [1, 43, 23],
    [43, 34, 37],
    [5, 2, 4]
]

print(arr[0][2])

for row in arr:
    for col in row:
        print(col)

# Try Except
try: 
    number = int(input("Enter number: "))
    print(number)
except:
    print("invalid number")

# Working with files

file = open('test.txt', "r") # Read file
file = open('test.txt', "a") # Overide
file = open('test.txt', "w") # Create Write
print(file.readable())
print(file.read())
print(file.readline())
print(file.readlines())
print(file.readlines()[1])
file.write("Hi\n")
file.close()

# Working with Classes
from students import Students
from People import People

student_1 = Students("Max", 32) 
student_2 = Students("Oga Buga", 43)
people_1 = People("Foo", 43, "+99899-769-82-93")

print(student_1.name, student_2.name)
print(student_1.getInfo())
print(people_1.getInfo())


# Source from Giraffe Academy
