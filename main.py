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


class StartMenu():
    
    def __init__(self, screen, bg_colour = BLACK):
        self.screen = screen
        self.bg_colour = bg_colour
        self.clock = pygame.time.Clock()
        self.lessonButton = graphics.Button(screen, 100, 100, 400, 400, LESSON)
        self.quizButton = graphics.Button(screen, 500, 100, 600, 700, TRIVIA)
    
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
                if self.lessonButton.isPressed():
                    state = self.lessonButton.getState()
                elif self.quizButton.isPressed():
                    state = self.quizButton.getState()
        return state != MENU
    
    
    #Updates the screen
    def updateScreen(self):
        self.screen.fill(BLACK)
        self.lessonButton.drawButton()
        self.quizButton.drawButton()
        pygame.display.flip()
        
        
        
class PlayQuiz():
    def __init__(self, screen, bg_colour = BLACK):
        self.screen = screen
        self.bg_colour = bg_colour
        self.questionList, self.selectionList, self.answerList, self.scoreList, self.timeList = wordProcessing.getTriviaScript("Quiz1.txt")        
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
                if lineNumber < len(self.questionList):
                    #Process input if there the dialog is a selection
                    if event.key == pygame.K_UP:
                        selection = max(0, selection-1)
                    elif event.key == pygame.K_DOWN:
                        selection = min(3, selection +1)
                    elif event.key == pygame.K_SPACE:
                        if selection+1 == int(self.answerList[lineNumber]):
                            score += int(self.scoreList[lineNumber])
                        lineNumber += 1
                        timer = 0
   
            #Starts trivia timer when doing a quiz
            elif event.type == TIMER:
                    timer += 1
        
        return done
    
    
    #Updates the screen
    def updateScreen(self):
        global lineNumber, timer
        self.screen.fill(WHITE)
        graphics.setBackground(self.screen, "Blackboard.jpg")
        graphics.setCharacter(self.screen, "Sensei.png", int(((self.screen.get_width())/1.75)), 100)
        graphics.drawDialogBox(self.screen, BLACK, 0.65)
    
        #Display dialog while there is still script
        if lineNumber < len(self.questionList):
            #text = "".join(wordProcessing.processSelection(self.selectionList[lineNumber]))
            graphics.displayDialog(self.screen, self.questionList[lineNumber], self.selectionList[lineNumber], True)
            
        
            if selection == 0:
                graphics.drawSelection(self.screen, 0)
            elif selection == 1:
                graphics.drawSelection(self.screen, 1)
            elif selection == 2:
                graphics.drawSelection(self.screen, 2)
            elif selection == 3:
                graphics.drawSelection(self.screen, 3)
            
            #Draws the timer, and updates the line number if the user fails
            graphics.drawTimer(self.screen, timer, int(self.timeList[lineNumber]))

            if timer >= int(self.timeList[lineNumber]):
                lineNumber += 1
                timer = 0
    
        else:
            graphics.displayDialog(self.screen, "The End.", "Congratulations! You have reached the end of this chapter!", False)  #Denotes the end of a chapter
        graphics.printScore(self.screen, score)
        pygame.display.flip()    
        
        
class PlayStory():
    def __init__(self, screen, bg_colour = BLACK):
        self.screen = screen
        self.bg_colour = bg_colour
        self.backgroundPictureList, self.foregroundPictureList, self.speakerProfilePictureList, self.speakerList, self.dialogList = wordProcessing.getLessonScript("Lesson1.txt")  
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
                if lineNumber < len(self.backgroundPictureList):
                    #Process input if there the dialog is a selection
                    if event.key == pygame.K_SPACE:
                        lineNumber+= 1
                    elif event.key == pygame.K_LEFT:
                        lineNumber -= 1
                    elif event.key == pygame.K_RIGHT:
                        lineNumber += 1
        return done
    
    
    #Updates the screen
    def updateScreen(self):
        global lineNumber, timer
        
        self.screen.fill(WHITE)
        #Display dialog while there is still script
        if lineNumber < len(self.backgroundPictureList):
            graphics.setBackground(self.screen, self.backgroundPictureList[lineNumber])
            graphics.setCharacter(self.screen, self.foregroundPictureList[lineNumber],int(((self.screen.get_width())/3.5)), 100)
            graphics.drawDialogBox(self.screen, BLACK, 0.65)            
            #text = "".join(wordProcessing.processSelection(self.selectionList[lineNumber]))
            graphics.displayDialog(self.screen, self.speakerList[lineNumber], self.dialogList[lineNumber], False)
    
        else:
            graphics.setBackground(self.screen, self.backgroundPictureList[lineNumber-1])
            graphics.setCharacter(self.screen, self.foregroundPictureList[lineNumber-1], int(((self.screen.get_width())/3.5)), 100)
            graphics.drawDialogBox(self.screen, BLACK, 0.65)            
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
        elif state == TRIVIA:
            triviaGame = PlayQuiz(screen)
            triviaGame.gameLoop()
        elif state == LESSON:
            lessonGame = PlayStory(screen)
            lessonGame.gameLoop()
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