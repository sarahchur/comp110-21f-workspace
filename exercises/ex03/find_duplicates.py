"""Finding duplicate letters in a word."""

__author__ = "730228276"

word: str = input("Enter a word: ")
dup: bool = False

i: int = 0
j: int = 0

while i < len(word):
    character: str = word[i]
    j = j + 1
    while j < len(word):
        if character == word[j]:
            j = j + 1
            dup = True
        else:
            j = j + 1
    i = i + 1
        
print(dup)
   