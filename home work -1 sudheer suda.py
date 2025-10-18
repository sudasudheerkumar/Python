Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Name:sudheer kumar suda
# Class: CS661
# CRN: 23985

#1. Write a brief description of all the following Object Types with an example.
# Numbers (Integers and Float):
#Numbers refer to numerical values that can be either integers (e.g. -3, 0, 10) and floating point numbers (e.g. 3.14, -0.01). Integers are whole numbers without a fractional part and float numbers are numbers with a decimal point. Example: a = 10.5 b = -3.14

# Strings:Strings are sequences of characters represented by quotes (either single or double). They can be used to store text information such as names, sentences, etc. Example: name = "John Doe" message = "Welcome to the world of programming"

# Lists:   Lists are ordered collections of elements that can be of any data type including numbers, strings, and other lists. Lists are defined using square brackets and the elements are separated by commas. Example: numbers = [1, 2, 3, 4, 5] names = ["John", "Jane", "Jim", "Jack"]

# Tuples:    Tuples are similar to lists, but they are immutable, meaning their elements cannot be changed once they are assigned. They are defined using parentheses and the elements are separated by commas. Example: numbers = (1, 2, 3, 4, 5) names = ("John", "Jane", "Jim", "Jack")

# Dictionaries:  Dictionaries are unordered collections of key-value pairs, where each key is unique and maps to a specific value. Dictionaries are defined using curly braces and the key-value pairs are separated by colons. Example: person = {"name": "John Doe", "age": 30, "city": "New York"} menu = {"pizza": 10, "burger": 5, "salad": 7}



# 1. Write a brief description of all the following Object Types with an example.
#Points: 5 (3 points for explanation 2 points for example)

#Numbers (Integers and Float):


#Strings
# 2. Simple message: store a message in a variable and then print that message. After printing, change the value of the variable to a new message and print that message

message = "This is the first message."
print(message)
This is the first message.

message="this is the second message."
print(message)
this is the second message.


#3. Personal message: store a person’s name in a variable and print a simple message to that person. The message should include either! or? as well as at least one comma e.g., Hello Eric, would you like to learn more about Python?

name = "Eric"
message = "Hello " + name + ", would you like to learn more about Python?"
print(message)
Hello Eric, would you like to learn more about Python?

#4. Name Case: store a person’s name in a variable and print that person’s name in lowercase, uppercase and proper case.

name = "john doe"
lowercase = name.lower()
uppercase = name.upper()
propercase = name.title()

SyntaxError: multiple statements found while compiling a single statement
print("Lowercase:",lowercase)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print("Lowercase:",lowercase)
NameError: name 'lowercase' is not defined


name = "john doe"
lowercase = name.lower()
uppercase = name.upper()
propercase = name.title()
SyntaxError: multiple statements found while compiling a single statement


name = "john"
lowercase = name.lower()
uppercase = name.upper()
propercase = name.title()
print("Lowercase:",lowercase)
Lowercase: john
print("Uppercase:",uppercase)
Uppercase: JOHN
print("propercase:",propertcase)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print("propercase:",propertcase)
NameError: name 'propertcase' is not defined. Did you mean: 'propercase'?
print("propercase:",propercase)
propercase: John


#5. Stripping names: store a person’s name in a variable with extra white space to the left and right of the name. print the name using one of the stripping functions to remove the white space.
#5. Stripping names: store a person’s name in a variable with extra white space to the left and right of the name. print the name using one of the stripping functions to remove the white space.


name = "    John Doe    "
print(name.strip())
John Doe


#6. String Formatter: write a sentence using multiple pairs of curly braces and substitutions


name = "John Doe"
age = 26
city = "New York"
sentence = "Hello, my name is {}, I am {} years old, and I live in {}.".format(name, age, city)

print(sentence)
SyntaxError: multiple statements found while compiling a single statement

name = "john doe"
age = 26

city = "New York"
sentence = "Hello, my name is {}, I am {} years old, and I live in {}." format(name,age,city)
SyntaxError: invalid syntax
print(sentence)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print(sentence)
NameError: name 'sentence' is not defined
name = "john doe"
age = 26
city = "New York"sentence = "Hello, my name is {}, I am {} years old, and I live in {}." .format(name,age,city)
SyntaxError: invalid syntax
city = "New York"sentence = "Hello, my name is {}, I am {} years old, and I live in {}." .format(name,age,city)
SyntaxError: invalid syntax





name = "john doe"
age = 26
city = "New York"
sentence = "Hello, my name is {}, I am {} years old, and I live in {}." .format(name,age,city)
print(sentence)
Hello, my name is john doe, I am 26 years old, and I live in New York.


# Part 2: Lists

#  7. Names: store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

names = ["Suda", "Sravya", "Sudheer", "Pravallika", "Naidu"]
for name in names:
    print(name)

    
Suda
Sravya
Sudheer
Pravallika
Naidu


#  8. Greetings: start with the list that you used in number 1, print a message to each person. The text of each message should be the same, but each message should be personalized with the person’s name.

names = ["Suda", "Sravya", "Sudheer", "Pravillaka", "Naidu"]
for name in names
SyntaxError: incomplete input


names = ["Suda", "Sravya", "Sudheer", "Pravillaka", "Naidu"]
for name in names:
    print("Dear " + name + ", I hope all the guys have a nice day!")

    
Dear Suda, I hope all the guys have a nice day!
Dear Sravya, I hope all the guys have a nice day!
Dear Sudheer, I hope all the guys have a nice day!
Dear Pravillaka, I hope all the guys have a nice day!
Dear Naidu, I hope all the guys have a nice day!


#9. Guests: Using your list, create a simple message inviting each of your friends to dinner. Someone can’t make it! Modify your list, replacing the name of the guest with the name of a new person that you’re inviting.

names = ["Suda", "Sravya", "Sudheer", "Pravillaka", "Naidu"]
names[2] = 'Pavan'
print("Dear " + names[0] + ", you are cordially invited to a dinner party at my place.")
Dear Suda, you are cordially invited to a dinner party at my place.
print("Dear " + names[1] + ", you are cordially invited to a dinner party at my place.")
Dear Sravya, you are cordially invited to a dinner party at my place.
print("Dear " + names[2] + ", you are cordially invited to a dinner party at my place.")
Dear Pavan, you are cordially invited to a dinner party at my place.
print("Dear " + names[3] + ", you are cordially invited to a dinner party at my place.")
Dear Pravillaka, you are cordially invited to a dinner party at my place.
print("Dear " + names[4] + ", you are cordially invited to a dinner party at my place.")
Dear Naidu, you are cordially invited to a dinner party at my place.


# 10.More Guests: use insert() to add a new guest to the beginning, middle and end of your list. Print a new set of invitations, one for each person in the list.

names = ["Suda", "Sravya", "Sudheer", "Pravillaka", "Naidu"]
names.insert(0, 'David')
names.insert(3, 'Rockey')
names.insert(-1, 'maverick')
for name in names:
    print("Dear " + name + ", you are cordially invited to a dinner party at my place.")

    
Dear David, you are cordially invited to a dinner party at my place.
Dear Suda, you are cordially invited to a dinner party at my place.
Dear Sravya, you are cordially invited to a dinner party at my place.
Dear Rockey, you are cordially invited to a dinner party at my place.
Dear Sudheer, you are cordially invited to a dinner party at my place.
Dear Pravillaka, you are cordially invited to a dinner party at my place.
Dear maverick, you are cordially invited to a dinner party at my place.
Dear Naidu, you are cordially invited to a dinner party at my place.


#11. Hard times: you were informed that your new dinner table won’t arrive for another month, so you can only invite 2 people. Use pop() to remove guests from your list one at a time. Each time you remove a name from the list, print a message to that person letting them know that you’re sorry that you can’t invite them to dinner.



guests = ["Suda", "Sravya", "Sudheer", "Pravillaka", "Naidu"]
while len(guests) > 2:
    guest = guests.pop()
    print(f"Sorry {guest}, I won't be able to invite you to dinner.")
    print("These are the remaining guests:")
for guest in guests:
    
SyntaxError: invalid syntax
while len(guests) > 2:
    guest = guests.pop()
    print(f"Sorry {guest}, I won't be able to invite you to dinner.")
    print("These are the remaining guests:")
    for guest in guests:
        print(guest)

        
Sorry Naidu, I won't be able to invite you to dinner.
These are the remaining guests:
Suda
Sravya
Sudheer
Pravillaka
Sorry Pravillaka, I won't be able to invite you to dinner.
These are the remaining guests:
Suda
Sravya
Sudheer
Sorry Sudheer, I won't be able to invite you to dinner.
These are the remaining guests:
Suda
Sravya
>>> 
>>> 
>>> 
>>> #12.Tidying up: use del to remove the last two names from your list. Print your list to ensure that you actually have an empty list.
>>> 
>>> names = ["Suda", "Sravya", "Sudheer", "Pravillaka", "Naidu"]
>>> del names[-2:]
>>> print(names)
['Suda', 'Sravya', 'Sudheer']
>>> 
>>> 
>>> #13.Seeing the World: make a list of at least 5 places in the world that you’d like to visit. Use sorted() to print your list in alphabetical order. Show that the list is still in the original order by printing it. Use reverse() to change the order of your list and print it. Use reverse() again to change the list back to its original state.
>>> 
>>> places_to_visit = ['INDIA', 'PARIS', 'TEXAS', 'NEW YORK', 'USA']
>>> print(sorted(places_to_visit))
['INDIA', 'NEW YORK', 'PARIS', 'TEXAS', 'USA']
>>> print(places_to_visit)
['INDIA', 'PARIS', 'TEXAS', 'NEW YORK', 'USA']
>>> places_to_visit.reverse()
>>> print(places_to_visit)
['USA', 'NEW YORK', 'TEXAS', 'PARIS', 'INDIA']
