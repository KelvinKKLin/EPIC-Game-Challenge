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

class Button():
    def __init__(self, screen, x1, y1, x2, y2, state):
        self.screen = screen
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.state = state
        
    def getX(self):
        return self.x1, self.x2
    
    def getY(self):
        return self.y1, self.y2
    
    def draw(self):
        pygame.draw.rect(self.screen, GREEN, [self.x1, self.y1, self.x2-self.x1, self.y2-self.y1], 0)
    
    def getState(self):
        return self.state        
        
    def isPressed(self):
        pos = pygame.mouse.get_pos()
        return pos[0] > self.x1 and pos[0] < self.x2 and pos[1] > self.y1 and pos[1] < self.y2      
         
    
#Draws a dialog box for the game
def drawDialogBox(screen, colour, percentage):
    lift = 10 #Amount of spacing the rectangle has
    rectangularAttributes = [0 + lift, screen.get_height()*percentage-lift, screen.get_width() - (lift*2) , screen.get_height()-(screen.get_height()*percentage)] #Sets the attribute for the rectangle
    pygame.draw.rect(screen, colour, rectangularAttributes, 0)

#Displays a background
def setBackground(screen, location):
    background = pygame.image.load(location).convert()
    screen.blit(background, [0,0])

#Displays a character onto the screen
def setCharacter(screen, location, character_x, character_y):
    character = pygame.image.load(location).convert()
    character.set_colorkey(BLACK)
    screen.blit(character, [character_x, character_y])
    
#Displays the score onto the screen
def printScore(screen, score):
    font = pygame.font.SysFont("Calibri", 25, True, False)
    output = "Score: " + str(score)
    text = font.render(output, True, WHITE)
    screen.blit(text, [screen.get_width() - 125, 10])
    
def drawTimer(screen, time, endingTime):
    if time < 5:
        pygame.draw.rect(screen,GREEN,[20,20,(100)-((time/float(endingTime))*100),100],0)
        return "Happy"
    elif time < 8 and time >= 5:
        pygame.draw.rect(screen,YELLOW,[20,20,(100)-((time/float(endingTime))*100),100],0)
        return "Nutral"
    else:
        pygame.draw.rect(screen,RED,[20,20, (100)-((time/float(endingTime))*100),100],0)
        return "Sad"
        
#Draws text onto the screen
def displayDialog(screen, characterName, text, isASelection, currentBeltColour, lightColourList):
    
    #Different fonts for different purposes
    characterFont = pygame.font.SysFont("Calibri", 25, True, False)
    textFont = pygame.font.SysFont("Calibri", 23, False, False)
    
    #Different amounts of spacing for different amounts of text
    nameHeightDisplacement = 255
    dialogHeightDisplacement = 220
    widthDisplacement = 1025    
    
    #Creates the character name and displays it onto the screen
    if currentBeltColour in lightColourList:
        characterLabel = characterFont.render(characterName, True, BLACK)
    else:
        characterLabel = characterFont.render(characterName, True, WHITE)
    screen.blit(characterLabel, [screen.get_width() - widthDisplacement, screen.get_height() - nameHeightDisplacement])
    
    #Process text depending on whether it is a selection or dialog
    if isASelection:
        text = wordProcessing.processSelection(text)
    else:
        text = wordProcessing.processDialog(text)
    
    #Renders dialog, and displays it onto the screen
    for line in text:
        if currentBeltColour in lightColourList:
            dialogLabel = textFont.render(str(line), True, BLACK)
        else:
            dialogLabel = textFont.render(str(line), True, WHITE)        
        screen.blit(dialogLabel, [screen.get_width() - widthDisplacement, screen.get_height() - dialogHeightDisplacement])
        dialogHeightDisplacement -= 20
        
#Draws a selection box around the selected item
def drawSelection(screen, selection):
    
    #Constants - TODO: Enumerate all the constants into one file.
    nameHeightDisplacement = 255
    dialogHeightDisplacement = 215
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
    elif selection == 3:
            rectangularAttributes = [0 + lift, screen.get_height() - dialogHeightDisplacement + 60, screen.get_width() - (lift*2), 20] #Sets the attribute for the rectangle
            pygame.draw.rect(screen, colour, rectangularAttributes, 1)      