# David Li
# August 25,2015
# PrimeFactors.py
# This program will prompt the user for an integer and find the prime factors

while True:
    n = int(input("Enter an integer: "))
    print("The prime factors of", n, " are: ")
    factor = 2
    while factor <= n:
        if n % factor == 0:
            print(factor,end=" ")
            n = n/factor
        else:
            factor += 1
    print()
    print("Complete!\n")

