import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 750))

def draw(drawing):
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

    #Check for user input
    while stillDrawing:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

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

        #Check for mouse clicks
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if 550 > mousePos[0] > 400 and 670 > mousePos[1] > 585:
                    #Press Restart button
                    screen.fill(255, 112, 112)
                    draw(drawing)
                    stillDrawing = False
                elif 820 > mousePos[0] > 660 and 670 > mousePos[1] > 585:
                    #Press Finished button
                    screen.fill(255, 112, 112)
                    stillDrawing = False
            elif pygame.mouse.get_pressed()[0]:

                    print("drawing a circle")

                    pygame.draw.circle(screen, (10, 70, 255), pygame.mouse.get_pos(), 3)
        pygame.display.flip()

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