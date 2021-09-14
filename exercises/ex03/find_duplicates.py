"""Finding duplicate letters in a word."""

__author__ = "730228276"

word: str = input("Enter a word: ")
dup: str = "False"

i: int = 0
while i < len(word):
    character: str = word[i]
    j: int = i + 1
    while j < len(word):
        if character == word[j]:
            dup: str = "True"

        j = j + 1
    i = i + 1
        
print(dup)
   