# David Li
# August 18, 2015
# This program will find the distance bewteen two points

import math
class point(object):
    def __init__(self,  x,y):
        #define x and y variables
        self.X= x
        self.Y = y
    def __str__(self):
        return ("Point(%s,%s)"%(self.X, self.Y))


print("This program will calculate the distance bewteen given points. ")
while True:
    try:
        p1= point(float(input("Enter the x1: ")),float(input("Enter y1: ")))
        p2 = point(float(input("Enter the x2: ")),float(input("Enter the y2: ")))
        break
    except ValueError:
        print("Mistake")
        continue
    except TypeError:
        print("Enter x,y coordinate: ")
        continue
    
d = math.sqrt((p2.X-p1.X)**2 +(p2.Y-p1.Y)**2)
print("The distance bewteen Point1" + str(p1) + "and Point2 "
      + str(p2) + " is %.2f" % d)

