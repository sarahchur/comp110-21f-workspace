"""Demonstration of dictionary capabilities."""


# Declaring a type of dictionary
schools: dict[str,int]

# Initialize to an empty dictionary
schools = dict()

# Set a key value pairing in the dictionary 
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation 
print(schools)

# Access a value by its key -- "lookup"
print(f" UNC has {schools['UNC']} students")

# Remove a key value pair from dictionary 
# By its key
schools.pop("Duke")

# Test for existence of a key 
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update/Reassign Key- Value pair
schools["UNC"] = 2000
schools["NCSU"] += 200

print(schools)

print(schools["UNCC"])
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")