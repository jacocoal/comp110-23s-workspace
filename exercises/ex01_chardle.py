"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730481986"
word: str = input("Enter a 5-character word: ")
if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if (len(character) != 1):
    print("Error: Character must be a single character.")
    exit()
chrcount: int = 0
print("Searching for " + character, "in " + word)
if (word[0] == character):
    print(str(character) + " found at index 0")
    chrcount = chrcount + 1
if (word[1] == character):
    print(str(character) + " found at index 1")
    chrcount = chrcount + 1
if (word[2] == character):
    print(str(character) + " found at index 2")
    chrcount = chrcount + 1
if (word[3] == character):
    print(str(character) + " found at index 3")
    chrcount = chrcount + 1
if (word[4] == character):
    print(str(character) + " found at index 4")
    chrcount = chrcount + 1
if (chrcount == 0):
    print("No instances of " + character + " found in " + word)
else:
    if (chrcount == 1):
        print(chrcount, "instance of " + character + " found in " + word)
    else:
        if (chrcount > 1):
            print(chrcount, "instances of " + character + " found in " + word)