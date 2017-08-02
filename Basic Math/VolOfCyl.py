# David Li
# August 18, 2015
# VolOfCyl.py
# This program will compute the volume of a cylinder

#Use the constant pi 
import math

print("This program will compute the volume of a cylinder. ")
while True:
    r= float(input("Enter the radius: "))
    h = float(input("Enter the height: "))

    volume= math.pi * r * r *h
    print("The volume of the cylinder is %.1f " % volume)
    print()
