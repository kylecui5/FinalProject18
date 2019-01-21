import sys
import os
import json
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 750))

class Drawer:
    """Provides drawing functions"""

    def __init__(self, textColor, largeFont, smallFont, inactiveButtonColor, activeButtonColor):
        """Initializes variables"""
        self.textColor = textColor
        self.largeFont = largeFont
        self.smallFont = smallFont
        self.inactiveButtonColor = inactiveButtonColor
        self.activeButtonColor = activeButtonColor
        self.backgroundColor = (255, 112, 112)

    def showWhatToDraw(self, titleOfDrawing):
        """Displays a screen with text to tell the user what to draw"""

        userHasNotClicked = True

        drawText = self.largeFont.render(f"Draw a(n): {titleOfDrawing}!", 1, self.textColor)
        drawTextPos = drawText.get_rect(centerx = 600, y=125)

        screen.blit(drawText, drawTextPos)
        pygame.display.flip()

        while userHasNotClicked:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    userHasNotClicked = False
    
    def deleteFileContents(self, drawing):
        """Deletes file contents in drawing file"""

        if drawing == "apple":
            path = os.path.abspath('Apple.txt')
        elif drawing == "bird":
            path = os.path.abspath('Bird.txt')
        elif drawing == "candle":
            path = os.path.abspath('Candle.txt')
        elif drawing == "clock":
            path = os.path.abspath('Clock.txt')
        elif drawing == "coffee mug":
            path = os.path.abspath('CoffeeMug.txt')
        elif drawing == "finger":
            path = os.path.abspath('Finger.txt')
        elif drawing == "moustache":
            path = os.path.abspath('Moustache.txt')
        elif drawing == "smiley face":
            path = os.path.abspath('SmileyFace.txt')

        baselineFile = open(path, "w")
        baselineFile.write("")

    def writeCoordsToFile(self, listOfCoords, drawing):
        """Writes the list of coordinates to a saved text file using JSON"""

        if drawing == "apple":
            path = os.path.abspath('Apple.txt')
        elif drawing == "bird":
            path = os.path.abspath('Bird.txt')
        elif drawing == "candle":
            path = os.path.abspath('Candle.txt')
        elif drawing == "clock":
            path = os.path.abspath('Clock.txt')
        elif drawing == "coffee mug":
            path = os.path.abspath('CoffeeMug.txt')
        elif drawing == "finger":
            path = os.path.abspath('Finger.txt')
        elif drawing == "moustache":
            path = os.path.abspath('Moustache.txt')
        elif drawing == "smiley face":
            path = os.path.abspath('SmileyFace.txt')
        
        baselineFile = open(path, "a")
        json.dump(listOfCoords, baselineFile)

    def draw(self, drawing, settingBaselineDrawings):
        """"Lets the user draw an object"""

        stillDrawing = True

        #Restart and Finished buttons
        restartText = self.smallFont.render("Restart!", 1, self.textColor)
        finishedText = self.smallFont.render("Finished!", 1, self.textColor)

        restartTextPos = restartText.get_rect(centerx = 475, y=600)
        finishedTextPos = finishedText.get_rect(x = 675, y = 600)
        restartButtonPos = pygame.Rect(400, 585, 150, 85)
        finishedButtonPos = pygame.Rect(660, 585, 160, 85)

        screen.blit(restartText, restartTextPos)
        screen.blit(finishedText, finishedTextPos)
        pygame.draw.rect(screen, (255, 255, 255), (300, 100, 600, 450))
        pygame.display.flip()

        listOfMouseCoordsString = ""
        listOfMouseCoords = []
        shortenedListOfMouseCoords = ""
        numCoordsInShortenedList = 0
        circleCount = 0
        coordsCount = 1

        #Check for user input
        while stillDrawing:

            mousePos = pygame.mouse.get_pos()

            if 550 > mousePos[0] > 400 and 670 > mousePos[1] > 585:
                #Hover over Restart button
                pygame.draw.rect(screen, self.activeButtonColor, restartButtonPos)
                screen.blit(restartText, restartTextPos)
            elif 820 > mousePos[0] > 660 and 670 > mousePos[1] > 585:
                #Hover over Finished button
                pygame.draw.rect(screen, self.activeButtonColor, finishedButtonPos)
                screen.blit(finishedText, finishedTextPos)
            else:
                #Reset buttons
                pygame.draw.rect(screen, self.inactiveButtonColor, restartButtonPos)
                pygame.draw.rect(screen, self.inactiveButtonColor, finishedButtonPos)
                screen.blit(restartText, restartTextPos)
                screen.blit(finishedText, finishedTextPos)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    #if 550 > mousePos[0] > 400 and 670 > mousePos[1] > 585:
                    if restartButtonPos.collidepoint(e.pos):
                        #Press Restart button
                        screen.fill(self.backgroundColor)
                        self.showWhatToDraw(drawing)
                        screen.fill(self.backgroundColor)
                        return self.draw(drawing, settingBaselineDrawings)
                    #elif 820 > mousePos[0] > 660 and 670 > mousePos[1] > 585:
                    elif finishedButtonPos.collidepoint(e.pos):
                        #Press Finished button
                        screen.fill(self.backgroundColor)
                        stillDrawing = False

                #Mouse is being held (mouse is drawing)
                elif pygame.mouse.get_pressed()[0]:

                        listOfMouseCoords += pygame.mouse.get_pos()

                        if coordsCount % 25 == 0:
                            shortenedListOfMouseCoords += f"\n{(pygame.mouse.get_pos())}"
                            numCoordsInShortenedList += 1
                        coordsCount += 1

                        pygame.draw.circle(screen, (10, 70, 255), pygame.mouse.get_pos(), 3)

                        if circleCount > 0:
                            #Connects the two previous drawn circles with a line
                            pygame.draw.line(screen, (10, 70, 255), (listOfMouseCoords[circleCount-3], listOfMouseCoords[circleCount-2]), (listOfMouseCoords[circleCount-1], listOfMouseCoords[circleCount]), 6)
                            circleCount += 2
                        else:
                            circleCount += 3
                else:
                    circleCount = 0

            pygame.display.flip()

        listOfMouseCoordsString = f"{numCoordsInShortenedList}\n{drawing}:{shortenedListOfMouseCoords}"

        if settingBaselineDrawings:
            self.deleteFileContents(drawing)
            self.writeCoordsToFile(listOfMouseCoordsString, drawing)
        else:
            return listOfMouseCoordsString