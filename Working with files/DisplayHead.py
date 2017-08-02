# David Li
# August 4, 2015
# DisplayHead.py
# This program will display the first 10 lines of a file

import sys
NUM_LINES = 10

try:
    in_name = input("Enter the name of a Python file: ")
    #Open the file for reading
    inf = open(in_name, "r")

    #Read th first line from the line
    line = inf.readline()

    count = 0
    while count < NUM_LINES and line != "":
        #Remove the trailing newline character and count the line
        line = line.rstrip()
        count = count + 1

        #Display the line
        print(line)

        #Read the next line from the file
        line = inf.readline()

    #Close the file
    inf.close()
    
except IOError:
    print("An error occurred while accessing the file.")
