# David Li
# August 18, 2015
# IdealGasLaw.py
# This program will take values of pressure in atmospheres, volume in liters
# n is moles and R is 0.08205 L atm/(mol-K), T is the temperature in degrees Kelvin

IDEAL_GAS_CONST = 0.08205

print("This program will use the ideal gas law to determine \
      the amount of moles: ")

while True:
    pressure = float(input("Enter the pressure in atmospheres: "))
    volume = float(input("Enter the volume in liters: "))
    #get temperature in degrees and convert to kelvin
    temp = float(input("Enter the temperature in degrees: ")) + 273.15

    n= pressure * volume /(IDEAL_GAS_CONST * temp)
    print("The number of moles is %.2f " % n)
    print()
