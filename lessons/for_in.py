"""An example of for in syntax."""


names: list[str] = ["Sarah", "Haynes", "Anna", "Olivia"]

print("while output:")
i: int = 0
while i < len(names): 
    name: str = names[i] 
    print(name)
    i += 1

# for in loop is the same as above
print("for..in output")
for name in names:
    print(name)