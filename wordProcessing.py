#wordProcessing.py

'''
This processes text used for the game.
'''

#This splits a long dialog into lists of 91 characters to be displayed on the screen
def processDialog(text):
    dialog = []
    numberOfCharactersStored = 0
    for char in text:
        dialog.append(text[numberOfCharactersStored:numberOfCharactersStored+91])
        numberOfCharactersStored += 91
    return dialog

#This retrieves data from a file containing the game's dialog and splits it according to character, and reference
def getDialog(location):
    characterList = [] #List of strings containing character names
    dialogList = [] #List of strings containing dialog and/or selections
    referenceList = [] #List of strings containing reference points
    linearList = []    # List of booleans denoting whether the dialog is linear
    dialog = open(location, "r")
    for entry in dialog.readlines():
        data = entry.split("%%")
        characterList.append(data[0])
        dialogList.append(data[1])
        referenceList.append(data[2])
        linearList.append(data[3].split())
    dialog.close()
    return characterList, dialogList, referenceList, linearList
    
#This splits a selection into a list of choices
def processSelection(dialogList):
    selection = dialogList.split("$$")
    for choice in range(len(selection)):
        selection[choice] += (len(selection)) * " " 
    return selection
