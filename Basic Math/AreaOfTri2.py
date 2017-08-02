# David Li
# August 19, 2015
# AreaOfTri2.py

import math
print("This program will compute the area of a triangle using the sides ")

while True:
    s1 = float(input("Enter the length of the first side: "))
    s2 = float(input("Enter the length of the second side: "))
    s3 = float(input("Enter the length of the third side: "))
    s=(s1+s2+s3)/2

    area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    print("The area of the triangle is %.2f " % area)
