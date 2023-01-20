import pprint    # includes the '.pprint' method that prints lists/dictionaries in a nice format

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}    ## 'character': 'count of the character'

for character in message.upper():
    count.setdefault(character, 0)    ## if the character key doesn't exist, create the key 'character' and start the count at zero
    count[character] += 1

print(count)
# {'I': 7, 'T': 6, ' ': 13, 'W': 2, 'A': 5, 'S': 3, 'B': 1, 'R': 5, 'G': 2, 'H': 3, 'C': 3, 'O': 2, 'L': 3, 'D': 3, 'Y': 1, 'N': 4, 'P': 1, ',': 1, 'E': 5, 'K': 2, '.': 1}

pprint.pprint(count)    ## prints results in a nice format
# {' ': 13,
#  ',': 1,
#  '.': 1,
#  'A': 5,
#  'B': 1,
# ...
#  'Y': 1}

# pprint.pformat() assigns the text to a variable
example = pprint.pformat(count)
print(example)
# {' ': 13,
#  ',': 1,
#  '.': 1,
#  'A': 5,
#  'B': 1,
# ...
#  'Y': 1}

'''
Dictionaries contain key-value pairs. Keys are like a list's indexes.
Dictionaries are mutable. Variables hold references to dictionary values, not the dictionary value itself.
Dictionaries are unordered. There is no "first" key-value pair in a dictionary.
The keys(), values(), and items() methods will return list-like values of a dictionary's keys, vaues, and both keys and values, respectively.
The get() method can return a default value if a key doesn't exist.
The setdefault() method can set a value if a key doesn't exist.
The pprint module's pprint() "pretty print" function can display a dictionary value cleanly. The pformat() function returns a string value of this output.
'''