"""
Fantasy Game Inventory
You are creating a fantasy video game. The data structure to model
the player’s inventory will be a dictionary where the keys are string
values describing the item in the inventory and the value is an integer
value detailing how many of that item the player has. For example, the
dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named displayInventory() that would take any possible
“inventory” and display it like the following:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
"""

def displayInventory(dictionary):
    print("Inventory:")
    item_total = 0
    for k, v in dictionary.items():
        print(f"{v} {k}")
        item_total += v
    print(f"Total number of items: {item_total}")


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inventory)
# 1 rope
# 6 torch
# 42 gold coin
# 1 dagger
# 12 arrow
# Total number of items: 62


groceries = {'apples': 3, 'grapes': 1, 'steak': 4, 'salad': 3}
displayInventory(groceries)
# Inventory:
# 3 apples
# 1 grapes
# 4 steak
# 3 salad
# Total number of items: 11



"""
List to Dictionary Function for Fantasy Game Inventory
Imagine that a vanquished dragon’s loot is represented as a list of strings like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems), 
where the inventory parameter is a dictionary representing the 
player’s inventory (like in the previous project) and the addedItems 
parameter is a list like dragonLoot. The addToInventory() function 
should return a dictionary that represents the updated inventory. 
Note that the addedItems list can contain multiples of the same item.
"""

def addToInventory(inventory, addItems):
    for item in addItems:
        inventory.setdefault(item, 0)

