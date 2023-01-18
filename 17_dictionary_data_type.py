myCat = {"size": "fat", "color": "gray", "disposition": "loud"}

print(myCat["size"])
# fat

print(f"My cat has {myCat['color']} fur.")
# My cat has gray fur.


## Dictionaries are unordered --> have no order
eggs = {"name": "Zophie", "species": "cat", "age": 8}
ham = {"species": "cat", "name": "Zophie", "age": 8}
print(eggs == ham)
# True

## Lists are ordered
set1 = [1, 2, 3]
set2 = [3, 2, 1]
print(set1 == set2)
# False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Dictionary Methods
# keys(), values(), items(), get(), setdefault()
# to return values into a list, you need to use list() method

eggs = {"name": "Zophie", "species": "cat", "age": 8}

print(list(eggs.keys()))    # return keys of the dictionary
# ['name', 'species', 'age']
print(eggs.keys())
# dict_keys(['name', 'species', 'age'])


print(list(eggs.values()))    # returns key values of the dictionary
# ['Zophie', 'cat', 8]
print(eggs.values())
# dict_values(['Zophie', 'cat', 8])


print(list(eggs.items()))    # returns key value pairs in 2 item tuples
# [('name', 'Zophie'), ('species', 'cat'), ('age', 8)]
print(eggs.items())
# dict_items([('name', 'Zophie'), ('species', 'cat'), ('age', 8)])


# get() takes 2 parameters. If first key parameter doesn't exist, it will return 2nd parameter
eggs = {"name": "Zophie", "species": "cat", "age": 8}
print(eggs.get("age", 0))
# 8
print(eggs.get("color", "--"))
# --

picnicItems = {"apples": 5, "cups": 8}
print("I am bringing " + str(picnicItems.get('napkins', 0)) + " napkins to the picnic.")
# I am bringing 0 napkins to the picnic.
print(f"I am bringing {picnicItems.get('napkins', 0)} napkins to the picnic.")
# I am bringing 0 napkins to the picnic.


# setdefault(a, b) Method    --> If key 'a' doesn't exist, assign the value 'b' to it
eggs = {"name": "Zophie", "species": "cat", "age": 8}

eggs.setdefault("color", "black")    # if the 'color' key doesn't exist, create it and assign 'black' to it
print(eggs)
# {'name': 'Zophie', 'species': 'cat', 'age': 8, 'color': 'black'}

eggs.setdefault("color", "orange")    # if the 'color' key doesn't exist, create it and assign 'orange' to it
print(eggs["color"])
# black    ## in this case, 'color': 'black' already exists, so it stays the same


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Looping thru Dictionary

eggs = {"name": "Zophie", "species": "cat", "age": 8}

# loop thru keys
for k in eggs.keys():
    print(k)
# name
# species
# age


# loop thru values
for v in eggs.values():
    print(v)
# Zophie
# cat
# 8

# loop thru key:values using items()
for k, v in eggs.items():
    print(f"{k}: {v}")
# name: Zophie
# species: cat
# age: 8

for i in eggs.items():
    print(i)
# ('name', 'Zophie')
# ('species', 'cat')
# ('age', 8)


'''
Dictionaries contain key-value pairs. Keys are like a list's indexes.
Dictionaries are mutable. Variables hold references to dictionary values, not the dictionary value itself.
Dictionaries are unordered. There is no "first" key-value pair in a dictionary.
The keys(), values(), and items() methods will return list-like values of a dictionary's keys, vaues, and both keys and values, respectively.
The get() method can return a default value if a key doesn't exist.
The setdefault() method can set a value if a key doesn't exist.
The pprint module's pprint() "pretty print" function can display a dictionary value cleanly. The pformat() function returns a string value of this output.'''
