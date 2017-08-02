# David Li
# September 2, 2015
# UniqueCharacters
# This program will returned the number of unique characters

s = input("Enter a string: ")

character = {}
for ch in s:
    character[ch] = True

#Display the result
print("That string contained", len(characters), "unique character(s).")
