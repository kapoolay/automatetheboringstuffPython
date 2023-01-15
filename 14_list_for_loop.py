## Loop thru a range
for i in range(4):
    print(i)

# 1
# 2
# 3
# 0

## For loop thru a list using range(len(someList))
supplies = ["pens", "binders", "notebook", "paper"]

for i in range(len(supplies)):
    print(f"Index {str(i)} in supplies is: {supplies[i]}")

# Index 0 in supplies is: pens
# Index 1 in supplies is: binders
# Index 2 in supplies is: notebook
# Index 3 in supplies is: paper


## List all even values between 0 - 100
evenNumb = list(range(0, 100, 2))
print(evenNumb)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50,
# 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Multiple assignment trick
cat = ["fat", "orange", "loud"]
size = cat[0]
color = cat[1]
disposition = cat[2]

## shortcut
size, color, disposition = cat

# size > 'fat'
# color > 'orange'
# disposition > 'loud'

## Multiple assignment shortcut
size, color, disposition = 'skinny', 'black', 'quiet'
# size
# 'skinny'
# color
# 'black'
# disposition
# 'quiet'

a = 'AAA'
b = 'BBB'
a, b = b, a
# a
# 'BBB'
# b
# 'AAA'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Augmented assignment operators (+=, -+, *=, /=, %/)
spam = 42
spam = spam + 1
# spam
# 43
spam += 1
# spam
# 44

# A for loop technically iterates over the values in a list.
# The range() function returns a list-like value, which can be passed to the list() function if you need an actual list value.
# Variables can swap their values using multiple assignment: a, b = b, a
# Augmented assignment operators like += are used as shortcuts.