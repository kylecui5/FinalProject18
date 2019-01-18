"""Main File"""

import sys
import pygame
import Drawer
import ImageAnalyzer

pygame.init()

screen = pygame.display.set_mode((1200, 750))
drawings = ["coffee mug", "apple", "clock", "basketball", "baseball", "candle", "bird", "smiley face"]

def clearScreen(backgroundColor = (255, 112, 112)):
    """Fills entire screen with a single color"""
    screen.fill(backgroundColor)

def homeScreen():
    """Displays Home screen"""
    clearScreen()
    homeScreenLoop = True

    #Draw screen text and buttons
    textColor = (10, 10, 10)
    inactiveButtonColor = (255, 220, 84)
    activeButtonColor = (255, 204, 0)

    largeFont = pygame.font.SysFont("leelawadeeuisemilight", 48)
    smallFont = pygame.font.SysFont("leelawadeeuisemilight", 36)

    welcomeText = largeFont.render("Kyle's \"Slow, Scribble!\"", 1, textColor)
    playButtonText = smallFont.render("Play!", 1, textColor)
    baselineDrawingsText = smallFont.render("Set Baseline Drawings", 1, textColor)

    welcomeTextPos = welcomeText.get_rect(centerx = 600, y = 125)
    playButtonTextPos = playButtonText.get_rect(x = 550, y = 400)
    baselineDrawingsTextPos = baselineDrawingsText.get_rect(x = 430, y = 500)
    playButtonPos = (490, 385, 185, 85)
    baselineDrawingsButtonPos = (375, 485, 430, 85)

    pygame.draw.rect(screen, inactiveButtonColor, playButtonPos)
    pygame.draw.rect(screen, inactiveButtonColor, baselineDrawingsButtonPos)
    screen.blit(welcomeText, welcomeTextPos)
    screen.blit(playButtonText, playButtonTextPos)
    screen.blit(baselineDrawingsText, baselineDrawingsTextPos)

    #Check for user input
    while homeScreenLoop:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        mousePos = pygame.mouse.get_pos()

        if 675 > mousePos[0] > 490 and 470 > mousePos[1] > 385:
            #Hover over play button
            pygame.draw.rect(screen, activeButtonColor, playButtonPos)
            screen.blit(playButtonText, playButtonTextPos)
        elif 805 > mousePos[0] > 375 and 570 > mousePos[1] > 485:
            #Hover over baseline drawings button
            pygame.draw.rect(screen, activeButtonColor, baselineDrawingsButtonPos)
            screen.blit(baselineDrawingsText, baselineDrawingsTextPos)
        else:
            #Reset buttons
            pygame.draw.rect(screen, inactiveButtonColor, playButtonPos)
            pygame.draw.rect(screen, inactiveButtonColor, baselineDrawingsButtonPos)
            screen.blit(playButtonText, playButtonTextPos)
            screen.blit(baselineDrawingsText, baselineDrawingsTextPos)

        #Check for mouse clicks
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if 675 > mousePos[0] > 490 and 470 > mousePos[1] > 385:
                    #Press play button
                    homeScreenLoop = False
                    play()

                elif 805 > mousePos[0] > 375 and 570 > mousePos[1] > 485:
                    #Press baseline drawings button 

                    print("pressed baseline drawings button")

                    homeScreenLoop = False
                    baselineDrawings()
            
        pygame.display.flip()
                
def baselineDrawings():
    """Displays baseline drawings screen to set baseline drawings"""
    clearScreen()
    passWordCheckRunning = True
    setBaselineDrawingsRunning = False

    #Password check

    print("in password check")

    password = "poopoo"
    inputText = ''
    inputBox = pygame.Rect(350, 282, 500, 50)
    inputBoxActive = False

    textColor = (10, 10, 10)
    smallFont = pygame.font.SysFont("leelawadeeuisemilight", 36)
    smallerFont = pygame.font.SysFont("leelawadeeuisemilight", 24)
    passwordText = smallFont.render("Password:", 1, textColor)
    passwordTextPos = passwordText.get_rect(x = 525, y = 200)
    placeholderText = smallerFont.render("Click to enter password...", 1, textColor)
    placeholderTextPos = placeholderText.get_rect(x = 375, y = 290)
    screen.blit(passwordText, passwordTextPos)
    screen.blit(placeholderText, placeholderTextPos)


    print("about to run password check loop")

    while passWordCheckRunning:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if inputBox.collidepoint(e.pos):
                    
                    print("mouse click collided with input box")

                    inputBoxActive = True
                    pygame.draw.rect(screen, (255, 112, 112), (351, 283, 499, 45))
                else:

                    print("mouse click outside of input box")

                    inputBoxActive = False
                    inputText = ''
                    screen.blit(placeholderText, placeholderTextPos)
            if e.type == pygame.KEYDOWN:
                if inputBoxActive:
                    if e.key == pygame.K_RETURN:
                        passWordCheckRunning = False
                        if inputText == password:

                            print("access granted")

                            setBaselineDrawingsRunning = True
                        else:
                            homeScreen()
                    elif e.key == pygame.K_BACKSPACE:
                        inputText = inputText[:-1]
                    else:

                        print(f"adding {e.unicode} to inputText string")

                        inputText += e.unicode

        pygame.draw.rect(screen, (0, 157, 255), inputBox, 2)
        pygame.display.flip()

    #Admin draws each object and saves the data to the BaselineDrawings.txt file
    while setBaselineDrawingsRunning:

        print("prepared to set baseline drawings")

        clearScreen()
        for n in range(len(drawings)):
            Drawer.showWhatToDraw(drawings[n])
            clearScreen()
            Drawer.draw(drawings[n], True)

        setBaselineDrawingsRunning = False
    
    homeScreen()

def play():
    """Plays the actual game"""
    
homeScreen()