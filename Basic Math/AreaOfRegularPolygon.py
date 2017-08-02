#David Li
# August 18, 2015

#Compute the area of a regular polygon

from math import tan, pi


while True:
    #Read input from the user
    s = float(input("Enter the length of each side of the polygon; "))
    n= int(input("Enter the number of sides: "))

    #Compute the area of the polygon
    area= (n*s**2)/(4*tan(pi/n))

    #Diplay the result
    print("The area of the polygon is ",area)
