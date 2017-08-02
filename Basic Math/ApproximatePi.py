# David Li
# August 23,2015
# ApproximatePi.py
# This program will approximate the value of pi using a infinite series
# 4*(1 - 1/3 + 1/5 - 1/7 + 1/9 - ....)

import sys

def piApprox(num):
    pi=4.0
    k=1.0
    est=1.0
    while 1<num:
        k+=2
        est=est-(1/k)+1/(k+2)
        num=num-1
        k+=2
    return pi*est

while True:
    try:
        num = int(input("Enter the number of series to approximate pi to: "))
        approx = piApprox(num)
        print(approx)
    except:
        print("This program will now close!")
        sys.exit(0)

