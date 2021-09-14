"""Finding duplicate letters in a word."""

__author__ = "730228276"

word: str = input("Enter a word: ")
dup: bool = False

i: int = 0
j: int = 0

while i < len(word):
    character = word[i]
    j = i + 1
    while j < len(word):
        if character == word[j]:
            j += 1
            dup = True
        else:
            j += 1
    i += 1

dup_str: str = str(dup)
print("Found duplicate: " + dup_str)
   