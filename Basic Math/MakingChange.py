# David Li
# August 17,2015
# This program will compute the minimum collection of coins needed to respresent a number of cents

CENTS_PER_TONNIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME =    10
CENTS_PER_NICKEL =   5

#Read the number of cents from the user
while True:
    cents= int(input("Enter the number of cents: "))
    #Determine the number of tonnies by performing an integer division by 200.
    #repeat for loonies,quarters ... pennies

    print(" ", cents // CENTS_PER_TONNIE, "toonies")

    #Compute remainder after dividing my 200
    cents = cents % CENTS_PER_TONNIE

    print(" ", cents // CENTS_PER_LOONIE, "loonies")
    cents = cents % CENTS_PER_LOONIE

    print(" ", cents // CENTS_PER_QUARTER, "quarters")
    cents = cents % CENTS_PER_QUARTER

    print(" ", cents // CENTS_PER_DIME, "dimes")
    cents = cents % CENTS_PER_DIME

    print(" ", cents // CENTS_PER_NICKEL, "nickels")
    cents = cents % CENTS_PER_NICKEL

    #Display the number of pennies
    print(" ", cents, "pennies")
