# David Li
# August 25,2015
# BinaryToDecimal.py
# This program will convert a binary (base 2) number to decimal (base 10)

print("This program will convert from binary to decimal. ")
x=input("Enter the binary number: ")


dec = 0

for digit in x:
    dec = dec*2 + int(digit)
print ("The decimal of the given binary is ", dec, ".")
