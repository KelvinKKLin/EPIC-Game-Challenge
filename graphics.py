#graphics.py

'''
This allows us to easily implement common GUI features of the game.
'''

import pygame
import wordProcessing

#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 251, 0)

#Draws a dialog box for the game
def drawDialogBox(screen, colour, percentage):
    lift = 10 #Amount of spacing the rectangle has
    rectangularAttributes = [0 + lift, screen.get_height()*percentage-lift, screen.get_width() - (lift*2) , screen.get_height()-(screen.get_height()*percentage)] #Sets the attribute for the rectangle
    pygame.draw.rect(screen, colour, rectangularAttributes, 0)

#Displays a background
def setBackground(screen, location):
    background = pygame.image.load(location).convert()
    screen.blit(background, [0,0])

def setCharacter(screen, location):
    character = pygame.image.load(location).convert()
    character.set_colorkey(WHITE)
    screen.blit(character, [int(((screen.get_width())/2)), 0])

#Draws text onto the screen
def displayText(screen, characterName, text, isASelection):
    
    #Different fonts for different purposes
    characterFont = pygame.font.SysFont("Calibri", 25, True, False)
    textFont = pygame.font.SysFont("Calibri", 23, False, False)
    
    #Different amounts of spacing for different amounts of text
    nameHeightDisplacement = 255
    dialogHeightDisplacement = 220
    widthDisplacement = 1025    
    
    #Creates the character name and displays it onto the screen
    characterLabel = characterFont.render(characterName, True, WHITE)
    screen.blit(characterLabel, [screen.get_width() - widthDisplacement, screen.get_height() - nameHeightDisplacement])
    
    #Process text depending on whether it is a selection or dialog
    if isASelection:
        text = wordProcessing.processSelection(text)
    else:
        text = wordProcessing.processDialog(text)
    
    #Renders dialog, and displays it onto the screen
    for line in text:
        dialogLabel = textFont.render(str(line), True, WHITE)    
        screen.blit(dialogLabel, [screen.get_width() - widthDisplacement, screen.get_height() - dialogHeightDisplacement])
        dialogHeightDisplacement -= 20
        
#Draws a selection box around the selected item
def drawSelection(screen, selection):
    
    #Constants - TODO: Enumerate all the constants into one file.
    nameHeightDisplacement = 255
    dialogHeightDisplacement = 220
    widthDisplacement = 1025       
    lift = 10
    percentage = 0.75
    colour = YELLOW
    
    #Draws the selection box
    if selection == 0:
        rectangularAttributes = [0 + lift, screen.get_height() - dialogHeightDisplacement, screen.get_width() - (lift*2), 20] #Sets the attribute for the rectangle
        pygame.draw.rect(screen, colour, rectangularAttributes, 1)
    elif selection == 1:
        rectangularAttributes = [0 + lift, screen.get_height() - dialogHeightDisplacement + 20, screen.get_width() - (lift*2), 20] #Sets the attribute for the rectangle
        pygame.draw.rect(screen, colour, rectangularAttributes, 1)        
    elif selection == 2:
        rectangularAttributes = [0 + lift, screen.get_height() - dialogHeightDisplacement + 40, screen.get_width() - (lift*2), 20] #Sets the attribute for the rectangle
        pygame.draw.rect(screen, colour, rectangularAttributes, 1)            