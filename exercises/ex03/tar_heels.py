"""An exercise in remainders and boolean logic."""

__author__ = "730228276"


integer: int = int(input("Enter an int: "))

if integer % 2 == 0:
    if integer % 7 == 0:
        print("TAR HEELS")

if integer % 2 == 0:
    if integer % 7 != 0:
        print("TAR")
else:
    if integer % 7 == 0:
        print("HEELS")
    else: 
        print("CAROLINA")
