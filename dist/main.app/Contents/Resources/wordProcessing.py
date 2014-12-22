#wordProcessing.py
import random

'''
This processes text used for the game.
'''

#This splits a long dialog into lists of 91 characters to be displayed on the screen
#def processDialog(text):
    #dialog = []
    #numberOfCharactersStored = 0
    #for char in text:
        #dialog.append(text[numberOfCharactersStored:numberOfCharactersStored+91])
        #numberOfCharactersStored += 91
    #return dialog
    
#This splits a string of dialog into lists of 91 characters (or less) to be displayed on the screen
#Input - A string
#Output - A list
def processDialog(text):
    dialog = []
    listOfText = text.split()
    line = ""
    for i in range(len(listOfText)):
        if len(line) < (90 - (len(listOfText[i]) + 1)):
            line = line + listOfText[i] + " "
        else:
            dialog.append(line)
            try:
                line = listOfText[i] + " "
            except:
                line = ""
            
    if not dialog or line:
        dialog.append(line)
    return dialog



##This retrieves data from a file containing the game's dialog and splits it according to character, and reference
#def getDialog(location):
    #characterList = [] #List of strings containing character names
    #dialogList = [] #List of strings containing dialog and/or selections
    #referenceList = [] #List of strings containing reference points
    #linearList = []    # List of booleans denoting whether the dialog is linear
    #scoreList = [] #List of scores for each quiz
    #backgroundList = [] #List of backgrounds
    #imageList = [] #List of character sprites
    #dialog = open(location, "r")
    #for entry in dialog.readlines():
        #data = entry.split("%%")
        #characterList.append(data[0])
        #dialogList.append(data[1])
        #referenceList.append(data[2])
        #linearList.append(data[3].split())
        #scoreList.append(data[4])
        ##backgroundList.append(data[5])
        ##imageList.append(data[6])
        
    #dialog.close()
    #return characterList, dialogList, referenceList, linearList, scoreList
    
#This retrieves data from a file containing the game's dialog and splits it according to character, and reference, etc
def getLessonScript(location):
    backgroundPictureList = []
    foregroundPictureList = []
    speakerProfilePictureList = []
    speakerList = []
    dialogList = []
    dialog = open(location, "r")
    for entry in dialog.readlines():
        data = entry.split("%%")
        #print data
        backgroundPictureList.append(data[0])
        foregroundPictureList.append(data[1])
        speakerProfilePictureList.append(data[2])
        speakerList.append(data[3])
        dialogList.append(data[4])
    dialog.close()
    return backgroundPictureList, foregroundPictureList, speakerProfilePictureList, speakerList, dialogList

#This retrieves data from a file containing the game's quiz questions and splits it according to character, and reference, etc
def getTriviaScript(location):
    backgroundPictureList = []
    speakerProfilePictureList = []
    questionList = []
    selectionList = []
    answerList = []
    scoreList = []
    timeList = []
    dialog = open(location, "r")
    for entry in dialog.readlines():
        data = entry.split("%%")
        questionList.append(data[0])
        selectionList.append(data[1])
        answerList.append(data[2])
        scoreList.append(data[3])
        timeList.append(data[4])
    dialog.close()
    return questionList, selectionList, answerList, scoreList, timeList

#This splits a selection for the quiz into a list of choices for the user to choose
def processSelection(dialogList):
    selection = dialogList.split("$$")
    for choice in range(len(selection)):
        selection[choice] += (len(selection)) * " " 
    return selection

#This returns a random list denoting the order of questions.
def getQuestionSequence(lenList):
    return random.sample(xrange(lenList), lenList)

