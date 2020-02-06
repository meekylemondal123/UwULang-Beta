# RULES:
# R, V, L, M -> W
# owo/uwu at each period
# ea -> ee
# se -> z


# method for finding letters
# method for replacing letters
from random import randint

def main():
    # This will contain the owo-ified string
    newString = ""

    
    #  Main method of the program
    phraseToReplace = input("Please enter the string you would like to owo-ify")

    for letter in range(len(phraseToReplace)):
        newString += locate(phraseToReplace[letter], letter, phraseToReplace)

    print (newString)
    
def replace(replaceLetter, index, fullString):
    # This method will replace the letter at the current index with the appropriate replacement char sequence
    return fullString[0:index] + replaceLetter + fullString[index:]    

    
def locate(letter, index, fullString):
    newLetter = ""
    
    # This method locates the index of all the letters 
    if letter.lower() == "r" or letter.lower() == "v" or letter.lower() == "l" or letter.lower() == "m":
        # Replacing the letter with so and so
        if letter.isUpper() == True:
            newLetter = "W"
        else:
            newLetter = "w"

    elif letter == ".":
        value = randint(1, 2)

        if (value == 1):
            newLetter = "uwu"
        else:
            newLetter = "owo"

            
    if index < len(fullString) - 1 and newLetter == "":
        # This is to avoid the possibility of detectinf and e and then checking for an a outside of the string index
        if letter == "e":
            if fullString[index + 1] == "a":
                newLetter = "ee"
        elif letter == "s":
            if fullString[index + 1] == "e":
                newLetter = "z"


    return replace(newLetter, index, fullString)

main()
