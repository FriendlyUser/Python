# David Li
# August 27,2015
# randomPass.py
# This program will create a random password containing between 7 and 10 characters

from random import randint

SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126

# return a string containing a random password
def randomPassword():
    #Select a random length for the password
    randomLength = randint(SHORTEST, LONGEST)

    result = ""
    for i in range(randomLength):
        randomChar = chr(randint(MIN_ASCII, MAX_ASCII))
        result = result + randomChar

    return result

def main():
    print("Your random password is:", randomPassword())

# Call the main function only if the module is not imported
if __name__ == "__main__":
    main()
