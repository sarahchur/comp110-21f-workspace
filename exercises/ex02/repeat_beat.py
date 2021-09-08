"""Repeating a beat in a loop."""

__author__ = "730228276"


# Begin your solution here...
beat = input("What beat do you want to repeat? ")
times = int(input("How many times do you want to repeat it? "))


i: int = 0

while i < times - 1:
    repeat_str: int = times
    print(str(beat) + str(times))
    i = i + 1

while i >= times - 1: 
    print(" No beat... ")
    i = i + 1








