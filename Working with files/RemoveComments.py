# David Li
# September 4, 2015
# RemoveComments.py
# This program will remove all the comments from a python file

#Read and open the input file
try:
    in_name = input("Enter the name of a Python file: ")
    inf = open(in_name, "r")
except:
    print("A problem was encountered while opening the input file.")
    print("Quitting...")
    quit()

#Read and open the output file, ensuring that it was opened
try:
    out_name = input("Enter the output file name: ")
    outf = open(out_name, "w")
except:
    print("A problem was encountered while opening the output file.")
    print("Qutting")
    quit()

try:
    #Read all of the lines from the input file, remove comments
    # and save the lines to a new file
    for line in inf:
        pos = line.find("#")

        # If there is a comment then form a slice
        # of the string that exclude it, overwriting line
        if pos > -1:
            line = line[0 : pos]
            line = line + "\n"

        #Write the line to the file
        outf.write(line)

    #Close the files
    inf.close()
    outf.close()

except:
    print("A problem was encountered while processing the file.")
    print("Quitting...")
    
