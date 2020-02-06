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
    


    
def locate(letter, index, fullString):
    newLetter = ""
    changes = False
    
    # This method locates the index of all the letters 
    if letter.lower() == "r" or letter.lower() == "l" or letter.lower() == "m":
        # Replacing the letter with so and so
        if letter.isupper() == True:
            newLetter = "W"
            changes = True
        else:
            newLetter = "w"
            changes = True

    elif letter == ".":
        value = randint(1, 2)

        if (value == 1):
            newLetter = " uwu. "
            changes = True
        else:
            newLetter = " owo. "
            changes = True
            
    elif letter == "v":
            if index == 0:
                newLetter = "w"
            else:
                if fullString[index - 1] == " ":
                    newLetter = "w"

                
    if index < len(fullString) - 1 and newLetter == "":
        # This is to avoid the possibility of detectinf and e and then checking for an a outside of the string index
        if letter == "e":
            if fullString[index + 1] == "a":
                newLetter = "ee"
                changes = True
        elif letter == "s":
            if fullString[index + 1] == "e":
                newLetter = "z"
                changes = True


    if changes:
        return newLetter
    else:
        return letter

main()
