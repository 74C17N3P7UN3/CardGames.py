# Python Packages
from os import name, system


def clear():
    print("\033[2J", end="")


# If regex is not working correctly
# for you, uncomment the code below
"""
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")
"""
