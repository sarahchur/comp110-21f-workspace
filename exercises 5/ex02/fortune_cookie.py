"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730228276"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

input("Your fortune cookie says...")

random: int = int(randint(1, 3))

Fortune_1: str = "A beautiful, smart, and loving person will be coming into your life. "
Fortune_2: str = "Your life will be happy and peaceful. "
Fortune_3: str = "Soon life will become more interesting. "

if random > 2:
    print(Fortune_1)
else: 
    if random < 2: 
        print(Fortune_2)
    else: 
        if random == 2: 
            print(Fortune_3)

print("Now, go spread positive vibes! ")