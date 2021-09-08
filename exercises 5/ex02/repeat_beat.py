"""Repeating a beat in a loop."""

__author__ = "730228276"

beat = input("What beat do you want to repeat? ")
times = int(input("How many times do you want to repeat it? "))

i: int = 0

repeat_str: str = ""

if times <= 0: 
    print("No beat... ")
else:
    while i < times:
        repeat_str = repeat_str + beat
        if i < times - 1:
            repeat_str = repeat_str + " "
        i = i + 1
    print(repeat_str)