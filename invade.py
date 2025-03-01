import pygame

pygame.init() #to initialize pygame:)

scree = pygame.display.set_mode((800, 600)) #to access the display

#Tittle and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# create an event which allows to exit the display
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

