import pyperclip
## The upper(), lower(), isupper(), and islower() Methods

spam = "Hello world!"
print(spam.upper())
# HELLO WORLD!
print(spam.lower())
# hello world!
print(spam)
# Hello world!


## Small input program for case sensitivity
# print("How are you?")
# feeling = input()
#
# if feeling.lower() == "great":
#     print("I feel great too.")
# else:
#     print("I hope the rest of your day is good!")



## isupper(), islower()
'''The isupper() and islower() methods will return a Boolean True value if the string has
at least one letter and all the letters are uppercase or lowercase, respectively.
Otherwise, the method returns False.'''

spam = "Hello world!"
print(spam.islower())
# False

spam = "hello world!"
print(spam.islower())
# True

spam = "HELLO WORLD!"
print(spam.isupper())
# True

print("12345".islower())
# False
print("12345".isupper())
# False



'''Since the upper() and lower() string methods themselves return strings,
you can call string methods on those returned string values as well.
Expressions that do this will look like a chain of method calls.'''

print("Hello".upper().isupper())    # .upper() returns the string as all caps, resulting in .isupper() to be true
# True



## The isX() Methods
'''
isalpha() Returns True if the string consists only of letters and isn’t blank

isalnum() Returns True if the string consists only of letters and numbers and is not blank

isdecimal() Returns True if the string consists only of numeric characters and is not blank

isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank

istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
'''

print("hello".isalpha())
# True
print("hello123".isalpha())
# False
print("hello123".isalnum())
# True
print("123".isdecimal())
# True
print("        ".isspace())
# True
print("Hello world!".isspace())
# False
print("Hello world!"[5].isspace())
# True
print("This Is Title Case".istitle())
# True
print("hello world!".title().istitle())
# True



## startswith() and endswith() Methods
'''
The startswith() and endswith() Methods
The startswith() and endswith() methods return True if the string
value they are called on begins or ends (respectively) with
the string passed to the method; otherwise, they return False.
'''
print("Hello world!".startswith("Hello"))
# True
print("Hello world!".startswith("H"))
# True
print("Hello world!".lower().startswith("h"))
# True
print("Hello world!".endswith("world!"))
# True
print("Hello world!".endswith("world"))    # this is false bc it's missing '!' at the end
# False




## join() and split() Methods
'''
The join() method is useful when you have a list of strings that need to be joined
together into a single string value. The join() method is called on a string, gets
passed a list of strings, and returns a string. The returned string is the
 concatenation of each string in the passed-in list.
'''

print(",".join(["cats", "rats", "bats"]))
# cats,rats,bats
print(" - ".join(["cats", "rats", "bats"]))
# cats - rats - bats
print("".join(["cats", "rats", "bats"]))
# catsratsbats
print("\n\n".join(["cats", "rats", "bats"]))    # this returns the string ("cats\n\nrats\n\nbats")
# cats
#
# rats
#
# bats

'''
The split() method does the opposite: It’s called on a string value and returns a list of strings.
'''
print("My name is Simon".split())    # .split() naturally splits a string using whitespace
# ['My', 'name', 'is', 'Simon']
print("My name is Simon".split("m"))    # splitting the string wherever 'm' exists. Notice 'm' is taken away
# ['My na', 'e is Si', 'on']




# rjust(), ljust(), center()
'''
The rjust() and ljust() string methods return a padded version of the string
they are called on, with spaces inserted to justify the text.The first argument
to both methods is an integer length for the justified string.
'''

print("hello".rjust(10))
# '     hello'
print(len('     hello'))
# 10
print("hello".ljust(10))
# 'hello     '
print(len('hello     '))
# 10

'''
An optional second argument to rjust() and ljust() will specify a fill character other than a space character.
'''
print('hello'.rjust(20, "*"))
# ***************hello
print('hello'.ljust(20, "-"))
# hello---------------


'''
The center() string method works like ljust() and rjust() but centers the text rather than justifying it to the left or right. 
'''
print('hello'.center(20, "="))
# =======hello========




# Removing whitespace with strip(), rstrip(), lstrip(), replace()
'''Sometimes you may want to strip off whitespace characters (space, tab, and newline)
from the left side, right side, or both sides of a string. The strip() string method will
return a new string without any whitespace characters at the beginning or end. The lstrip()
and rstrip() methods will remove whitespace characters from the left and right ends, respectively.'''

spam = "      x      "
print(spam.strip())
# "x"
print(spam.lstrip())
# 'x      '
print(spam.rstrip())
# '      x'


'''Optionally, a string argument will specify which characters on the ends should be stripped.'''

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
# BaconSpamEggs


spam = 'Hello there!'
print(spam.replace('e', 'XYZ'))
# HXYZllo thXYZrXYZ!




'''
The pyperclip module has copy() and paste() functions that can
send text to and receive text from your computer’s clipboard.
Sending the output of your program to the clipboard will make it
easy to paste it into an email, word processor, or some other software.
'''

pyperclip.copy('Hello, world!')
print(pyperclip.paste())
# Hello, world!



'''
upper() and lower() return an uppercase or lowercase string.
isupper(), islower(), isalpha(), isalnum(), isdecimal(), isspace(), istitle() returns
   True or False if the string is that uppercase, lowercase, alphabetical letters, and so on.
startswith() and endswith() also return bools.
‘,'.join([‘cat', ‘dog']) returns a string that combines the strings in the given list.
‘Hello world'.split() returns a list of strings split from the string it's called on.
rjust() ,ljust(), center() returns a string padded with spaces.
strip(), rstrip(), lstrip() returns a string with whitespace stripped off the sides.
replace() will replace all occurrences of the first string argument with the second string argument.
Pyperclip has copy() and paste() functions for getting and putting strings on the clipboard.
'''