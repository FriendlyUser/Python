# David Li
# August 31, 2015
# Tokenize.py
# This program will tokenize a string containing a mathematical expression

def tokenList(s):
    #Remove all of the spaces from s
    s = s.replace(" ", "")

    # Loop through all of the characters in the string
    # identifiying the tokens and adding them to the list
    tokens = []
    i = 0
    while i < len(s):
        # Handle the tokens that are always a single character *,/,^,( and )
        if s[i] == "*" or s[i] == "/" or s[i] == "^" or \
           s[i] == "(" or s[i] == ")":
            tokens.append(s[i])
            i = i + 1
            
        #Handle + and -
        elif s[i] == "+" or s[i] == "-":
            # If there is a previous character and it is a number of close bracket
            # then the + or - is a token on its own
            if i > 0 and (s[i-1] >= "0" and s[i-1] <= "9" or s[i-1] == ")"):
                tokens.append(s[i])
                i = i + 1
            else:
                # The + or - is part of a number
                num = s[i]
                i = i + 1

                # Keep on adding characters to the token as long as they are digits
                while i < len(s) and s[i] >= "0" and s[i] <= "9":
                    num = num + s[i]
                    i = i + 1
                tokens.append(num)

        #Handle a number without a leading + or -
        elif s[i] >= "0" and s[i] <= "9":
            num = ""
            # Keep on adding characters to the token as long as they are digits
            while i < len(s) and s[i] >= "0" and s[i] <= "9":
                 num = num + s[i]
                 i = i + 1
            tokens.append(num)
            
        # Any other character means the expression is not valid
        # Return an empty list to indicate that an error occured
        else:
            return []
    return tokens

def main():
    exp = input("Enter a matematical expression: ")
    tokens = tokenList(exp)
    print("The tokens are: ", tokens)

if __name__ == "__main__":
    main()
    
