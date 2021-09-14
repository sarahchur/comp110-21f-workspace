"""Finding duplicate letters in a word."""

__author__ = "730228276"

word: str = input("Enter a word: ")

i: int = 0

while i < len(word):
    character1: str = str(word[i])
    print(character1)
    j: int = i + 1
    character2: str = str(word[j])
    print(character2)
    i = i + 1
    j = j + 1
   