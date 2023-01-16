## Converting a string into a list
list("hello")
# ['h', 'e', 'l', 'l', 'o']

name = "Zophie"
print(name[0])
# 'Z'
print(name[1:3])
# 'op'
print(name[-2])
# 'i'
print("Zo" in name)
# True
print("xxx" in name)
# False
for letter in name:
    print(letter)
# Z
# o
# p
# h
# i
# e


## STRING MODIFICATION
# You cannot reassign a letter in a string
name = "Zophie the cat"
print(name[7])
# "t"
# name[7] = "x"
# print(name)
# Traceback (most recent call last):
#   File "<pyshell#152>", line 1, in <module>
#     name[7] = 'x'
# TypeError: 'str' object does not support item assignment

# Modifying a string
name = "Zophie a cat"
newName = name[0:7] + "the" + name[8:12]
print(newName)
# Zophie the cat


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Mutable and Immutable Data Types
# Lists are Mutable --> values CAN be added/removed/changed
# Strings are Immutable --> CANNOT be modified "in place"
# Reference --> A value that points to data like a list
# variables don't contain a list, but a reference to the list
# A mutable value is not stored in the variable - the variable contains a reference to that mutable value
# If a mutable value is changed, the reference is changed, affecting all variables that contain that reference

# Lists are mutable and store a reference to the values
spam = [0, 1, 2, 3, 4, 5]
cheese = spam    # cheese now is assigned the same reference as spam
print(spam)    # prints out original list
cheese[1] = "Hello"    # changes the reference's data set
print(cheese)
print(spam)    # the change in the variable 'cheese' changes the reference, which also changes the variable 'spam' which contains the same reference
# [0, 1, 2, 3, 4, 5]
# [0, 'Hello', 2, 3, 4, 5]
# [0, 'Hello', 2, 3, 4, 5]


# Another reference example  --> Python does this rather than make a new copy of the list to save computer memory
def eggs(someParam):
    someParam.append("Hello")

spam = [1, 2, 3]
eggs(spam)
print(spam)
# [1, 2, 3, 'Hello']


# To create a whole new copy/reference of a mutable value, use the 'copy' module --> copy.deepcopy()
import copy

spam = ["a", "b", "c", "d"]
cheese = copy.deepcopy(spam)    # this method creates a whole new reference, where any changes only affects 'cheese' and not 'spam'
cheese[1] = 42
print(cheese)
# ['a', 42, 'c', 'd']
print(spam)
# ['a', 'b', 'c', 'd']


# Strings are immutable
spam = 42
cheese = spam
spam = 100
print(spam)
# 100
print(cheese)
#42



# Strings can do a lot of the same things lists can do, but strings are immutable.
# Immutable values like strings and tuples cannot be modified "in place".
# Mutable values like lists can be modified in place.
# Variables don't contain lists, they contain references to lists.
# When passing a list argument to a function, you are actually passing a list reference.
# Changes made to a list in a function will affect the list outside the function.
# The \ line continuation character can be used to stretch Python instruction across multiple lines.