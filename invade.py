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
#ENemy
enemyimg = pygame.image.load('ufo.png') 
enemyX = 370
enenmyY = 480

move_left = move_right = move_up = move_down = False

def player(x, y):
    screen.blit(playerimg,(x, y ))# blit means to draw


# create an event which allows to exit the display
running = True
while running:

        #background colour
    screen.fill((0,0,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #event for key strokes to move characters
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
            # when key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
            

    if move_left:
        playerX -= 0.5
    if move_right:
        playerX += 0.5
    
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    player(playerX, playerY)# we call the function here so that it will always appear 
    pygame.display.update()
