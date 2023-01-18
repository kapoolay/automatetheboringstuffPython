# You can use data structures to model real world things in a way programs can understand
import pprint


# TicTacToe Data Structure

theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-M": " ", "mid-R": " ",
            "low-L": " ", "low-M": " ", "low-R": " "}

pprint.pprint(theBoard)
# {'low-L': ' ',
#  'low-M': ' ',
#  'low-R': ' ',
#  'mid-L': ' ',
#  'mid-M': ' ',
#  'mid-R': ' ',
#  'top-L': ' ',
#  'top-M': ' ',
#  'top-R': ' '}

# Moves
theBoard["mid-M"] = "X"
theBoard["top-L"] = "O"
theBoard["mid-L"] = "X"
theBoard["top-M"] = "O"
theBoard["low-R"] = "X"
theBoard["top-R"] = "O"

pprint.pprint(theBoard)
# {'low-L': ' ',
#  'low-M': ' ',
#  'low-R': 'X',
#  'mid-L': 'X',
#  'mid-M': 'X',
#  'mid-R': ' ',
#  'top-L': 'O',
#  'top-M': 'O',
#  'top-R': 'O'}

# O Wins!
# O|O|O
# X|X|
#  | |X


# type(value) function --> pass any value to this function and it will tell you the data type you are dealing with
print(type(42))
# <class 'int'>
print(type('hello'))
# <class 'str'>
print(type(theBoard))
# <class 'dict'>
print(type(theBoard['mid-R']))
# <class 'str'>
