import pygame

pygame.init() #to initialize pygame:)

screen = pygame.display.set_mode((800, 600)) #to access the display

#Tittle and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)



#player
playerimg = pygame.image.load('shipp.png') 
playerX = 370
playerY = 480

def player():
    screen.blit(playerimg,(playerX, playerY ))# blit means to draw


# create an event which allows to exit the display
running = True
while running:

        #background colour
    screen.fill((0,0,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    player()# we call the function here so that it will always appear 
    pygame.display.update()