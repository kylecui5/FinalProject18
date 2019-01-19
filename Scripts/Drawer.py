import sys
import os
import json
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 750))

def showWhatToDraw(titleOfDrawing):
    """Displays a screen with text to tell the user what to draw"""
    screen.fill((255, 112, 112))

    userHasNotClicked = True

    textColor = (10, 10, 10)
    largeFont = pygame.font.SysFont("leelawadeeuisemilight", 48)
    drawText = largeFont.render(f"Draw a(n): {titleOfDrawing}!", 1, textColor)
    drawTextPos = drawText.get_rect(centerx = 600, y=125)

    screen.blit(drawText, drawTextPos)
    pygame.display.flip()

    print(f"Blit {titleOfDrawing} to screen")


    while userHasNotClicked:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                userHasNotClicked = False
    
    print("exiting showWhatToDraw")

def writeCoordsToFile(listOfCoords):
    """Writes the list of coordinates to a saved text file using JSON"""

    path = os.path.abspath('BaselineDrawings.txt')
    
    print(path)
    
    baselineFile = open(path, "a")
    json.dump(listOfCoords, baselineFile)

def draw(drawing, settingBaselineDrawings):
    """"Lets the user draw an object"""
    stillDrawing = True

    #Restart and Finished buttons
    textColor = (10, 10, 10)
    inactiveButtonColor = (255, 220, 84)
    activeButtonColor = (255, 204, 0)

    smallFont = pygame.font.SysFont("leelawadeeuisemilight", 36)

    restartText = smallFont.render("Restart!", 1, textColor)
    finishedText = smallFont.render("Finished!", 1, textColor)

    restartTextPos = restartText.get_rect(centerx = 475, y=600)
    finishedTextPos = finishedText.get_rect(x = 675, y = 600)
    restartButtonPos = (400, 585, 150, 85)
    finishedButtonPos = (660, 585, 160, 85)

    pygame.draw.rect(screen, inactiveButtonColor, restartButtonPos)
    pygame.draw.rect(screen, inactiveButtonColor, finishedButtonPos)
    screen.blit(restartText, restartTextPos)
    screen.blit(finishedText, finishedTextPos)

    pygame.display.flip()

    listOfMouseCoordsString = ""
    listOfMouseCoords = []
    shortenedListOfMouseCoords = []
    circleCount = 0
    coordsCount = 1

    #Check for user input
    while stillDrawing:

        mousePos = pygame.mouse.get_pos()

        if 550 > mousePos[0] > 400 and 670 > mousePos[1] > 585:
            #Hover over Restart button
            pygame.draw.rect(screen, activeButtonColor, restartButtonPos)
            screen.blit(restartText, restartTextPos)
        elif 820 > mousePos[0] > 660 and 670 > mousePos[1] > 585:
            #Hover over Finished button
            pygame.draw.rect(screen, activeButtonColor, finishedButtonPos)
            screen.blit(finishedText, finishedTextPos)
        else:
            #Reset buttons
            pygame.draw.rect(screen, inactiveButtonColor, restartButtonPos)
            pygame.draw.rect(screen, inactiveButtonColor, finishedButtonPos)
            screen.blit(restartText, restartTextPos)
            screen.blit(finishedText, finishedTextPos)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if 550 > mousePos[0] > 400 and 670 > mousePos[1] > 585:
                    #Press Restart button
                    screen.fill((255, 112, 112))
                    draw(drawing, settingBaselineDrawings)
                    stillDrawing = False
                elif 820 > mousePos[0] > 660 and 670 > mousePos[1] > 585:
                    #Press Finished button
                    screen.fill((255, 112, 112))
                    stillDrawing = False

            #Mouse is being held (mouse is drawing)
            elif pygame.mouse.get_pressed()[0]:

                    print(f"drawing a circle at {pygame.mouse.get_pos()}")

                    listOfMouseCoords += pygame.mouse.get_pos()

                    if coordsCount % 50 == 0:
                        shortenedListOfMouseCoords.append(pygame.mouse.get_pos())
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

    listOfMouseCoordsString = f"{len(shortenedListOfMouseCoords)}\n {drawing}:\n {shortenedListOfMouseCoords}"

    print(f"Long list: {listOfMouseCoords}")
    print(f"Short list: {shortenedListOfMouseCoords}")
    print(listOfMouseCoordsString)
    print(settingBaselineDrawings)

    if settingBaselineDrawings:
        writeCoordsToFile(listOfMouseCoordsString)