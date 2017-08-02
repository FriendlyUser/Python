# David Li
# August 17,2015

from math import log10

a= int(input("Enter the value of a: "))
b= int(input("Enter the value of b: "))

print(a, "+", b, "is", a+b)
print(a, "-", b, "is", a-b)
print(a, "*", b, "is", a*b)
print(a, "/", b, "is", a/b)
print(a, "%", b, "is", a%b)

#Compute the logarithm and the power
print("The base 10 logarithm of", a, "is", log10(a))
print(a, "^", b, "is", a**b)
