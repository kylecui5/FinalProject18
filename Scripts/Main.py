"""Main File"""

import sys
import pygame
import Drawer
import ImageAnalyzer

pygame.init()
screen = pygame.display.set_mode((1200, 750))

'''
def exampleLoop():
    running = True

    while running:
        for e in pygame.event.get():    # get each event in the event queue... 
            if e.type == pygame.QUIT:   # ...and if that event is QUIT...
                running = False         # ......set running to False so the main loop ends
        
            if e.type == pygame.MOUSEMOTION:        # if the event is mouse motion...
                print(pygame.mouse.get_pos())       # ...print the mouse's locaation
            if e.type == pygame.MOUSEBUTTONDOWN:    # if the event type is a button press...
                pygame.draw.circle(screen, (10, 70, 255), pygame.mouse.get_pos(), 20)  # draw a blue circle with radius 20 at the mouse's position
    
        pygame.display.flip()               # update the display
'''

def clearScreen(color = (255, 112, 112)):
    """Fills entire screen with a single color"""
    screen.fill(color)

def homeScreen():
    """Displays Home screen"""
    clearScreen()
    homeScreenLoop = True

    #Draw screen text
    largeFont = pygame.font.SysFont("leelawadeeuisemilight", 48)
    smallFont = pygame.font.SysFont("leelawadeeuisemilight", 36)

    welcomeText = largeFont.render("Kyle's \"Slow, Scribble!\"", 1, (10, 10, 10))
    playButtonText = smallFont.render("Play!", 1, (10, 10, 10))
    baselineDrawingsText = smallFont.render("Set Baseline Drawings", 1, (10, 10, 10))

    welcomeTextPos = welcomeText.get_rect(centerx = 600, y=125)
    playButtonTextPos = playButtonText.get_rect(x = 550, y = 400)
    baselineDrawingsTextPos = baselineDrawingsText.get_rect(x = 430, y = 500)

    pygame.draw.rect(screen, (255, 220, 84), (490, 385, 185, 85))
    pygame.draw.rect(screen, (255, 220, 84), (375, 485, 430, 85))
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
            pygame.draw.rect(screen, (255, 204, 0), (490, 385, 185, 85))
            screen.blit(playButtonText, playButtonTextPos)
        elif 805 > mousePos[0] > 375 and 570 > mousePos[1] > 485:
            #Hover over baseline drawings button
            pygame.draw.rect(screen, (255, 204, 0), (375, 485, 430, 85))
            screen.blit(baselineDrawingsText, baselineDrawingsTextPos)
        else:
            #Reset buttons
            pygame.draw.rect(screen, (255, 220, 84), (490, 385, 185, 85))
            pygame.draw.rect(screen, (255, 220, 84), (375, 485, 430, 85))
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
                    homeScreenLoop = False
                    baselineDrawings()
            
        pygame.display.flip()

homeScreen()

def baselineDrawings():
    """Displays baseline drawings screen to set baseline drawings"""
    


def play():
    """Plays the actual game"""
    