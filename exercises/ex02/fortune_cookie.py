"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730228276"

from random import randint


# Begin your solution here...

print("Your fortune cookie says...")

random: int = int(randint(1, 4))

Fortune_1: str = "A beautiful, smart, and loving person will be coming into your life. "
Fortune_2: str = "Your life will be happy and peaceful. "
Fortune_3: str = "Soon life will become more interesting. "
Fortune_4: str = "You will become very wealthy. "

if random == 1:
    print(Fortune_1)
else: 
    if random == 2: 
        print(Fortune_2)
    else: 
        if random == 3: 
            print(Fortune_3)
        else: 
            print(Fortune_4)


print("Now, go spread positive vibes!")