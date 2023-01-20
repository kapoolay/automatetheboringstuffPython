'''
Write a function that takes a list value as an argument
and returns a string with all the items separated by a
comma and a space, with "and" inserted before the last item.
For example, passing the previous spam list to the function
would return 'apples, bananas, tofu, and cats'. But your function
should be able to work with any list value passed to it. Be sure
to test the case where an empty list [] is passed to your function.
'''

def commaCode(list):
    list.insert(-1, "and")
    print(list)

spam = ['apples', 'bananas', 'tofu', 'cats']
commaCode(spam)
# ['apples', 'bananas', 'tofu', 'and', 'cats']


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
commaCode(colors)
# ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'and', 'violet']
