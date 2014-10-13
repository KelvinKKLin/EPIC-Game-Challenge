#main.py

''' 
This is the main loop for the program.
TODO: Implement game
'''

import pygame
import graphics
import wordProcessing

#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 251, 0)

lineNumber = 0
selection = 0

characterList, dialogList, referenceList, linearList = wordProcessing.getDialog("test.txt")

#The main loop
def main():
    screen = initializeGame()
    gameLoop(screen)
    pygame.quit()
    print "Done"
    
#Initializes pyGame, and returns a screen for the game
def initializeGame():
    pygame.init()
    size = (1050, 750)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Test Game")
    return screen
    
#The game loop runs while the game is not over
def gameLoop(screen):
    done = False;
    clock = pygame.time.Clock()
    while not done:
        done = processEvents()
        gameLogic()
        updateScreen(screen)
        clock.tick(60)

#Processes user inputs
def processEvents():
    global lineNumber
    global selection
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            return done
        #Processes Keyboard input
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and linearList[lineNumber] == ['False']:
                lineNumber += 1
            elif event.key == pygame.K_UP:
                selection = max(0, selection-1)
            elif event.key == pygame.K_DOWN:
                selection = min(2, selection +1)
            elif event.key == pygame.K_RETURN:
                lineNumber += 1
    return done

#Determines the logic for the game
def gameLogic():
    return None

#Updates the screen
def updateScreen(screen):
    global lineNumber
    screen.fill(WHITE)
    graphics.setBackground(screen, "background1.jpg")
    graphics.drawDialogBox(screen, BLACK, 0.65)

    #Display dialog while there is still script
    if lineNumber < len(characterList):
        graphics.displayText(screen, characterList[lineNumber], dialogList[lineNumber], linearList[lineNumber] == ['True'])
        
        #Draws selection boxes if the dialog is a selection
        if linearList[lineNumber] == ['True']:
            if selection == 0:
                graphics.drawSelection(screen, 0)
            elif selection == 1:
                graphics.drawSelection(screen, 1)
            elif selection == 2:
                graphics.drawSelection(screen, 2)                
    else:
        graphics.displayText(screen, "The End.", "Congratulations! You have reached the end of this chapter!", False)  #Denotes the end of a chapter 
        
    
    pygame.display.flip()



main() #Runs the game
    