# strings
import math
print("Reem Mahmoud")
print('*'*10)

name = input('What is your name? ')
print("Hi, " + name)

favorite_color = input("What is your favorite color? ")
print(name + " likes " + favorite_color)

birth_year = int(input("What your were you born? "))
age = 2022-birth_year
print(age)
# could also use type() to see the type of something (ex: string, integer, float, etc.)
# we can write a big string (multiple lines) using three quotations

course = 'Python for Beginners'
print(course[0])  # first character
print(course[-1])  # first character from the end
print(course[0:3])  # from character 0 to 2
print(course[1:])  # from second character until the end
print(course[:5])  # from beginning until character 4
print(course[:])  # everything
print(course[1:-1])  # from character 1 until character -2 (second from the end)


first = 'Reem'
last = 'Mahmoud'
# method one
message = first + ' [' + last + '] is a coder'
# method two
msg = f'{first} [{last}] is a coder'

length = len(msg)
capital = msg.upper()
capital_first_char = msg[0].upper()
first_char_position = msg.find("R")  # returns 0
word_position = msg.find('Mahmoud')  # returns 5 b/c Mahmoud starts at char 5 (spaces are also counted as chars)
# if you call find on a character which does not  exist, it will return -1
new_word = msg.replace('coder', 'programmer')
is_in = 'Reem' in msg  # returns True

#
#
#
# Arithmetic
x = 17
cosine_of_x = math.cos(x)
# see import math at the top of the file can use the dot to get more math 'methods' i.e. things after dot
# the math module methods have things like floor and ceiling etc.
a = 10 * 3  # multiplication
b = 10 / 3  # division
c = 10 // 3  # returns the integer part only (i.e. floor, but there is a separate floor method for math)
d = 10 % 3  # mod i.e. returns remainder
e = 10 ** 3  # power
a += 3  # a=a+3, can be done with any operand
x = round(a)  # rounds the number
y = abs(b)  # absolute value

#
#
#
# if statements
is_hot = True
money = 10
if is_hot and not money > 10:
    prize = 10 * 100
    print(f'You win ${prize}')
elif is_hot or not money > 10:
    print('Not pathetic enough')
else:
    print("Hey, you're already blessed!")
# use == for equals and != for not equal

#
#
#
# while loops
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('You failed!')  # we can have else statements for while loop

command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car is already started')
        else:
            started = True
            print('Car started')
    elif command == 'stop':
        if not started:
            print('Car is already stopped')
        else:
            started = False
            print('Car stopped')
    elif command == 'help':
        print('''
start - to start the car  
stop - to stop the car
quit - to quit
        ''')
    elif command == 'quit':
        break
    else:
        print("Sorry I don't understand")
# note that we don't indent the help message since that will cause an indentation in the displayed message

#
#
#
# for loops
for item in 'Python':
    print(item)  # item will be each letter in the word Python for each iteration
for item in ['Reem', 'Salim', 'Mahmoud']:
    print(item)  # item will be each name in the list for each iteration
for item in [1, 2, 3, 4]:
    print(item)  # item will be each number in the list for each iteration
for item in range(10):
    print(item)  # item will start from 0 to 9
for item in range(5, 10):
    print(item)  # item will start from 5 to 9
for item in range(5, 10, 2):
    print(item)  # item will start from 5 to 9 taking 2 steps at a time

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

names = ['Reem', 'Salim', 'Mahmoud']
print(names[0])  # prints Reem, we can also just print names which prints the whole list as is
names[0] = 'John'

#2D lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
first_row_second_column = matrix[0][1]
for row in matrix:
    for item in row:
        print(item)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])

numbers = [1, 2, 3, 4]
numbers.append(20)  # adds 20 to the end
numbers.insert(1, 10)  # adds 10 at index 1
numbers.remove(2)  # removes 2 from list
numbers.clear()  # removes all items
numbers.pop()  # removes last item
numbers.index(3)  # returns index of first occurrence of 5
is_3_in = 3 in numbers  # returns True if 3 is in the list, otherwise False
numbers.count(3)  # counts how many 3's are in the list
numbers.sort()  # returns None if printed but sorts the list from smallest to largest
numbers.reverse()  # reverses the list, can be used to sort from largest to smallest
numbers_2 = numbers.copy()  # copies list

# Tuples
numbers = (1, 2, 3)  # can't be modified
x, y, z = numbers  # assigns 1, 2, 3 to x, y, z respectively, can be done for lists too

#
#
#
# Dictionaries
customer = {
    "name": "John Smith",  # each key should be a string or number, but the value of the key can be anything
    "email": "john@gmail.com",
    "age": 30,
    "is_verified": True
}
the_name = customer["name"]  # returns John Smith
the_name2 = customer.get("name")  # does the same thing but returns None instead of an error if the key DNE
birthdate = customer.get("birthdate", "Jan 18 1998")  # assigns default value for birthdate if it doesn't exist
customer["birthdate"] = "Jan 18 1998"  # adds this key with this value to the dictionary
customer["name"] = "Jack Smith"  # changes the value of name

message = input('> ')
words = message.split(' ')  # splits message into pieces everytime it sees a space, puts items ina list
emojis = {
    ":)": "😊",
    ";)": "😉"
}
# emojis can be accessed by pressing Windows key and dot
output = ""
for word in words:
    output += emojis.get(word, word) + " "  # prints output as is if not emoji, otherwise prints emoji
print(output)

#
#
#
# Functions


def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')


greet_user('Reem', 'Mahmoud')  # arguments are positional i.e order matters
greet_user(last_name='Mahmoud', first_name='Reem')  # specifies the keys/parameters for the arguments so order DN matter
# if you mix key arguments and positional arguments, put positional first


def square(number):
    return number * number


try:
    age = int(input('Age: '))
    print(age)
except ValueError:  # put the type of error that the program might encounter
    print("Invalid value")  # tells the program not to crash but instead print this when there is a ValueError
# can add expect for other error types

#
#
#
# Classes (creates new types/objects besides numbers, strings, boolean, lists, dictionaries etc.)


class Point:  # capitalize each point of your class name and define the methods of this class below
    def draw(self):
        print('draw')


point1 = Point()
point1.draw()  # prints draw
point1.x = 10  # can define attributes for a our object
print(point1.x)  # prints 10


class PointImproved:
    def __init__(self, xcoor, ycoor):  # this method is a constructor: it initializes the x and y of a point
        self.x = xcoor  # basically does the same thing as point1.x
        self.y = ycoor

    def xcoordinate(self):
        print(f'the xcoordinate is {self.x}')


point3 = PointImproved(10, 20)
print(point3.x)  # prints 10


# Inheritance
class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):  # lets the dog class inherit the methods of the mammal class
    def play(self):
        print('play')


class Cat(Mammal):
    pass  # means the inside of this class is empty (has no methods)

#
#
#
# Modules
# we can create modules (basically just other py files) then import them and use their functions etc


import converter  # lets us import the converter module and all its functions
kilos = converter.lbs_to_kg(70)
# in this case must write converter dot whatever
from converter import lbs_to_kg  # lets us import a specific function from the converter module
print(lbs_to_kg(70))
# in this case we don't need to write converter, only the function name

# can also import from packages (folders that hold multiple modules)
# if you have a package called utilities that has the converter module you have to do import utilities.converter
# you also have to do things like utilities.converter.lbs_to_kg() etc.

#
#
#
# random variables
import random
random.random()  # generates a random value between 0 and 1
random.randint(10, 20)  # generates a random value between 10 and 20
members = ['John', 'Smith']
leader = random.choice(members)  # generates a random value from the members list

# note that you can return tuples in a function by returning (value1,value2,etc) or just value1,value2 without parenth

#
#
#
# importing modules from paths in computer
from pathlib import Path

path = Path("utilities")  # path is 'relative' i.e. just directory, can also put 'absolute' path like C:\Windows etc
print(path.exists())
path2 = Path('emails')  # this directory doesn't exist but we can create it below
print(path2.mkdir())
print(path2.rmdir())  # deletes email directory
print(path2.glob('*'))  # searches for all directories and files inside them
path2.glob('*.py')  # searches for all py files, the returned object has all such files, so we can loop over them

# can use PyPI which has many python packages
# to install a package, the command to do so is written in the package installation place on PyPI
# you must write that command on the terminal window below then you can import the package as needed
