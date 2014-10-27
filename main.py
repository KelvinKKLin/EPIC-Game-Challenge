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

#Game States
MENU = 0
LESSON = 1
TRIVIA = 2

#User Defined Events
TIMER = 25

#Variable used to control the flow of the story

#Used for dialog
lineNumber = 0 
selection = 0
score = 0
timer = 0

#Used for start menu
state = MENU

quit = False

#Gets data from a story file
characterList, dialogList, referenceList, linearList, scoreList = wordProcessing.getDialog("test.txt")

class StartMenu():
    
    def __init__(self, screen, bg_colour = BLACK):
        self.screen = screen
        self.bg_colour = bg_colour
        self.clock = pygame.time.Clock()
        self.test = graphics.Button(screen, 100, 100, 400, 400, LESSON)
    
    def gameLoop(self):
        done = False
        clock = pygame.time.Clock()
        while not done:
            self.updateScreen()
            done = self.processEvents()
            clock.tick(60)
            
    #Processes user inputs
    def processEvents(self):
        global state, quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                return True
            if event.type == pygame.MOUSEBUTTONDOWN :
                if self.test.isPressed():
                    state = self.test.getState()
        return state != MENU
    
    
    #Updates the screen
    def updateScreen(self):
        self.screen.fill(BLACK)
        self.test.drawButton()
        pygame.display.flip()
        
        
        
class PlayDialog():
    def __init__(self, screen, bg_colour = BLACK):
        self.screen = screen
        self.bg_colour = bg_colour
        self.clock = pygame.time.Clock()
        
    #The game loop runs while the game is not over
    def gameLoop(self):
        done = False
        clock = pygame.time.Clock()
        pygame.time.set_timer(TIMER, 1000)
        while not done:
            done = self.processEvents()
            self.updateScreen()
            clock.tick(60)
            
    
    #Processes user inputs
    def processEvents(self):
        global lineNumber, selection, score, timer, quit
        done = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit = True
                return done
            #Processes Keyboard input
            elif event.type == pygame.KEYUP:
                #If there are still lines remaining 
                if lineNumber < len(characterList):
                    #Process input if there the dialog is a selection
                    if linearList[lineNumber] == ['True']:                        
                        if event.key == pygame.K_UP:
                            selection = max(0, selection-1)
                        elif event.key == pygame.K_DOWN:
                            selection = min(2, selection +1)
                        elif event.key == pygame.K_RETURN:
                            score += int(scoreList[lineNumber].split(",")[selection])
                            lineNumber =  int(referenceList[lineNumber].split(",")[selection])
                        
                    #Process input if the dialog is linear
                    elif event.key == pygame.K_SPACE:
                        lineNumber = int(referenceList[lineNumber])
                        
            #Starts trivia timer when doing a quiz
            elif event.type == TIMER:
                if lineNumber < len(characterList) and linearList[lineNumber] == ['True']:
                    timer += 1   
                elif timer != 0:
                    timer = 0
        return done
    
    
    #Updates the screen
    def updateScreen(self):
        global lineNumber
        self.screen.fill(WHITE)
        graphics.setBackground(self.screen, "background1.jpg")
        graphics.setCharacter(self.screen, "john.png")
        graphics.drawDialogBox(self.screen, BLACK, 0.65)
    
        #Display dialog while there is still script
        if lineNumber < len(characterList):
            graphics.displayDialog(self.screen, characterList[lineNumber], dialogList[lineNumber], linearList[lineNumber] == ['True'])
            
            #Draws selection boxes if the dialog is a selection
            if linearList[lineNumber] == ['True']:
                if selection == 0:
                    graphics.drawSelection(self.screen, 0)
                elif selection == 1:
                    graphics.drawSelection(self.screen, 1)
                elif selection == 2:
                    graphics.drawSelection(self.screen, 2)
                
                #Draws the timer, and updates the line number if the user fails
                graphics.drawTimer(self.screen, timer)
                if timer >= 10:
                    lineNumber = 0
        else:
            graphics.displayDialog(self.screen, "The End.", "Congratulations! You have reached the end of this chapter!", False)  #Denotes the end of a chapter
        graphics.printScore(self.screen, score)
        pygame.display.flip()    
        
        
#The main loop
def main():
    screen = initializeGame()
    while not quit:
        if state == MENU:
            menu = StartMenu(screen)
            menu.gameLoop()
        elif state == LESSON:
            dialogGame = PlayDialog(screen)
            dialogGame.gameLoop()
    pygame.quit()
    print "Done"

#Initializes pyGame, and returns a screen for the game
def initializeGame():
    pygame.init()
    size = (1050, 750)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Test Game")
    return screen

main() #Runs the game