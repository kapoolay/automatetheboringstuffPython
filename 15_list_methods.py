## Similar to a function, but calls on or attached to a certain value

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ someList.index() Method  --> returns the value's index in the list

spam = ['hello', 'hi', 'howdy', 'heyas']

print(spam.index('hello'))
# 0

print(spam.index('heyas'))
# 3

## You need to include the list name with the method, or it errors out --> someList.index()
spam = ['hello', 'world', 'hi']
print(index('hello'))
# Traceback (most recent call last):
#   File "<pyshell#27>", line 1, in <module>
#     index('hello')
# NameError: name 'index' is not defined

## The value you are searching for needs to exist in the list
spam = ['cat', 'dog', 'rat']
print(spam.index('I DO NOT EXIST IN THE SPAM LIST'))
# Traceback (most recent call last):
#   File "/Users/Kev/learning/Udemy/automateTheBoringStuffWithPython/15_list_methods.py", line 24, in <module>
#     print(spam.index('I DO NOT EXIST IN THE SPAM LIST'))
# ValueError: 'I DO NOT EXIST IN THE SPAM LIST' is not in list

## If you search for a duplicated value in the list, it will return the first value's index in the list
cats = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']

print(cats.index('Pooka'))
# 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ someList.append() Method --> adds the value to the end of the list
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)
# ['cat', 'dog', 'bat', 'moose']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ someList.insert(value's index, value) --> adds the value to a certain place in the list using an index
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)
# ['cat', 'chicken', 'dog', 'bat']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ someList.remove() --> removes a value from the list. It only removes the first instance of the value.
spam = ['cat', 'bat', 'rat', 'elephant', 'bat', 'lion', 'bat']
spam.remove('bat')
print(spam)
# ['cat', 'rat', 'elephant', 'bat', 'lion', 'bat']

## Attempting to remove() a value that doesn't exist produces an error
spam = ['cat', 'dog']
print(spam.remove('bat'))
# Traceback (most recent call last):
#   File "<pyshell#36>", line 1, in <module>
#     spam.remove('bat')
# ValueError: list.remove(x): x not in list


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ del function removes an index value from the list using the index, not the value
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[0]
print(spam)
# ['bat', 'rat', 'elephant']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ someList.sort() --> sorts a list in numerical/alphabetical order
spam = [1, 10, 2, 3.14, -7]
spam.sort()
print(spam)
# [-7, 1, 2, 3.14, 10]

spam = ['zebra', 'ant', 'bat', 'elephant']
spam.sort()
print(spam)
# ['ant', 'bat', 'elephant', 'zebra']

## You can reverse the sort order using .sort(reverse=True)
spam = ['ant', 'zebra', 'bat', 'cat', 'elephant']
spam.sort(reverse=True)    # first it sorts in alphabetical order, then reverses the order
print(spam)
# ['zebra', 'elephant', 'cat', 'bat', 'ant']

## You cannot sort a list that has both string and integer data types
spam = [1, 2, 3, 'hello', 'hi', 5]
spam.sort()
# Traceback (most recent call last):
#   File "<pyshell#44>", line 1, in <module>
#     spam.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'

## .sort() uses "ASCII-betical" order --> sorted alphabetically, but upper case characters are before lower case
spam = ['Alice', 'Carol', 'Bob', 'ants', 'badgers', 'cats', 'Zoe']
spam.sort()
print(spam)
#['Alice', 'Bob', 'Carol', 'Zoe', 'ants', 'badgers', 'cats']

## Sort in true alphabetical order using .sort(key=str.lower)
spam = ['Alice', 'Carol', 'Bob', 'ants', 'badgers', 'cats']
spam.sort(key=str.lower)
print(spam)
# ['Alice', 'ants', 'badgers', 'Bob', 'Carol', 'cats']



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ERRORS

## append() | insert() only work for list data types. String data types don't have this kind of method
eggs = 'hello'
print(eggs.append('world'))
# Traceback (most recent call last):
#   File "<pyshell#29>", line 1, in <module>
#     eggs.append('world')
# AttributeError: 'str' object has no attribute 'append'


## Do not assign a method to a variable, because methods return 'None'
spam = ['cat', 'dog', 'bat']
## GOOOOOOD
spam.append('bird')
print(spam)
# ['cat', 'dog', 'bat', 'bird']

## BAAAAAAAD
spam = spam.append('tiger')
print(spam)
# None


# RECAP
# Methods are functions that are "called on" values.
# The index() list method returns the index of an item in the list.
# The append() list method adds a value to the end of a list.
# The insert() list method adds a value anywhere inside a list.
# The remove() list method removes an item, specified by the value, from a list.
# The sort() list method sorts the items in a list.
# The sort() method's reverse=True keyword argument can make the sort() method sort in reverse order.
# These list methods operate on the list "in place", rather than returning a new list value.