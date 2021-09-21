"""Drawing forests in a loop."""

__author__ = "730228276"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(str(input("Depth: ")))

i: int = 0
string: str = ""

while i <= depth:
    if i < depth:
        string = string + TREE
    else: 
        if i == depth:
            string = string + TREE
    i = i + 1



