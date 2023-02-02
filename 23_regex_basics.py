

# Regex is a language to find text patterns

# Phone number 415-555-0155
# Not a phone number 4,155,550,155


def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True


# num = '415-555-0155'
# notNum = '415-asdf'
#
# print(isPhoneNumber(num))
# print(isPhoneNumber(notNum))


message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 on my office line.'
foundNumber = False

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ REGEX METHOD
# First import regex module
import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 on my office line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)     # .search() returns a match object
print(mo.group())     # match objects have a method called .group() that gives you the actual text

# .findall() returns all the occurrences of the regex pattern
print(phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-9999 on my office line.'))


'''
Regular expressions are mini-language for specifying text patterns. Writing code to do pattern matching without regular expressions is a huge pain.
Regex strings often use backslashes (like \d), so they are often written using raw strings: r'\d'
\d is the regex for a numeric digit character.
Import the re module first.
Call the re.compile() function to create a regex object.
Call the regex object's search() method to create a match object.
Call the match object's group() method to get the matched string.
'''