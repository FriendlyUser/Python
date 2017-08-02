# David Li
# August 18, 2015
# AreaAndVolume.py
# This program will ask the user for a radius and compute the area and volume

import math
r= float(input("Enter the radius :"))
area= math.pi *r *r
volume =4/3*math.pi*r**3
print("The area is %.2f " %area)
print("The volume is %.2f " % volume)
