import math

"""Primitive Data Type in Python:
    1.Number
    2.Boolean
    3.String

    Variable Naming Rules:
        1.Variable Names should be descriptive and meaningful
        2.all letters should be lower-case
        3.to separate the name of two words use underscores"""

"""Input a 2D array in Python"""
# n = int(input())
# coordinates = [[int(j) for j in input().split()] for i in range(n)]

"""Reversing a string"""
string = "abacaba"
string2 = string[::-1]  # string[start:stop:step]
print(string2)
print(string == string2)

"""Sorting a string"""
a = 'ZENOVW'
b = sorted(a)
print(b)
# sorted returns a list, so you can make it a string again using join
# so,
c = ''.join(b)
print(c)

# so, in conclusion, for sorting a string we have to write the following
string = 'abacaba'
string_sorted = ''.join(sorted(string))
print(string_sorted)


course = "Python for Beginners"
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('Beginner'))
print(course.replace('Beginner', 'Absolute Begi'))
print('os' in course)
print(course.title())

print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x += 3
print(x)

# Operator Precedence : 1. parenthesis
#                       2. exponentiation
#                       3. multiplication or division
#                       4. addition or subtraction

x = 2.501
print(round(x))
print(abs(x))
print(math.trunc(x))
print(math.ceil(2))
print(math.ceil(2.0001))
print(math.floor(2))
print(math.floor(2.999999999))

is_hot = True
is_cold = True

if is_cold is not True or is_hot is not True:
    if is_hot:
        print('''It's a hot day
    Drink plenty of water''')
    elif is_cold:
        print("It's a cold day")
        print("Wear warm clothes")
    else:
        print("It's a lovely day")
    print("Enjoy your day")
else:
    print("LOL! It cannot be hot and cold simultaneously")

name = "Oggy"
if len(name) < 3:
    print("ERROR! Name must be at least 3 characters long")
elif len(name) > 50:
    print("ERROR! Name must be at most 50 characters long")
else:
    print("Name looks good")

# weight = input("Weight: ")
weight = 160
# unit = input("(L)Lbs or (K)Kg? ")
unit = 'l'
if unit.upper() == 'L':
    print(f"You are {int(weight) * 0.45}kg")
elif unit.upper() == 'K':
    print(f"You are {int(weight) / 0.45}lbs")
else:
    print("Invalid Input. Type 'L' or 'K'")


i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

# answer = 984
# i = 1
# while i <= 3:
#     guess = input("Guess : ")
#     if int(guess) == answer:
#         print("You win!")
#         break
#     i += 1
# else:
#     print("Sorry, you failed")

#########################
# Car Game

# is_started = False

# while True:
#     inp = input("> ")
#     if inp == "quit":
#         break
#     elif inp == "help":
#         print("start - to start the car")
#         print("stop - to stop the car")
#         print("quit - to exit")
#     elif inp == "start":
#         if is_started:
#             print("Car already started")
#         else:
#             is_started = True
#             print("Car started...Ready to go!")
#     elif inp == "stop":
#         if not is_started:
#             print("Car already stopped")
#         else:
#             is_started = False
#             print("Car stopped")
#     else:
#         print("I did not understand that...")


for item in 'Python':
    print(item)

for item in ["Apurbo", "Adip", "Arnob"]:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 10):
    print(item)

for item in range(5, 10, 2):
    print(item)

prices = [10, 20, 30, 40]
summation = 0
for item in prices:
    summation += item
print(summation)

for i in range(4):
    for j in range(3):
        print(f"(x, y) = ({i}, {j})")


numbers = [2, 2, 2, 2, 5]
for item in numbers:
    print("X" * item)

names = ['Apurbo', 'Adip', 'Arnob']
print(names)
print(names[0])
print(names[-1])
print(names[1:])

numbers = [1, 2, 3, 10, 984, 1000]
maximum = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]

print(maximum)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])
for row in matrix:
    for item in row:
        print(item)

numbers = [9, 8, 4, 6, 2, 1, 4]

numbers.append(22)

numbers.insert(1, 984)

print("After removing 4: ")
numbers.remove(4)
# numbers.remove(23)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(984))
# print(numbers.index(23))

print(23 in numbers)

print(numbers.count(984))
print(numbers.count(23))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(786)
print(numbers)
print(numbers2)

numbers.clear()
print(numbers)

# Eliminating Duplicates

"""Process 1: Without using built-in function"""

dup = [1, 1, 1, 2, 3, 4, 4, 4, 5, 6]
uniques = []

for numb in dup:
    if numb not in uniques:
        uniques.append(numb)

print(uniques)

"""Process 2: Using built-in function"""
dup = [1, 1, 1, 2, 3, 4, 4, 4, 5, 6]
uniques = set(dup)  # this process is done using set operation in python
print("Uniques: ", uniques)


"""Strings Terminology"""

string = "I love \"Python\" \nProgramming"
print(string)

string = "      python programming   "
print(string.upper())
print(string.lower())


print(string.title())


print(string.strip())  # removes white spaces from both ends of the string
print(string.lstrip())  # removes white spaces from only the left end of the string
print(string.rstrip())  # removes white spaces from only the left end of the string


print(string.find("pro"))
print(string.find("Pro"))


print(string.replace("p", "j"))

# to check whether a character or a sequence of characters exist in a string
print("gram" in string)

# so, find() method returns an index whereas "in" returns a boolean

# to check whether a character or sequence of characters do not exist
print("gra" not in string)

print("swift" not in string)




"""Set in Python"""

"""Set is an unordered collection of unique items and thus we cannot
    access the item of a set using index"""

# Set is represented by "{}" curly braces
first = {1, 5, 7}
first.add(4)
first.add(5)
first.add(5)
first.add(6)
print(first)

second = {2, 3, 7, 99, 45}
print(second)

union = first | second
print(union)

intersection = first & second
print(intersection)

difference = first - second
print(difference)

# Symmetric Difference (Something like "XOR" operation
sd = first ^ second  # "^" this sign is called "caret"
print(sd)

"""Set Object does not support indexing. i.e. we cannot use
    first [0] to access any item. If we want to know if there exist any
    particular item then we have go through the following process"""

if 456 in first:
    print("yes")
else:
    print("no")


# Tuples
numbers = (1, 2, 3)
print(numbers[1])
print(numbers.count(2))
print(numbers.index(3))

# Unpacking for List and Tuple

# Lists are represented by Square Brackates "[]"
# Whereas Tuples are represented by Parenthesis "()"
# Lists are mutable meaning that the can be changed
# Whereas Tuples are immutable meaning that they cannot be changed

coordinates = [1, 2, 3]
x, y, z = coordinates
print(x)
print(y)
print(z)

coordinates = (4, 5, 6)
x, y, z = coordinates
print(x)
print(y)
print(z)


# Dictionary
customer = {
    "name": "Apurbo",
    "age": 20,
    "is_verified": True
}

print(customer["name"])


"""Declaring a new empty dictionary and then add items to it"""
x = {}
x.update({'192.168.0.2': 'main'})
print(x)
x.update({'192.168.0.1': 'replica'})
print(x)

print(x['192.168.0.1'])


# In dictionary, if the key is not present, a "Key Value" Error occurs
# print(customer["Name"])
print(customer.get("name"))

# But if we use the "get" method, the absence of key does not raise
# "key Value" error rather it returns "None"

# Moreover we can pass a default value to get method in case the key
# is not present in the dictionary, the default value is returned
print(customer.get("Name"))
print(customer.get("birth_date", "Jan 1, 1990"))

customer["name"] = "Orik"
customer["age"] = 11
print(customer["name"])

# We can easily add new (key, value) pairs in dictionary
customer["birthdate"] = "April 11, 2007"
print(customer)

# Exercise for Dictionary

# phone = input("Phone Number: ")
phone = "1234/"
value = {
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine",
    '0': "Zero"
}
for digits in phone:
    print(value.get(digits, "!"))


# Emoji Converter

# message = input("> ")
message = "Good Morning Dinajpur XD"
words = message.split(' ')
emojis = {
    ":)": "🙂",  # Use (Win + .) for viewing emojis
    ":(": "😥",
    "XD": "😆",
    "-_-": "😑",
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)

# Functions

# There should be two blank lines before and after a function


def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome to Dinajpur")


print("Start")
greet_user("Hasin", "Apurbo")  # These arguments are called Positional
# Arguments meaning that their position matters

# If a parameterized function is not passed a parameter
# "Type Error" occurs
print("Finish")

# Difference between argument and parameter:
# here the "user_name" is parameter (parameter=>function definition) (p=>f)
# and "Apurbo" is the argument
# i.e. parameter is the placeholder which is used in the function for receiving informations
# whereas, arguments are the one which we pass to a function while calling it

# Keyword Arguments
greet_user(last_name="Orik", first_name="Ababil")

# Function with return statement


def square(number):
    return number * number


print(square(999))

# Emoji Converter through a function


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "🙂",  # Use (Win + .) for viewing emojis
        ":(": "😥",
        "XD": "😆",
        "-_-": "😑",
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emoji_converter("Good Morning Dinajpur :)"))

# Exception Handling
try:
    #age = int(input("Age: "))
    age = 20
    income = 20000
    risk = income / age
    print(risk)
    print(age)
except ValueError:
    print("Age cannot be nothing other than numeric values")
except ZeroDivisionError:
    print("Age cannot be zero")

# Comments

# Comments should be used to explain "Why"s and "How"s but not "What"s
# Comments should not be used in obvious situations
# It should be used only in the case when the implementation is not
# obvious.
# Comments are good but too much of a good thing is a bad thing

# to comment multiple lines just select all the desired lines
# and press CTRL+/

"""Filter Function"""
# here the "items" is a list and every item of the list is a tuple
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# i.e. here items is basically, a list of tuples

print(items)

# here we want to filter this list of tuples and show only those items
# which have price greater or equal than 10

# We can simply iterate over the list of tuples and add those tuples to
# answer that is >= 10 but there is a better and elegant approach to do
# this. The approach is as follows

filteredList = list(filter(lambda item: item[1] >= 10, items))
# here filter(function, iterable) and in this case, the function is a
# lambda function which checks whether the second item of every tuple of the
# list is greater or equal than 10. As the function is checking the second
# item of all the tuples of the list, "item[1]>=10" is used.
# And as iterable, the list "items" is passed
print(filteredList)


"""Map Function"""

# here we have a list of tuples and we want to convert this list of tuples
# to a list of integers containing only the prices of each product

# here is the naive approach to do this task

items = [           # list of tuples to be converted
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)

# now here's the better and more elegant approach to the given problem

# map(function, one or more iterables)
# here as function we will use lambda function
# and the iterable here is the list, i.e. the "items"
# "Iterable"s are List, Tuple, Map etc

items = [           # list of tuples to be converted
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

x = list(map(lambda item: item[1], items))
print(x)


"""Sorting in ASCENDING ORDER"""
numbers = [3, 51, 2, 8, 6]

numbers.sort()
print(numbers)

"""Sorting in DESCENDING ORDER"""
numbers = [3, 51, 2, 8, 6]

numbers.sort(reverse=True)
print(numbers)

"""But if we want to keep intact the original list, we have to use
"sorted()" method. This method will return a new list and the original 
list will be kept intact"""

numbers = [3, 51, 2, 8, 6]
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers)

"""But if we have list of complex item instead of having only integer
For instance, if we have a list of tuples the sorting procedure is 
as follows"""

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# the following procedure will not actually sort the list of tuples
# because Python doesn't know how to sort this list of tuples
items.sort()

# to sort this list of tuples using "sort()" method we have to do the following


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

"""Using Lambda(meaning ANONYMOUS function) function"""

"""Syntax of Lambda function: lambda parameter: expression
here "parameter" is the parameter(s) that we have to use if we define a 
function and the "expression" is what we have to return from that function"""

items2 = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

items2.sort(key=lambda item: item[1])
print(items2)


"""Stack Implementation in Python"""

browsing_session = []
print(browsing_session)

browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print("Element at the top of the stack", browsing_session[-1])

while browsing_session:
    print(browsing_session.pop())


"""
Multiple Line
Comments 
"""

# CLASSES


class Point:
    def draw(self):
        print("draw")

    def move(self):
        print("move")


point1 = Point()
point1.draw()
point1.move()

# Methods of a class has to be defined within the class
# but attributes of a class can be defined "any where" in the "program"

point1.x = 10
point1.y = 23
print(point1.x)
print(point1.y)


# Constructors

class Point:
    def __init__(self, x, y):
        # here "self.x" and "self.y" has the same effect as we were previously assigning "point1.x" and "point1.y"
        self.x = x  # here "self" is similar to "this" pointer in C++
        self.y = y  # self.x is performing job like defining an attribute and assigning it to a value passed to the constructor

    def draw(self):
        print("draw")

    def move(self):
        print("move")


point = Point(7, 82)
print(point.x)
print(point.y)
point.x = 17
print(point.x)

# Exercise for Class

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


app = Person('Apurbo')
print(app.name)
app.talk();

orik = Person("Orik")
orik.talk()

# INHERITANCE


class Mammal:
    def walk(self):
        print("Walking")


class Cat(Mammal):
    pass


class Dog(Mammal):
    def bark(self):
        print("Barking!!!")


meow = Cat()
meow.walk()

spike = Dog()
spike.walk()
spike.bark()

# MODULES

# A module in python is basically a file with python code
# it is used to break codes in different files instead of writing all the
# codes in one file
# this increases modularity and helps to reuse them
# Moreover it allows to address accidentally occurred errors very efficiently

# Again there are two ways to import a module

# 1st way
from converters import kg_to_lbs

print(kg_to_lbs(65))

#2nd way
import converters
print(converters.kg_to_lbs(67))

# So, to import a specific function of a module we use "from ... import ...
# and by this process we can use the imported function as it were defined
# in this python file

# If we use "import ...", all the functions of that module is imported
# but to to access any function, we need to prefix that function by the
# moudule name and the dot(.) operator

# Exercise for Modules
import utils
numbers = [1, 2, 4, 5, -1, 9]
print(utils.find_max(numbers))

# PACKAGES

# A Package is a container for multiple MODULES
# Instead of adding all the modules in only one directory, we can accumulate
# modules in different related directories which are called Packages

# But to convert a directory to a Package, we have to add a python file
# in that directory called "__init__.py"

# Efficiently, we can create a new Package in PyCharm by adding a new
# "Python Package" in that project folder

# Importing a specific function from a module of a package
from ecommerce.shipping import calc_shipping
calc_shipping()
calc_shipping()

# Importing the entire module of a package
from ecommerce import shipping
shipping.calc_shipping()

# Importing the entire package
import ecommerce.shipping

ecommerce.shipping.calc_shipping()


# So, we can see that if we import an entire package, to access a specific
# function we have to prefix the name of "Package" and "Module" by the dot(.)
# operator
#
# If we import a specific module from a package, we have to prefix the module
# name and a dot(.) operator to access any specific function
#
# Again if we import a specific function from a specific module of a package,
# we can simply access that function as if the function were defined in the
# current python file

# Packages are necessary for Django


# Generating Random Values

import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 20))

# Randomly picking an item from a list
members = ["Apurbo", "Adip", "Arnob"]
leader = random.choice(members)
print(leader)

# Exercise for Random

class Dice:
    def roll(self):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        return (d1, d2)


dice = Dice()
print(dice.roll())


""" Files and Directories"""
from pathlib import Path

# here pathlib is a module and as the first letter of "Path" is capital,
# "Path" is a class

# Absolute Path : A path which has the absolute definition
# Relative Path : A path from the current directory

path = Path("email")
# print(path.mkdir())  # mkdir to make a directory
# print(path.rmdir())  # rmdir to remove a directory

path = Path()
for file in path.glob('*'):
    print(file)

"""
"*" shows all the files and directories in the path
"*.*" will only show all the files, not the directories
"*.py" will only show the files having .py extension not other files
"""

""" PyPI and Pip"""




























