## Escape Characters
# \'  Single quote
# \"  Double quote
# \t  Tab
# \n  Newline (line break)
# \\  Backslash

import pprint

print('Hello there!\nHow are you?\nI\'m fine.')
# Hello there!
# How are you?
# I'm fine.


## Raw Strings --> r'string values'
## Raw strings will literally print any backslashes in the string and ignore escape characters
print(r'That is Carol\'s cat.')    # having '\' in the text will also include it in the output
# That is Carol\'s cat.


## Multi-line strings using """ or '''
print("""Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, 
and extortion.
Sincerely,
Bob.""")
# Dear Alice,
# Eve's cat has been arrested for catnapping, cat burglary,
# and extortion.
# Sincerely,
# Bob.

## Perfectly valid Python code
def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')

spam()
# Hello!


spam = ("""Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, 
and extortion.
Sincerely,
Bob.""")

print(spam)
# Dear Alice,
# Eve's cat has been arrested for catnapping, cat burglary,
# and extortion.
# Sincerely,
# Bob.



## Similarities between strings and lists
spam = "Hello world!"
print(spam[0])
# H
print(spam[1:5])
# ello
print(spam[-1])
# !
print("Hello" in spam)  # this is case sensitive
# True
print("HELLO" in spam)
# False
print("x" in spam)
# False


'''
Strings are enclosed by a pair of single quotes or double quotes (as long as the same kind are used).
Escape characters let you put quotes and other characters that are hard to type inside strings.
Raw strings (which have the r prefix before the first quote) will literally print any backslashes in the string and ignore escape characters.
Multiline strings begin and end with three quotes, and can span multiple lines.
Indexes, slices, and the "in" and "not in" operators all work with strings.
'''