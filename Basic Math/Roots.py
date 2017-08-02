# David Li
# August 21,2015
# Roots.py
# This program will compute the number of roots of the quadratic and the real valued roots
import math

print("The Quadratic Equation is ax*x+bx+c")
while True:
    try:
        a=float(input("Enter a: "))
        b=float(input("Enter b: "))
        c=float(input("Enter c: "))
        det=b**2-4*a*c

        print("The equation is %.2f" %a + "x^2 +" +" %.2f" % b + "x +" " %.2f" % c)

        #no roots
        if(det < 0):
            print("No Roots: ")
        #one root
        elif(det == 0):
            root1= -b/(2*a)
            print("One Root: %.2f" % root1)
        #two roots
        else:
            root1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
            root2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
            print("Two Roots: %.2f" % root1 + ", %.2f " % root2)
            
    except ValueError:
        print("Try again. ")
        continue
    except TypeError:
        print("Try again. ")
        continue
    except:
        print("Unexpected error: ")
        continue
    print()
    
